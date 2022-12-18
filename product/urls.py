from django.urls import path

from . import views

urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    path('addcomment/<int:id>', views.addcomment, name='addcomment'),
]