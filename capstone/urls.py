from django.urls import path

from . import views

urlpatterns = [
    # path('', views.index, name='index'),
    path('signup', views.signup, name='signup'),
    path('', views.login_view, name='login'),
    path('data', views.get_data, name='data'),
    path('testf', views.testfunction, name='testf'),
    path('transactions', views.transactions, name='transactions'),
    path('index',views.index,name='index'),
    path('logout',views.logout_view,name='logout'),

]
