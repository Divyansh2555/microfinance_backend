from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views.group import Group_viewSet

router = DefaultRouter()

router.register(r'groups', Group_viewSet, basename='group')

urlpatterns = [
    path('', include(router.urls)),
]