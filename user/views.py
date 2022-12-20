from django.http import HttpResponse
from django.shortcuts import render

from home.models import UserProfile, Setting
from product.models import Category


# Create your views here.
def index(request):
    category = Category.objects.all()
    current_user = request.user
    setting = Setting.objects.get(pk=1)
    profile = UserProfile.objects.get(user_id=current_user.id)
    context = {'category': category, 'profile': profile, 'setting': setting, }
    return render(request, 'user_profile.html', context)