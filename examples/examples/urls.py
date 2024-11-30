"""
URL configuration for examples project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

# http://127.0.0.1:8000/ => index metotu eğer boş bıraksaydık bu şekildeydi.
# http://127.0.0.1:8000/products => index metotu => aşağıdaki path kısmına products/ yazarsak bu şekilde istek atmalıyız
# yani myapp için şu anda path kısmını boş bırakmayıp products/ url si belirledik. 
urlpatterns = [
    path("products/",include("myapp.urls")),
    path("admin/", admin.site.urls),
]