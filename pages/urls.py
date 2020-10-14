from django.urls import path
from .views import HomePageView, AboutPageView, ContactPageView

app_name = 'pages'

urlpatterns = [
    path('', HomePageView.as_view(), name='home-view'),
    path('about/', AboutPageView.as_view(), name='about-view'),
    path('contact-us/', ContactPageView.as_view(), name='contact-view'),
]
