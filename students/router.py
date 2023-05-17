from django.urls import include, path
from rest_framework import routers
from students.views import StudentViewSet

router = routers.SimpleRouter()
router.register(r'students', StudentViewSet)
