from django.urls import path
from . import views

# http://127.0.0.1:8000 => index
# http://127.0.0.1:8000/details => details
# http://127.0.0.1:8000/list => list
urlpatterns = [
    path('', views.index, name="index"),
    path('index', views.index, name="index"),
    path('details', views.details, name="details"),
    path('productList', views.productList, name="productList"),
    # path('telefon', views.telefon, name="telefon"),
    # path('bilgisayar', views.bilgisayar, name="bilgisayar"),
    path('<int:category_id>', views.getProductsByCategoryId),
    #sıralama önemli products/5 yazdığımızda bunu integer olarak algılaması için int: yukarıda olmalı
    path('<str:category>', views.getProductsByCategory, name="products_by_category"),
]