from django.urls import path, include
from .views.login import LoginView
from .views.signup import SignupView
from rest_framework.routers import DefaultRouter
from .views.profile import UserProfileViewSet
from .views.role import RoleViewSet

router = DefaultRouter()

router.register(r'profiles', UserProfileViewSet, basename='profile')
router.register(r'roles', RoleViewSet, basename='role')

urlpatterns = [
    # AUTH APIs
    path('signup/', SignupView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),

    # VIEWSETS APIs
    path('', include(router.urls)),
]