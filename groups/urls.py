from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views.group import Group_viewSet
from .views.group_members import Group_Members_ViewSet

router = DefaultRouter()

router.register(r'groups', Group_viewSet, basename='group')
router.register(r'group_members', Group_Members_ViewSet, basename='group-member')

urlpatterns = [
    path('', include(router.urls)),
]