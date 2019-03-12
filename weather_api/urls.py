from django.urls import path, include
from .views import view_data


urlpatterns = [
    path('', view_data, name='view_data')
]

