from django.urls import path
from errors.views import get_errors

urlpatterns = [
    path('v/<int:version>/error/list',get_errors),
]