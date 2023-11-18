from rest_framework.serializers import ModelSerializer, ReadOnlyField
from .models import Post, Forum, ErCode, CompanyVacancy, CompanyPost
from django.contrib.auth import get_user_model

User = get_user_model()


class PostSerializer(ModelSerializer):
    user = ReadOnlyField(source='user.email')
    profile = ReadOnlyField()

    class Meta:
        model = Post
        fields = "__all__"

    def create(self, validated_data):
        user = self.context['request'].user
        profile = self.context['request'].user.profiler
        post = Post.objects.create(user=user, profile=profile, **validated_data)
        return post


class PostViewSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"


class ForumSerializer(ModelSerializer):
    user = ReadOnlyField(source='user.email')
    profile = ReadOnlyField()

    class Meta:
        model = Forum
        fields = "__all__"

    def create(self, validated_data):
        user = self.context['request'].user
        profile = self.context['request'].user.profiler
        forum = Forum.objects.create(user=user, profile=profile, **validated_data)
        return forum


class ForumViewSerializer(ModelSerializer):
    class Meta:
        model = Forum
        fields = "__all__"


class ErCodeSerializer(ModelSerializer):
    user = ReadOnlyField(source='user.email')
    profile = ReadOnlyField()

    class Meta:
        model = ErCode
        fields = "__all__"

    def create(self, validated_data):
        user = self.context['request'].user
        profile = self.context['request'].user.profiler
        ercode = ErCode.objects.create(user=user, profile=profile, **validated_data)
        return ercode


class ErCodeViewSerializer(ModelSerializer):
    class Meta:
        model = ErCode
        fields = "__all__"


class CompanyPostSerializer(ModelSerializer):
    user = ReadOnlyField(source='user.email')
    profile = ReadOnlyField()

    class Meta:
        model = CompanyPost
        fields = "__all__"

    def create(self, validated_data):
        user = self.context['request'].user
        profile = self.context['request'].user.profiler
        comppost = CompanyPost.objects.create(user=user, profile=profile, **validated_data)
        return comppost


class CompanyPostSerializerView(ModelSerializer):
    class Meta:
        model = CompanyPost
        fields = "__all__"


class CompanyVacancySerializer(ModelSerializer):
    user = ReadOnlyField(source='user.email')
    profile = ReadOnlyField()

    class Meta:
        model = CompanyVacancy
        fields = "__all__"

    def create(self, validated_data):
        user = self.context['request'].user
        profile = self.context['request'].user.profiler
        compvac = CompanyVacancy.objects.create(user=user, profile=profile, **validated_data)
        return compvac


class CompanyVacancySerializerView(ModelSerializer):
    class Meta:
        model = CompanyVacancy
        fields = "__all__"
