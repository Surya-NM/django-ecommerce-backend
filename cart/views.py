from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .models import  cartItem as CartItem
from .models import cart as Cart
from .serializers import CartSerilaizer
from products.models import Product
from rest_framework import status


class CartView (APIView):
    permission_classes = [IsAuthenticated]

    def get (self, request):
        cart, created = Cart.objects.get_or_create(
            user = request.user
        )

        serializer = CartSerilaizer(cart)
        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )

class AddToCart (APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        user = request.user

        product_id = request.data.get('product_id') 
        quantity = request.data.get('quantity')

        if not product_id:
            return Response(
                {"errors" : "Product id is required"},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            product = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            return Response (
                {"errors" : "Product not found"},
                status=status.HTTP_400_BAD_REQUEST
            )
        if not product.is_available:
            return Response(
                {"errors" : "Product is not available"},
                status=status.HTTP_400_BAD_REQUEST
            )

        if product.stock <=0 :
            return Response(
                {"errors" : "Product is out of stock"},
                status=status.HTTP_400_BAD_REQUEST
            )

        if quantity is None:
            return Response(
                {'errors' : 'Quantity is requried'},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            quantity = int(quantity)
        except ValueError:
            return Response(
                {"errors" : "Quantity Must be a Number"},
                status=status.HTTP_400_BAD_REQUEST
            )

        if quantity <= 0 :
            return Response(
                {'errors' : 'Quantity Must be Greater than 0'},
                status=status.HTTP_400_BAD_REQUEST
            )

        cart, created = Cart.objects.get_or_create(
    user=user
)

# Check whether the product already exists in the cart.
        cart_item = CartItem.objects.filter(
    cart=cart,
    product=product
).first()

# if the product already exists in the cart increase the quantity
        if cart_item :
            new_quantity = cart_item.quantity + quantity

#Is the quantity greater than the stock?
            if new_quantity > product.stock:
             return Response(
                {"errors" : "Requested quantity exceeds available stock"},
                status=status.HTTP_400_BAD_REQUEST
            )
            cart_item.quantity = new_quantity
            cart_item.save()
        else:
       

          if quantity > product.stock:
            return Response(
                      {
                        "error": "Requested quantity exceeds available stock"
                    },
                    status=status.HTTP_400_BAD_REQUEST
                )
          CartItem.objects.create(
            cart=cart,
            product=product,
            quantity=quantity
        )
        serializer = CartSerilaizer(cart)
        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )


  
           


        

        


 



        
   

        