from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # This will match the empty path within the 'myapp/' prefix
]
