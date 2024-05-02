from rest_framework import generics
from EasyStock.models import Category
from EasyStock.serializers import CategorySerializer


class CategoryCreateView(generics.CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
