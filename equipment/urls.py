from django.urls import path
from . import views


urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('register/', views.register, name='register'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('index/', views.index, name='index'),
    path('equipment-list/', views.equipment_list, name='equipment_list'),
    path('rental-list/', views.rental_list, name='rental_list'),
    path('maintenance-list/', views.maintenance_list, name='maintenance_list'),
]
