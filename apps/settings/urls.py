from django.urls import path
from apps.settings.views import AboutView, ContactView, HelloView


urlpatterns = [    
    path('hello/', HelloView.as_view()),
    path('about/', AboutView.as_view()),
    path('contact/', ContactView.as_view()),
    
]

