from django.urls import path
from . import views

app_name = 'jimyou'
urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    path('home-page/', views.HomeView.as_view(), name="home-page"),
    path('services/', views.profile, name="services"),
    path('about-us/', views.AboutusView.as_view(), name="about-us"),
    path('about-me/', views.AboutmeView.as_view(), name="about-me"),
    path('contacts/', views.CreateView.as_view(), name="contacts"),
    path('hm/', views.HmView.as_view(), name="hm"),
    # path('login-index/', views.loginView.as_view(), name="login-index"),
    path('index-account/', views.loginView.as_view(), name="index-account"),
    path('post_list/', views.good_in, name="post_list"),
    path('post_create/<int:pk>/', views.post_in.as_view(), name="post_create"),
    path('post_input/', views.post_in_input.as_view(), name="post_input"),
    path('good_detail/<int:pk>/', views.good_detail, name="good_detail"),
    path('good_good/<int:pk>/', views.good_test_in, name="good_good"),
    path('good_comment/<int:pk>/', views.goodcomment.as_view(), name="good_comment"),
    path('endcontents/', views.ContentsView.as_view(), name="endcontents"),
    # path('postsave/', views.postsave, name='postsave'),
    # path('comment/<int:pk>/', views.profileDetail.as_view(), name='comment'),
    
]
