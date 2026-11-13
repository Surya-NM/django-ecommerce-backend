from decimal import Decimal

from django.db import transaction

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from .models import Order, OrderItem
from .serializers import OrderSerializer

from cart.models import cart as Cart


class CreateOrderAPIView(APIView):

    permission_classes = [IsAuthenticated]

    @transaction.atomic
    def post(self, request):

        # 1. Get user's cart
        try:
            cart = Cart.objects.get(user=request.user)

        except Cart.DoesNotExist:
            return Response(
                {"error": "Cart not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        # 2. Get cart items
        cart_items = cart.Items.select_related("product")

        # 3. Check empty cart
        if not cart_items.exists():
            return Response(
                {"error": "Cart is empty"},
                status=status.HTTP_400_BAD_REQUEST
            )

        total_price = Decimal("0.00")

        # 4. Check stock
        for cart_item in cart_items:

            product = cart_item.product

            if cart_item.quantity > product.stock:
                return Response(
                    {
                        "error": (
                            f"Only {product.stock} stock available "
                            f"for {product.name}"
                        )
                    },
                    status=status.HTTP_400_BAD_REQUEST
                )

        # 5. Create Order
        order = Order.objects.create(
            user=request.user,
            total_price=Decimal("0.00"),
            status="pending"
        )

        # 6. Create OrderItems
        for cart_item in cart_items:

            product = cart_item.product
            quantity = cart_item.quantity
            price = product.price

            item_total = price * quantity

            OrderItem.objects.create(
                order=order,
                product=product,
                quantity=quantity,
                price=price,
                total_price=item_total
            )

            # 7. Reduce stock
            product.stock -= quantity

            product.save(
                update_fields=["stock"]
            )

            # 8. Add to order total
            total_price += item_total

        # 9. Update order total
        order.total_price = total_price

        order.save(
            update_fields=["total_price"]
        )

        # 10. Clear cart
        cart.Items.all().delete()

        # 11. Response
        serializer = OrderSerializer(order)

        return Response(
            {
                "message": "Order created successfully",
                "order": serializer.data
            },
            status=status.HTTP_201_CREATED
        )


class OrderListAPIView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):

        orders = (
            Order.objects
            .filter(user=request.user)
            .prefetch_related("items__product")
            .order_by("-created_at")
        )

        serializer = OrderSerializer(
            orders,
            many=True
        )

        return Response(serializer.data)


class OrderDetailAPIView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request, pk):

        try:
            order = (
                Order.objects
                .prefetch_related("items__product")
                .get(
                    id=pk,
                    user=request.user
                )
            )

        except Order.DoesNotExist:
            return Response(
                {"error": "Order not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = OrderSerializer(order)

        return Response(serializer.data)


class CancelOrderAPIView(APIView):

    permission_classes = [IsAuthenticated]

    @transaction.atomic
    def post(self, request, pk):

        try:
            order = (
                Order.objects
                .prefetch_related("items__product")
                .get(
                    id=pk,
                    user=request.user
                )
            )

        except Order.DoesNotExist:
            return Response(
                {"error": "Order not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        # 1. Already cancelled
        if order.status == "cancelled":
            return Response(
                {"error": "Order is already cancelled"},
                status=status.HTTP_400_BAD_REQUEST
            )

        # 2. Delivered order cannot be cancelled
        if order.status == "delivered":
            return Response(
                {"error": "Delivered order cannot be cancelled"},
                status=status.HTTP_400_BAD_REQUEST
            )

        # 3. Restore stock
        for item in order.items.all():

            product = item.product

            product.stock += item.quantity

            product.save(
                update_fields=["stock"]
            )

        # 4. Change status
        order.status = "cancelled"

        order.save(
            update_fields=[
                "status",
                "updated_at"
            ]
        )

        return Response(
            {
                "message": "Order cancelled successfully"
            },
            status=status.HTTP_200_OK
        )

# ADMIN LIST

class AdminOrderList (APIView):
    permission_classes = [IsAuthenticated]
    def get (self, request):
        if request.user.role != 'admin':
            return Response(
                {"errors" : "Admin access required"},
                status=status.HTTP_403_FORBIDDEN
            )

        orders = (
            Order.objects.all()
            .prefetch_related('items__product')
            .order_by("-created_at")
        )

        serializer = OrderSerializer(
            orders,
            many = True
        )
        return Response(serializer.data)

class AdminOrderStatusUpdateAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def patch (self, request,pk):
        if request.user.role != 'admin':
                    return Response(
                        {"errors" : "Admin access required"},
                        status=status.HTTP_403_FORBIDDEN
                    )
        try:
            order = Order.objects.get(id = pk)

        except Order.DoesNotExist :
            return Response(
                {"errors": "Order Not Found"},
                status=status.HTTP_404_NOT_FOUND
            )

   # Get new status

        new_request = request.data.get("status")

        allowed_status =  [
            "pending",
            "confirmed",
            "processing",
            "shipped",
            "delivered",
            "cancelled"
        ]    

        if new_request not in allowed_status:
            return Response(
                {"errors" : "Invalid order status"},
                status=status.HTTP_400_BAD_REQUEST
            )
         
         # Update status
        order.status = new_request
        order.save(update_fields=['status', 'updated_at'])

        return Response(
            {'message' : "Order status updated successfully",
            "order_id": order.id,
            "status": order.status},
            status=status.HTTP_200_OK
        )

        

        