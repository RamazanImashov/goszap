# Generated by Django 4.2.5 on 2023-11-17 21:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("vacancy", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("profiles", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Resume",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "specialization",
                    models.CharField(
                        choices=[
                            ("Front-end разработка", "Front-end разработка"),
                            ("Back-end разработка", "Back-end разработка"),
                            ("Мобильная разработка", "Мобильная разработка"),
                            ("Data science", "Data science"),
                            ("UX/UI дизайн", "UX/UI дизайн"),
                        ],
                        max_length=45,
                    ),
                ),
                (
                    "sex",
                    models.CharField(
                        choices=[("f", "female"), ("m", "male")], max_length=1
                    ),
                ),
                (
                    "city_of_residence",
                    models.CharField(max_length=15, verbose_name="Город проживания"),
                ),
                ("date_of_birth", models.DateField(verbose_name="Дата рождения")),
                (
                    "phone_number",
                    models.CharField(max_length=13, verbose_name="Номер телефона"),
                ),
                ("citizenship", models.CharField(max_length=20)),
                (
                    "profile_photo",
                    models.ImageField(
                        blank=True,
                        height_field=472,
                        upload_to="profile",
                        width_field=354,
                    ),
                ),
                ("skills", models.TextField(verbose_name="Навыки, скиллы")),
                (
                    "cover_letter",
                    models.TextField(verbose_name="Сопроводительное письмо"),
                ),
                (
                    "education",
                    models.CharField(
                        choices=[
                            ("Среднее", "Среднее"),
                            ("Среднее специальное", "Среднее специальное"),
                            ("Неоконченное высшее", "Неоконченное высшее"),
                            ("Высшее", "Высшее"),
                            ("Бакалавр", "Бакалавр"),
                            ("Магистр", "Магистр"),
                            ("Кандидат наук", "Кандидат наук"),
                            ("Доктор наук", "Доктор наук"),
                        ],
                        max_length=20,
                        verbose_name="Уровень образования",
                    ),
                ),
                ("expected_salary", models.CharField(blank=True, max_length=5)),
                (
                    "status",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("viewed", "Просмотрено"),
                            ("rejected", "Отказано"),
                            ("contact_soon", "Кандидатура подходит, скоро свяжемся"),
                        ],
                        max_length=20,
                        null=True,
                    ),
                ),
                (
                    "applied_vacancies",
                    models.ManyToManyField(
                        blank=True,
                        related_name="applicants_resumes",
                        to="vacancy.vacancy",
                    ),
                ),
                (
                    "profile",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="resume",
                        to="profiles.userprofile",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="resume",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="OtherResume",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("upload_file", models.FileField(upload_to="resume_file/")),
                (
                    "profile",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="other_resume",
                        to="profiles.userprofile",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="other_resume",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
