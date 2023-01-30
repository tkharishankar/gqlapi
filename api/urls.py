from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
)

from . import views

urlpatterns = [
    path('', views.getRoutes),
    path('projects/', views.getProjects),
    path('users/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
]
