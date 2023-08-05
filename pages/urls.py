from django.urls import path

from pages.views import home, signup, signin, signout, cart, contact

urlpatterns = [
    path('', home, name='home'),
    path('signup/', signup, name='signup'),
    path('logout/', signout, name='logout'),
    path('login/', signin, name='login'),
    path('cart/', cart, name='cart'),
    path('contact/', contact, name='contact'),
]