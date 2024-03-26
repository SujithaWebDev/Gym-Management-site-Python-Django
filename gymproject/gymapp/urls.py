from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('signup/',views.signup,name='signup'),
    path('login/',views.login,name='login'),
    path('create/',views.create,name='create'),
    path('update/<int:item_id>/',views.update,name='update'),
    path('delete/<int:item_id>/',views.delete,name='delete'),
    path('view/',views.view,name='view'),

]