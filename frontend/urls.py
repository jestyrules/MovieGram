from django.urls import path

from frontend import views

urlpatterns = [
    path("homepage/",views.homepage,name="homepage"),
    path("singlemov/<int:proid>/",views.singlemov,name="singlemov"),
    path("registermov/",views.registermov,name="registermov"),
    path("loginmov/",views.loginmov,name="loginmov"),
    path("registersave/",views.registersave,name="registersave"),
    path("userlogin/",views.userlogin,name="userlogin"),
    path("logout/",views.logout,name="logout"),
    path("cartsave/",views.cartsave,name="cartsave"),
    path("cartdisplay/",views.cartdisplay,name="cartdisplay"),
    path("cartdelete/<int:dataid>/",views.cartdelete,name="cartdelete"),
    path('pro/<catname>/', views.pro, name="pro"),
    path('checkout/', views.checkout, name="checkout"),
    path('checkoutsave/', views.checkoutsave, name="checkoutsave"),

]
