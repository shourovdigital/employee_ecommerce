
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('employee_apps.urls')),
    path('inv/', include('inventory.urls')),
]
