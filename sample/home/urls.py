from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('signin', views.signin, name='signin'),
    path('signup', views.signup, name='signup'),
    path('contact', views.contact, name='contact'),
    path('logout', views.logout, name='logout'),
    path('adding', views.add_cart, name='adding'),
    path('removing', views.remove, name='removing'),
    path('empty', views.empty, name='empty'),
    path('cart', views.cart, name='cart'),
    path('itemadd', views.itemadd, name='itemadd'),
    path('itemremove', views.itemremove, name='itemremove'),
    path('checkout', views.checkout, name='checkout'),
    path('edit', views.edit, name='edit'),
    path('delete',views.delete, name='delete'),
    path('create', views.make, name='create'),
    path('myorders', views.myorders, name='myorders'),
    path('showorder/<int:id>', views.showorder, name='showorder'),
    path('search', views.search, name='search'),

]