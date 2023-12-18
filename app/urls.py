from django.urls import path, include
from .views import Appview
urlpatterns = [
    path('', Appview.as_view(), name='app'),
]