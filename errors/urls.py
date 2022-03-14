from django.urls import path
from errors.views import get_errors,create_errors

urlpatterns = [
    path('v/<int:version>/error/list',get_errors),
    path('v/<int:version>/error/create',create_errors),
]