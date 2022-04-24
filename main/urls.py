from django.urls import path
from . import views

app_name = 'main'


# path('url-pattern', views.function, name='url-name')
urlpatterns = [
    path('index', views.index, name='index_page'),
    path('login', views.login_view, name='login_page'),
    path('logout', views.logout_view, name='logout_page'),
    path('register', views.register_view, name='register_page'),
    path('cabinet', views.cabinet_view, name='cabinet_page'),
    path('about', views.about_view, name='about_page'),
    path('account/<int:id>', views.account_detail, name='account_detail_page'),
    path('account/create', views.account_create, name='account_create_page'),
]
