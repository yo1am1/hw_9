from django.urls import path
from . import views

urlpatterns = [
    path("", views.add_number, name="input_number"),
    path("message/", views.message, name="send_message"),
]
