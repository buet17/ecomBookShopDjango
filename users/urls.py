from django.urls import path
from users import views


#create urls here
urlpatterns = [
    path('', views.index, name="home"),
    path('about-us/', views.about, name="about_us"),
    path('my-profile/', views.my_profile, name="my_profile"),
    path('services/', views.services, name="services"),
    path('customers/shop-registration/', views.registration, name="registration"),
    path('shop-login/', views.shop_login, name="shop_login")
]
