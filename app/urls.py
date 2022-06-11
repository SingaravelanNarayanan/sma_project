
from django.urls import path,include
from app import views

urlpatterns = [
    path('',views.home,name='home'),
    path('signup/',views.sign_up,name='signup'),
    path('signin/',views.signin,name='signin'),
    path('logout/',views.logout,name='logout'),
    path('user_bio',views.user_bio,name='user_bio')
    
]
