from rest_framework.viewsets import ModelViewSet
from .models import Project
from .serializers import ProjectSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .permissions import IsAuthorPermission

# Create your views here.


class ProjectViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    def get_permissions(self):
        if self.action in ('list', 'retrieve'):
            permissions = [IsAuthenticated]
        else:
            permissions = [IsAuthorPermission, IsAdminUser]
        return [permission() for permission in permissions]