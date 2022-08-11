from django.urls import path
from .views import ListCategory, DetailCategory,ListBook,DetailBook,ListProduct,DetailProduct

urlpatterns = [
    path('category/', ListCategory.as_view(), name='category'),
    #path('category/<int:pk>/', DetailCategory.as_view(), name='singlecategory'),
    #path('book', ListBook.as_view(),name='book'),
    #path('book/<int:pk>/', DetailBook.as_view(), name='singlebook'),
    #path('product', ListProduct.as_view(), name='product'),
    #path('category/<int:pk>/', DetailProduct.as_view(), name='singleproduct'),
]
