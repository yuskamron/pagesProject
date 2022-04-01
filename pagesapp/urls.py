from django.urls import path
from .views import HomePageView, AboutPageView, PaymentView, ContactView

urlpatterns = (
    path('about/', AboutPageView.as_view(), name='about'),
    path('payment/', PaymentView.as_view(), name='payment'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('', HomePageView.as_view(), name='home'),


)