from django.urls import path, include
from . import views
from django.conf.urls import url
from django.contrib import admin
# from django.contrib.auth.views import login, logout


# app_name = 'accounts'
urlpatterns = [
    path('', views.index, name="index"),
    path('create/', views.Create_Account.as_view(), name="create_account"),
    path('login/', views.Account_login.as_view(), name="login"),
    path('user_form/', views.UserUpdateForm.as_view(), name="update_account"),
    path('create_profile/', views.add, name="create_profile"),
    # path('profile_list/', views.lisy, name="profile_list"),
    path('profile_index/', views.indexprofile, name='profile_index'), 
    path('profile_detail/<int:pk>/', views.detail, name='profile_detail'),
    path('profile_update/<int:pk>/', views.update, name='profile_update'),
    path('profile_delete/<int:pk>/', views.delete, name='profile_delete'),
    # path('profile_index/', views.indexprofile, name='profile_index'),#一覧ページ
    path('logout/', views.LogoutView.as_view(template_name='login_app/index.html',next_page='/') , name="logout"),
    # url(r'^logout/$', logout, {'template_name': 'index.html'}, name='logout'),
]
# https://qlitre-weblog.com/django-iine-ajax-create/