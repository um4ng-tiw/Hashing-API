from django.urls import path
from . import views

urlpatterns = [
    path('', views.hashOverview, name="hash-overview"),
    path('create/', views.createHash, name="create-hash")
]