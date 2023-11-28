from django.db import models
from django.contrib.auth import get_user_model
# from apps.vacancy.models import Vacancy
from apps.profiles.models import UserProfile
from apps.post.models import CompanyVacancy


User = get_user_model()


class Resume(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='resume')
    first_name = models.CharField(max_length=50, verbose_name='Имя')
    last_name = models.CharField(max_length=50, verbose_name='Фамилия')
    profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='resume')
    specialization = models.CharField(max_length=45, verbose_name='Направление')
    sex_choice = [
        ('f', 'female'),
        ('m', 'male')
    ]
    sex = models.CharField(max_length=1, choices=sex_choice, verbose_name='Пол')
    city_of_residence = models.CharField(max_length=50, verbose_name='Город проживания')
    date_of_birth = models.DateField(verbose_name='Дата рождения')
    citizenship = models.CharField(max_length=20)
    profile_photo = models.ImageField(width_field=354, height_field=472, upload_to='profile', blank=True)
    education_choice = [
        ('Среднее', 'Среднее'),
        ('Среднее специальное', 'Среднее специальное'),
        ('Неоконченное высшее', 'Неоконченное высшее'),
        ('Высшее', 'Высшее'),
        ('Бакалавр', 'Бакалавр'),
        ('Магистр', 'Магистр'),
        ('Кандидат наук', 'Кандидат наук'),
        ('Доктор наук', 'Доктор наук'),
    ]
    education = models.CharField(max_length=20, choices=education_choice, verbose_name='Уровень образования')
    status = models.CharField(max_length=20, blank=True, null=True)
    expected_salary = models.CharField(max_length=5, blank=True)
    applied_vacancies = models.ManyToManyField(CompanyVacancy, related_name='applicants_resumes', blank=True)

    def __str__(self):
        return f'{self.id} - resume of: {self.user}'


class OtherResume(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='other_resume')
    profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='other_resume')
    upload_file = models.FileField(upload_to='resume_file/')
