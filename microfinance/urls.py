from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('forms/', include('customers.urls')),
    path('org/', include('organizations.urls')),
    path('center/', include('centers.urls')),
    path('group/', include('groups.urls')),


]