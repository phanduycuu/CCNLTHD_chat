from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FileViewSet

router = DefaultRouter()
router.register(r'', FileViewSet)  # Tạo API cho File

urlpatterns = [
    path('', include(router.urls)),  # Gộp tất cả API vào
]