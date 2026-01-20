from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from logs.views import LogStreamViewSet

router = DefaultRouter()
router.register(r'logs', LogStreamViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]