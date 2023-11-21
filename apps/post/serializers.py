from rest_framework.serializers import ModelSerializer, ReadOnlyField
from .models import Post, Forum, ErCode, CompanyVacancy, CompanyPost
from django.contrib.auth import get_user_model
from apps.review.serializers import CommentSerializer, LikeSeeSerializer

User = get_user_model()


class PostSerializer(ModelSerializer):
    user = ReadOnlyField(source='user.email')
    profile = ReadOnlyField(source='profile.id')

    class Meta:
        model = Post
        fields = "__all__"

    def create(self, validated_data):
        user = self.context['request'].user
        profile = user.user_profile
        post = Post.objects.create(user=user, profile=profile, **validated_data)
        return post


class PostViewSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"


class ForumSerializer(ModelSerializer):
    user = ReadOnlyField(source='user.email')
    profile = ReadOnlyField(source='profile.id')

    class Meta:
        model = Forum
        fields = "__all__"

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['comments'] = CommentSerializer(instance.comments.all(), many=True).data
        rep['like'] = instance.likes.all().count()
        return rep

    def create(self, validated_data):
        user = self.context['request'].user
        profile = user.user_profile
        forum = Forum.objects.create(user=user, profile=profile, **validated_data)
        return forum


class ForumViewSerializer(ModelSerializer):
    class Meta:
        model = Forum
        fields = "__all__"


class ErCodeSerializer(ModelSerializer):
    user = ReadOnlyField(source='user.email')
    profile = ReadOnlyField(source='profile.id')

    class Meta:
        model = ErCode
        fields = "__all__"

    def create(self, validated_data):
        user = self.context['request'].user
        profile = user.user_profile
        ercode = ErCode.objects.create(user=user, profile=profile, **validated_data)
        return ercode


class ErCodeViewSerializer(ModelSerializer):
    class Meta:
        model = ErCode
        fields = "__all__"


class CompanyPostSerializer(ModelSerializer):
    user = ReadOnlyField(source='user.email')
    profile = ReadOnlyField(source='profile.id')

    class Meta:
        model = CompanyPost
        fields = "__all__"

    def create(self, validated_data):
        user = self.context['request'].user
        profile = user.company_profile
        comppost = CompanyPost.objects.create(user=user, profile=profile, **validated_data)
        return comppost


class CompanyPostSerializerView(ModelSerializer):
    class Meta:
        model = CompanyPost
        fields = "__all__"


class CompanyVacancySerializer(ModelSerializer):
    user = ReadOnlyField(source='user.email')
    profile = ReadOnlyField(source='profile.id')

    class Meta:
        model = CompanyVacancy
        fields = "__all__"

    def create(self, validated_data):
        user = self.context['request'].user
        profile = user.company_profile
        compvac = CompanyVacancy.objects.create(user=user, profile=profile, **validated_data)
        return compvac


class CompanyVacancySerializerView(ModelSerializer):
    class Meta:
        model = CompanyVacancy
        fields = "__all__"
