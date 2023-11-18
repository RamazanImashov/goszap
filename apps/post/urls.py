from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import PostViewSet, ErCodeViewSet, ForumViewSet, CompanyPostViewSet, CompanyVacancyViewSet

router = DefaultRouter()
router.register('post', PostViewSet)
router.register('er_code', ErCodeViewSet)
router.register('forum', ForumViewSet)
router.register('comp_vacancy', CompanyVacancyViewSet)
router.register('comp_post', CompanyPostViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
