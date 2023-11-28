from rest_framework.views import APIView
from rest_framework.viewsets import generics, ModelViewSet
from .serializers import ResumeSerializer, OtherResumeSerializer
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .permissions import IsAuthorPermission, IsAdminPermission
from .models import Resume, OtherResume
from drf_yasg.utils import swagger_auto_schema


User = get_user_model()


class ResumeView(APIView):
    permission_classes = [IsAuthenticated, IsAuthorPermission]

    # def perform_create(self, serializer):
    #     if self.request.user.is_authenticated:
    #         serializer.save(user=self.request.user)
    #     else:
    #         raise ValidationError('Пользователь не аутентифицирован')

    @swagger_auto_schema(request_body=ResumeSerializer())
    def post(self, request):
        serializer = ResumeSerializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save(user=request.user)
        return Response('Ваше резюме успешно размещено на сайте!')

    def get(self, request):
        users_resume = Resume.objects.filter(user=request.user)
        serializer = ResumeSerializer(users_resume, many=True)
        return Response(serializer.data)


class ResumeDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Resume.objects.all()
    serializer_class = ResumeSerializer
    permission_classes = [IsAuthenticated, IsAdminPermission]


class OtherResumeViewSet(ModelViewSet):
    queryset = OtherResume.objects.all()
    serializer_class = OtherResumeSerializer
    permission_classes = IsAuthorPermission

    def get_permissions(self):
        if self.action in ('list', 'retrieve'):
            permissions = [IsAuthenticated]
        elif self.action == 'create':
            permissions = [IsAuthenticated]
        else:
            permissions = [IsAuthorPermission, IsAdminPermission]
        return [permission() for permission in permissions]
