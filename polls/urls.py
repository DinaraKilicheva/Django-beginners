from django.urls import path

from polls.views import homepage

urlpatterns = [
    path('', homepage, name='homepage')
]
