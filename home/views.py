from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from home.models import Setting, ContactFormu, ContactFormMessage
from product.models import Product, Category, Images, Comment


# Create your views here.
def index(request):
    setting = Setting.objects.get(pk=1)
    sliderdata = Product.objects.all()[:4]
    category = Category.objects.all()
    randomproducts = Product.objects.all().order_by('?')[:12]#4 satir 3 sutun urun
    context = {'setting': setting, 'category': category, 'page': 'home', 'sliderdata': sliderdata, 'randomproducts': randomproducts}
    return render(request, 'index.html', context)

def hakkimizda(request):
    setting = Setting.objects.get(pk=1)
    category = Category.objects.all()
    context = {'setting': setting, 'category': category}
    return render(request, 'hakkimizda.html', context)

def referanslar(request):
    setting = Setting.objects.get(pk=1)
    category = Category.objects.all()
    context = {'setting': setting, 'category': category}
    return render(request, 'referanslarimiz.html', context)

def iletisim(request):

    if request.method == 'POST':
        form = ContactFormu(request.POST)
        if form.is_valid():
            data = ContactFormMessage()
            data.name = form.cleaned_data['name']
            data.email = form.cleaned_data['email']
            data.subject = form.cleaned_data['subject']
            data.message = form.cleaned_data['message']
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()
            messages.success(request, "Mesajınız Gönderilmiştir")
            return HttpResponseRedirect ('/iletisim')

    setting = Setting.objects.get(pk=1)
    category = Category.objects.all()
    form = ContactFormu()
    context = {'setting': setting, 'form': form, 'category': category}
    return render(request, 'iletisim.html', context)

def category_product(request,id,slug):
    category = Category.objects.all()
    categorydata = Category.objects.get(pk=id)
    products = Product.objects.filter(category_id=id)
    context = {'products': products, 'category': category, 'categorydata': categorydata}
    return render(request, 'products.html', context)

def product_detail(request,id,slug):
    category = Category.objects.all()
    product = Product.objects.get(pk=id)
    images = Images.objects.filter(product_id=id)
    comments = Comment.objects.filter(product_id=id, status='True')
    context = {'product': product, 'category': category, 'images': images, 'comments': comments}
    return render(request, 'product_detail.html', context)
