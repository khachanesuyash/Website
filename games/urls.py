from django.urls import path,re_path,include
from . import views

urlpatterns = [

    path('', views.home, name='home'),  # default homepage
    re_path(r'plot5/', views.home_plot5, name='home_plot5'),
    re_path(r'plot4/', views.home_plot4, name='home_plot4'),
    re_path(r'plot3/', views.home_plot3, name='home_plot3'),
    re_path(r'plot2/', views.home_plot2, name='home_plot2'),
    re_path(r'plot/', views.home_plot, name='home_plot'),
    re_path(r'myadmin/', include('Admin.urls')),
    path('games/', views.index, name='index'),
    path('searches/', views.search, name='search'),
    re_path(r'searches/', views.redirect, name='search'),
    # path('games/searches/', views.search, name = 'search'),
    path('games/result/', views.result, name='result'),
    # path('games/clicked/searches/', views.redirect, name = 'search'),
    path('graph/', views.plot, name='graph'),

]