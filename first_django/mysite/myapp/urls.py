from django.urls import path
from .views import index, newform_view

urlpatterns = [
    path("", index, name="index"),
    path("form", newform_view, name="forms")
]


