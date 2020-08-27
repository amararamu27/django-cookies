from django.shortcuts import render, redirect
from app26.forms import ProductForm
from app26.models import ProductModel


def showIndex(request):
    return render(request,'index.html',{"data":ProductModel.objects.all(),'data1':len(request.COOKIES)-1})


def adminPage(request):
    return render(request,'admin.html',{'data':ProductForm()})


def productSave(request):
    product_save = ProductForm(request.POST, request.FILES)
    if product_save.is_valid():
        product_save.save()
        return render(request,'index.html',{"data":ProductModel.objects.all()})
    else:
        return render(request,'admin.html',{'data':ProductForm()})


def addCart(request):
    pno = request.GET.get('id')
    value = request.GET.get('val')
    # response = render(request,'index.html',{"data":ProductModel.objects.all(),'data1':len(request.COOKIES)-1})
    response = redirect('main')
    response.set_cookie(key=pno,value=value)
    return response


def viewCart(request):
    res1 = []
    for x in request.COOKIES.keys():
        if x == 'csrftoken':
            continue
        else:
            res = ProductModel.objects.get(pno=x)
            res1.append(res)
    return render(request,'view_cart.html',{'data':res1})


def removeCart(request):
    pno = request.GET.get('cid')
    response = redirect('view_cart')
    response.delete_cookie(pno)

    return response