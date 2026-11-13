from rest_framework import generics
from .models import Product, Category
from .serializers import ProductSerializer, CategorySerializer
from rest_framework.filters import OrderingFilter, SearchFilter
from django_filters.rest_framework import DjangoFilterBackend

# Category CURD
class Clistcreateview (generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class Cretriveupdatedestory (generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

# Product CURD and Filter, Ordering, Searching
class Plistcreateview (generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_serializer(self, *args, **kwargs):

        if self.request.method == 'POST':
            kwargs['many'] = True

        return super().get_serializer(*args, **kwargs)

    filter_backends = [DjangoFilterBackend,
                       OrderingFilter,
                       SearchFilter]       

    
    filterset_fields = ['category', 'price', 'is_available']

    search_fields = ['name', 'description']

    ordering_fields = ['price', 'created_at', 'name']

    ordering = ['-created_at']

class Pretriveupdatedestory (generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer