from core.views import BaseViewSet
from rest_framework import viewsets, generics, status, filters
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from students.models import Student
from students.serializers import StudentSerializer
from core.services import send_data_to_kafka
from core.decorators import rate_limit


class StudentPagination(PageNumberPagination):
    page_size = 20


class StudentViewSet(BaseViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    pagination_class = StudentPagination
    permission_classes = [IsAuthenticated, ]

    @rate_limit(rate=1, period=60)
    def create(self, request):
        data = request.data
        if not request.user.is_authenticated:
            return Response({"error": "The user is anonymous"}, status=status.HTTP_401_UNAUTHORIZED)

        try:
            serializer_class = self.get_serializer_class()
            serializer = serializer_class(data=data)
            if serializer.is_valid():
                # Instead of saving the object, pass it to kafka queue function
                send_data_to_kafka(serializer.validated_data)
                return Response(serializer.validated_data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


    def update(self, request, pk=None):
        return Response(status=status.HTTP_403_FORBIDDEN)

    def destroy(self, request, pk=None):
        student = self.get_object()
        if not request.user.is_authenticated:
            return Response({"error": "User not authorized"}, status=status.HTTP_401_UNAUTHORIZED)
        student.delete()
        return Response({'success': True}, status=status.HTTP_200_OK)
