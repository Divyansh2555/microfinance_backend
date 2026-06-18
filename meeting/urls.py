from django.urls import path, include
from rest_framework import routers
from .views.meeting import MeetingViewSet
from .views.meeting_attendance import MeetingAttendanceViewSet
from .views.collections import CollectionViewSet

router = routers.DefaultRouter()

router.register(r'meetings', MeetingViewSet, basename='meeting')
router.register(r'meeting-attendance', MeetingAttendanceViewSet, basename='meeting-attendance')
router.register(r'collections', CollectionViewSet, basename='collection')

urlpatterns = [
    path('', include(router.urls)),
]