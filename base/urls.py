from django.urls import path
from .views import (dashboard, add_food, add_order, register, login_view, logout_view,
                    food_details, customer_page, orders_page, all_users_page,
                    delete_user, edit_user, delete_food, edit_food, about_us, home, current_user, add_admin_user)


urlpatterns = [
    path('', home, name='home'),
    path('menu', dashboard, name='menu'),
    path('food_details/<int:pk>', food_details, name='food_details'),
    path('add_food', add_food, name='add_food'),
    path('add_order/<int:user>/<str:phone>/<str:food>/<int:price>',
         add_order, name='add_order'),
    path('register', register, name='register'),
    path('login', login_view, name='login'),
    path('logout', logout_view, name='logout'),
    path('customer_page', customer_page, name='customer_page'),
    path('orders', orders_page, name='orders'),
    path('all_users', all_users_page, name='all_users'),
    path('delete_user/<int:pk>', delete_user, name='delete_user'),
    path('edit_user/<int:pk>', edit_user, name='edit_user'),
    path('delete_food/<int:pk>', delete_food, name='delete_food'),
    path('edit_food/<int:pk>', edit_food, name='edit_food'),
    path('about_us', about_us, name='about_us'),
    path('current_user', current_user, name='current_user'),
    path('add_admin', add_admin_user, name='add_admin'),
]
