from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from .models import Post, ErCode, Forum, CompanyPost, CompanyVacancy, DitailCompanyPost, DitailCompanyVacancy, DitailUserPost
from .serializers import (PostSerializer, ForumSerializer, ErCodeSerializer, CompanyVacancySerializer,
                          CompanyPostSerializer, DitailCompanyVacancySerializer,
                          DitailCompanyPostSerializer, DitailUserPostSerializer, ListCompanyPostSerializer,
                          ListForumSerializer, ListErCodeSerializer, ListPostSerializer, ListCompanyVacancySerializer)
from rest_framework.permissions import IsAuthenticated
from .permissions import IsAuthorPermission, IsAdminPermission
from apps.review.models import Like
from apps.review.serializers import CommentActionSerializer, LikeSerializer
from rest_framework.decorators import action

# Create your views here.


class PermissionMixin:
    def get_permissions(self):
        if self.action in ('list', 'retrieve'):
            permissions = [IsAuthenticated]
        elif self.action == 'create':
            permissions = [IsAuthenticated]
        else:
            permissions = [IsAuthorPermission]
        return [permission() for permission in permissions]


class PostViewSet(PermissionMixin, ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get_permissions(self):
        if self.action in ('list', 'retrieve'):
            permissions = [IsAuthenticated]
        elif self.action == 'create':
            permissions = [IsAuthenticated]
        else:
            permissions = [IsAuthorPermission]
        return [permission() for permission in permissions]

    def get_serializer_class(self):
        if self.action == 'list':
            return ListPostSerializer
        return self.serializer_class

class ErCodeViewSet(PermissionMixin, ModelViewSet):
    queryset = ErCode.objects.all()
    serializer_class = ErCodeSerializer

    def get_serializer_class(self):
        if self.action == 'list':
            return ListErCodeSerializer
        return self.serializer_class

    def get_permissions(self):
        if self.action in ('list', 'retrieve'):
            permissions = [IsAuthenticated]
        elif self.action == 'create':
            permissions = [IsAuthenticated]
        else:
            permissions = [IsAuthorPermission]
        return [permission() for permission in permissions]


class ForumViewSet(PermissionMixin, ModelViewSet):
    queryset = Forum.objects.all()
    serializer_class = ForumSerializer

    def get_serializer_class(self):
        if self.action == 'list':
            return ListForumSerializer
        return self.serializer_class

    def get_permissions(self):
        if self.action in ('list', 'retrieve'):
            permissions = [IsAuthenticated]
        elif self.action == 'create':
            permissions = [IsAuthenticated]
        else:
            permissions = [IsAuthorPermission]
        return [permission() for permission in permissions]

    @action(methods=['POST'], detail=True, permission_classes=[IsAuthenticated])
    def like(self, request, pk=None):
        forum = self.get_object()
        user = request.user
        serializer = LikeSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            try:
                like = Like.objects.get(forum=forum, author=user)
                like.delete()
                message = 'Unlike'
            except Like.DoesNotExist:
                Like.objects.create(forum=forum, author=user)
                message = 'Like'
            return Response(message, status=200)

    @action(methods=['POST'], detail=True, permission_classes=[IsAuthenticated])
    def comments(self, request, pk=None):
        video = self.get_object()
        user = request.user
        serializer = CommentActionSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(video=video, author=user)
            message = request.data
            return Response(message, status=200)


class CompanyPostViewSet(PermissionMixin, ModelViewSet):
    queryset = CompanyPost.objects.all()
    serializer_class = CompanyPostSerializer

    def get_serializer_class(self):
        if self.action == 'list':
            return ListCompanyPostSerializer
        return self.serializer_class

    def get_permissions(self):
        if self.action in ('list', 'retrieve'):
            permissions = [IsAuthenticated]
        elif self.action == 'create':
            permissions = [IsAuthenticated]
        else:
            permissions = [IsAuthorPermission]
        return [permission() for permission in permissions]


class CompanyVacancyViewSet(PermissionMixin, ModelViewSet):
    queryset = CompanyVacancy.objects.all()
    serializer_class = CompanyVacancySerializer

    def get_serializer_class(self):
        if self.action == 'list':
            return ListCompanyVacancySerializer
        return self.serializer_class

    def get_permissions(self):
        if self.action in ('list', 'retrieve'):
            permissions = [IsAuthenticated]
        elif self.action == 'create':
            permissions = [IsAuthenticated]
        else:
            permissions = [IsAuthorPermission]
        return [permission() for permission in permissions]


class DitailCompanyPostViewSet(PermissionMixin, ModelViewSet):
    queryset = DitailCompanyPost.objects.all()
    serializer_class = DitailCompanyPostSerializer

    def get_permissions(self):
        if self.action in ('list', 'retrieve'):
            permissions = [IsAuthenticated]
        elif self.action == 'create':
            permissions = [IsAuthenticated]
        else:
            permissions = [IsAuthorPermission]
        return [permission() for permission in permissions]


class DitailCompanyVacancyViewSet(PermissionMixin, ModelViewSet):
    queryset = DitailCompanyVacancy.objects.all()
    serializer_class = DitailCompanyVacancySerializer

    def get_permissions(self):
        if self.action in ('list', 'retrieve'):
            permissions = [IsAuthenticated]
        elif self.action == 'create':
            permissions = [IsAuthenticated]
        else:
            permissions = [IsAuthorPermission]
        return [permission() for permission in permissions]


class DitailUserPostViewSet(PermissionMixin, ModelViewSet):
    queryset = DitailUserPost.objects.all()
    serializer_class = DitailUserPostSerializer

    def get_permissions(self):
        if self.action in ('list', 'retrieve'):
            permissions = [IsAuthenticated]
        elif self.action == 'create':
            permissions = [IsAuthenticated]
        else:
            permissions = [IsAuthorPermission]
        return [permission() for permission in permissions]