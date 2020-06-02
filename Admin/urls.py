from django.urls import path,re_path,include
from . import views

urlpatterns = [
    path('', views.admin_page, name='admin_page'),
    re_path(r'admin1/games/up_del/deleted/', views.delete_func, name = 'deleted'),
    re_path(r'admin1/games/up_del/updated/', views.update_func, name = 'updated'),
    re_path(r'admin1/games/up_del/', views.update_delete, name = 'updel'),
    re_path(r'admin1/import/', views.ImportCSV, name='ImportCSV'),
    re_path(r'admin1/games/', views.disp_games, name='disp_games'),
    re_path(r'admin1/', views.AdminLogin, name='AdminLogin'),    
]