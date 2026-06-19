from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views.regionaloffice import RegionOfficeViewSet
from .views.headoffice import HeadOfficeViewSet
from .views.company import CompanyViewSet
from .views.areaoffice import AreaOfficeViewSet
from .views.branchoffice import BranchViewSet


router = DefaultRouter()
router.register(r'branches', BranchViewSet, basename='branch')
router.register(r'headoffices', HeadOfficeViewSet, basename='headoffice')
router.register(r'companies', CompanyViewSet, basename='company')
router.register(r'areas', AreaOfficeViewSet, basename='area')
router.register(r'regionaloffices', RegionOfficeViewSet, basename='regionaloffice')


urlpatterns = [
    path('', include(router.urls)),
]