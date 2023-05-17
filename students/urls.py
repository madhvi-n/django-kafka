from django.urls import path, include
from .router import router

urlpatterns = [
    path('api/v1/', include(router.urls)),
]
