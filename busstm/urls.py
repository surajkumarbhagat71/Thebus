from django.urls import path
from .import views

urlpatterns=[
    path('',views.home,name="home"),
    path('main/usersignup/',views.user_signup,name="user_signup"),
    path('main/onersignup/',views.oner_signup,name="oner_signup"),
    path('main/userlogin',views.user_login,name="user_login"),
    path('logout',views.logout,name="logout"),
    path('main/onerlogin',views.oner_login,name="oner_login"),
    path('oner_logout', views.oner_logout, name="oner_logout"),
    path('bus_oner/dashaboard',views.dashaboard,name="dashaboard"),
    path('bus_oner/add_bus',views.add_bus,name="add_bus"),
    path('bus_oner/profile',views.oner_profile,name="oner_profile"),
    path('user/my_booking',views.user_booking,name="user_booking"),
    path('user/profile',views.user_profile,name="user_profile"),

]