from rest_framework.serializers import ModelSerializer, ReadOnlyField
from .models import Project
from django.contrib.auth import get_user_model


User = get_user_model()


class ProjectSerializer(ModelSerializer):
    user = ReadOnlyField(source='user.email')
    profile = ReadOnlyField()

    class Meta:
        model = Project
        fields = "__all__"

    def create(self, validated_data):
        user = self.context['request'].user
        if User.objects.filter(type_user='Human'):
            profile = self.context['request'].user.profiler
        else:
            profile = self.context['request'].user.profiles
        project = Project.objects.create(user=user, profile=profile, **validated_data)
        return project


class ProjectViewSerializer(ModelSerializer):
    class Meta:
        model = Project
        fields = "__all__"