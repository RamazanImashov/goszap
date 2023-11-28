from rest_framework.serializers import ValidationError, ReadOnlyField
from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Resume, OtherResume
from django.core.validators import MinValueValidator
from datetime import date, timedelta
from .utils_resume import send_resume_data
from apps.post.models import CompanyVacancy
# from apps.vacancy.models import Vacancy
# from .tasks import send_activation_code_celery

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email']


class ResumeSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    profile = ReadOnlyField(source='profile.id')
    email = serializers.ReadOnlyField(source='user.email')
    date_of_birth = serializers.DateField(format='%d.%m.%Y', input_formats=['%d.%m.%Y'],
                                          validators=[
                                              MinValueValidator(
                                                limit_value=date.today() - timedelta(days=14*365),
                                                message='Вы должны быть старше 14 лет')
                                            ]
                                          )

    class Meta:
        model = Resume
        fields = '__all__'
    date_of_birth = serializers.DateField(format='%d.%m.%Y', input_formats=['%d.%m.%Y'])
    applied_vacancies = serializers.PrimaryKeyRelatedField(
        queryset=CompanyVacancy.objects.all(),
        many=True,
        write_only=True
    )

    class Meta:
        model = Resume
        exclude = ['profile_photo']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        user_data = representation.pop('user')
        representation.update(user_data)
        return representation

    def validate_sex(self, value):
        allowed_sex = ['f', 'm']

        if value not in allowed_sex:
            raise ValidationError(
                f'Недопустимое значение статуса. Допустимые значения: {", ".join(allowed_sex)}')

        return value

    def validate_education(self, value):
        allowed_education = ['Среднее', 'Среднее специальное', 'Неоконченное высшее',
                            'Высшее', 'Бакалавр', 'Магистр', 'Кандидат наук', 'Доктор наук']

        if value not in allowed_education:
            raise ValidationError(
                f'Недопустимое значение статуса. Допустимые значения: {", ".join(allowed_education)}')

        return value

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        email = user_data.email
        user = User.objects.filter(email=email).first()
        profile = user.user_profile
        if user:
            resume = Resume.objects.create(user=user, profile=profile, **validated_data)
            return resume
        else:
            raise serializers.ValidationError('Пользователь с указанным email не найден')


class OtherResumeSerializer(serializers.ModelSerializer):
    user = ReadOnlyField(source='user.email')
    profile = ReadOnlyField(source='profile.id')

    class Meta:
        model = OtherResume
        fields = "__all__"

    def create(self, validated_data):
        user = self.context['request'].user
        if user.type_user == 'Human':
            profile = user.profiler
        else:
            profile = user.profile
        profile = user.user_profile
        project = OtherResume.objects.create(user=user, profile=profile, **validated_data)
        return project


class OtherResumeSeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = OtherResume
        fields = "__all__"
