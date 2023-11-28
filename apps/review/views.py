from .models import Like, Comment
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from .serializers import *
from rest_framework.permissions import AllowAny, IsAuthenticated
from .perimissions import IsAuthor
from drf_yasg.utils import swagger_auto_schema
from apps.profiles.models import UserProfile


# Create your views here.

class PermissionMixin:
    def get_permissions(self):
        if self.action == 'create':
            permissions = [IsAuthenticated]
        elif self.action in ('update', 'partial_update', 'destroy'):
            permissions = [IsAuthor]
        else:
            permissions = [AllowAny]
        return [permissions() for permissions in permissions]


class CommentView(PermissionMixin, ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


# class RecommendedVacanciesView(APIView):
#     def get(self, request, *args, **kwargs):
#         # user_skills = request.user.resume.first().skills
#         user_stack = request.user.user_profile.stack
#         user_p_languages = request.user.programming_languages
#         user_skills = user_stack.split(',')
#         # user_skills_lang = user_p_languages.split(',')
#         user_skills.append(user_p_languages.split(','))
#         user_skills_list = user_skills.split(',')
#         print('===========================')
#         print(user_skills_list)
#         recommended_vacancies = Vacancy.objects.filter(
#             reduce(lambda x, y: x | y, [Q(requirements__contains=skill) for skill in user_skills_list])
#         )
#
#         serialized_vacancies = FavoriteVacancySerializer(recommended_vacancies, many=True)
#         return Response(serialized_vacancies.data)


class LikeView(PermissionMixin, ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSeeSerializer
