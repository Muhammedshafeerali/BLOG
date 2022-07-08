
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('newpost/',views.newPost,name="New Post"),
    path('viewpost/',views.viewPost,name="View Post"),
    path('getcategory/',views.getcategory,name="getcategory")
]
