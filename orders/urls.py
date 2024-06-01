from django.urls import path
from . import views

app_name = 'orders'

urlpatterns = [
    path("", views.OrderPlaceView.as_view(), name="order"),
]
