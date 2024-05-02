from django.urls import  path
from EasyStock.views import ProductListView, ProductDetailView, ProductCreateView, ProductDeleteView, ProductUpdateView
from EasyStock.views.category import CategoryCreateView

urlpatterns = [
    path('product/create/', ProductCreateView.as_view(), name='product-create'),
    path('category/create/', CategoryCreateView.as_view(), name='category-create'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('products/', ProductListView.as_view(), name='product-list'),
    path('product/<int:pk>/update/', ProductUpdateView.as_view(), name='product-update'),
    path('product/<int:pk>/delete/', ProductDeleteView.as_view(), name='product-delete'),
]