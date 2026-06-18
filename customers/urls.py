from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views.customer_view import CustomerViewSet
from .views.document_view import DocumentViewSet
from .views.address_view import AddressViewSet
from .views.kyc_view import KycViewSet


router = DefaultRouter()

router.register(r'customers', CustomerViewSet, basename='customer')
router.register(r'documents', DocumentViewSet, basename='document')
router.register(r'addresses', AddressViewSet, basename='address')
router.register(r'kyc', KycViewSet, basename='kyc')


urlpatterns = [
    path('', include(router.urls)),
]