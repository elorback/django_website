from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('registration/',views.registerUser, name='registration'),
    path('login/',views.login_method,name='login_method'),
    path('logout/',views.user_logout,name='user_logout'),
    path('add_item/', views.add_item, name='add_item'),
    path('user_page/', views.user_page, name='user_page'),
    path('user_items',views.user_items,name='user_items'),
    path('multiple_posts',views.multiple_posts,name='multiple_posts'),
    path('delete_profile',views.delete_profile,name='delete_profile'),
    path('user_settings',views.user_settings,name='user_settings'),

  
]
