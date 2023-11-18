from rest_framework.viewsets import ModelViewSet
from .models import Post, ErCode, Forum, CompanyPost, CompanyVacancy
from .serializers import PostSerializer, ForumSerializer, ErCodeSerializer,CompanyVacancySerializer, CompanyPostSerializer
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from .permissions import IsAuthorPermission

# Create your views here.


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get_permissions(self):
        if self.action in ('list', 'retrieve'):
            permissions = [IsAuthenticated]
        elif self.action == 'create':
            permissions = [IsAuthenticated]
        else:
            permissions = [IsAuthorPermission, IsAdminUser]
        return [permission() for permission in permissions]


class ErCodeViewSet(ModelViewSet):
    queryset = ErCode.objects.all()
    serializer_class = ErCodeSerializer

    def get_permissions(self):
        if self.action in ('list', 'retrieve'):
            permissions = [IsAuthenticated]
        elif self.action == 'create':
            permissions = [IsAuthenticated]
        else:
            permissions = [IsAuthorPermission, IsAdminUser]
        return [permission() for permission in permissions]


class ForumViewSet(ModelViewSet):
    queryset = Forum.objects.all()
    serializer_class = ForumSerializer

    def get_permissions(self):
        if self.action in ('list', 'retrieve'):
            permissions = [IsAuthenticated]
        elif self.action == 'create':
            permissions = [IsAuthenticated]
        else:
            permissions = [IsAuthorPermission, IsAdminUser]
        return [permission() for permission in permissions]


class CompanyPostViewSet(ModelViewSet):
    queryset = CompanyPost.objects.all()
    serializer_class = CompanyPostSerializer

    def get_permissions(self):
        if self.action in ('list', 'retrieve'):
            permissions = [IsAuthenticated]
        elif self.action == 'create':
            permissions = [IsAuthenticated]
        else:
            permissions = [IsAuthorPermission, IsAdminUser]
        return [permission() for permission in permissions]


class CompanyVacancyViewSet(ModelViewSet):
    queryset = CompanyVacancy.objects.all()
    serializer_class = CompanyVacancySerializer

    def get_permissions(self):
        if self.action in ('list', 'retrieve'):
            permissions = [IsAuthenticated]
        elif self.action == 'create':
            permissions = [IsAuthenticated]
        else:
            permissions = [IsAuthorPermission, IsAdminUser]
        return [permission() for permission in permissions]