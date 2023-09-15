from django.urls import path
from . import views

urlpatterns = [
    path('home/',views.home,name='home'),
    path('help/',views.help,name='help'),
    path('welcome/',views.welcome,name='welcome'),
    path('contact/',views.contact,name='contact'),
    path('emp/',views.emp,name='emp'),
    path('pet/',views.pet,name='pet')
]



