from rest_framework.serializers import ValidationError, ReadOnlyField
from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Resume, OtherResume
from .utils_resume import send_resume_data
from apps.vacancy.models import Vacancy
# from .tasks import send_activation_code_celery


User = get_user_model()  # возвращает активную модельку юзера


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email']


class ResumeSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    email = serializers.ReadOnlyField(source='user.email')
    date_of_birth = serializers.DateField(format='%d.%m.%Y', input_formats=['%d.%m.%Y'])
    applied_vacancies = serializers.PrimaryKeyRelatedField(
        queryset=Vacancy.objects.all(),
        many=True,
        write_only=True
    )

    class Meta:
        model = Resume
        exclude = ['profile_photo']

    def validate_phone_number(self, attrs):
        phone_number = attrs
        if not phone_number.startswith('+996') or not phone_number[4:].isdigit():
            raise ValidationError('Номер должен начинаться с +996 и содержать только цифры')
        elif len(phone_number) != 13:
            raise ValidationError('Указано неправильное количество цифр, проверьте номер')
        return attrs

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        user_data = representation.pop('user')
        representation.update(user_data)
        return representation

    def validate_specialization(self, value):
        allowed_specializations = ['Front-end разработка', 'Back-end разработка',
                                   'Мобильная разработка', 'Data science', 'UX/UI дизайн']

        if value not in allowed_specializations:
            raise ValidationError(
                f'Недопустимое значение направления. Допустимые значения: {", ".join(allowed_specializations)}')

        user = self.context.get('request').user if self.context.get('request') else None
        if user:
            existing_resume = Resume.objects.filter(user=user, specialization=value).exclude(
                id=self.instance.id if self.instance else None).first()
            if existing_resume:
                raise serializers.ValidationError('Вы уже создали резюме с такой специализацией')
        return value

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
        applied_vacancies = validated_data.pop('applied_vacancies', [])  # Извлекаем applied_vacancies из данных
        user_data = validated_data.pop('user')
        email = user_data.email
        user = User.objects.filter(email=email).first()
        if user:
            resume = Resume.objects.create(user=user, **validated_data)
            resume.applied_vacancies.set(applied_vacancies)
            send_resume_data(email, resume)
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
        profile = user.user_profile
        project = OtherResume.objects.create(user=user, profile=profile, **validated_data)
        return project


class OtherResumeSeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = OtherResume
        fields = "__all__"