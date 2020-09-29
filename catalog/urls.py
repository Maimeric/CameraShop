from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('registration', views.registration, name='registration'),
    path('camera/<int:camera_id>/', views.camera_page, name='camera_page'),
    path('category/<int:category_id>', views.category, name='category'),
    path('camera/<int:camera_id>/add_to_cart', views.add_to_cart, name='add_to_cart'),
    path('camera/<int:camera_id>/remove_from_card', views.remove_from_cart, name='remove_from_cart'),
    path('basket/<int:user_id>', views.basket, name='basket'),
    path('order/', views.order_create, name="order_create"),

    path('account/', include('django.contrib.auth.urls')),
]
