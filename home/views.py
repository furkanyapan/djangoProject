from django.contrib import messages
from django.contrib.auth import logout, authenticate, login
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
    setting = Setting.objects.get(pk=1)
    category = Category.objects.all()
    categorydata = Category.objects.get(pk=id)
    products = Product.objects.filter(category_id=id)
    context = {'products': products, 'category': category, 'categorydata': categorydata, 'setting': setting,}
    return render(request, 'products.html', context)

def product_detail(request,id,slug):
    setting = Setting.objects.get(pk=1)
    category = Category.objects.all()
    product = Product.objects.get(pk=id)
    images = Images.objects.filter(product_id=id)
    comments = Comment.objects.filter(product_id=id, status='True')
    context = {'product': product, 'category': category, 'images': images, 'comments': comments, 'setting': setting,}
    return render(request, 'product_detail.html', context)

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/')
        else:
            messages.error(request, "Kullanıcı adı veya şifre yanlış")
            return HttpResponseRedirect('/login')
    category = Category.objects.all()
    setting = Setting.objects.get(pk=1)
    context = {'category': category, 'setting': setting, }
    return render(request, 'login.html', context)