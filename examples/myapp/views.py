from unicodedata import category
from django.http import HttpResponseNotFound
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse

data = {
    "telefon": "telefon kategorisindeki ürünler",
    "bilgisayar": "bilgisayar kategorisindeki ürünler!!!",
    "elektronik": "elektronik kategorisindeki ürünler"
}

# Create your views here.

# http://127.0.0.1:8000
def index(request):

    list_items = ""
    category_list = list(data.keys())
    for category in category_list:
        redirect_path = reverse("products_by_category", args= [category])
        list_items +=f"<li><a href=\"{redirect_path}\"><b>{category}</b> : </a>{data[category]}</li>"

    html = f"<ul>{list_items}</ul>"    
    return HttpResponse(html)

def details(request):
    return HttpResponse("details")

def  productList(request):
    return HttpResponse("list")

# def getProductsByCategory(request, category):
#     category_text = None
#     if category == "bilgisayar":
#         category_text = "Bilgisasyar kategorisindeki ürünler"
#     elif category == "telefon":
#         category_text = "Telefon kategorisindeki ürünler"
#     else:
#         category_text = "Yanlış kategori seçimi"      
#     return HttpResponse(category_text)

def getProductsByCategory(request, category):
    try:
        category_text = data[category]
        return HttpResponse(f"<h1>{category_text}</h1>")
        # return HttpResponse(category_text)
    except:
        return HttpResponseNotFound(f"<h1>Yanlış Kategori Seçimi</h1>")
# def  telefon(request):
#     return HttpResponse("Telefon kategorisindeki ürünler")

# def  bilgisayar(request):
#     return HttpResponse("Bilgisayar kategorisindeki ürünler")

def getProductsByCategoryId(request, category_id):
    category_list = list(data.keys())
    if category_id > len(category_list):
         return HttpResponseNotFound("Yanlış Kategori Seçimi")
    category_name = category_list[category_id-1]

    redirect_path = reverse("products_by_category", args= [category_name])
    return redirect(redirect_path)
    # return redirect("/products/"+ category_name)
