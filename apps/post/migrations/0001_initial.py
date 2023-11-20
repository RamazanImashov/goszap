# Generated by Django 4.2.5 on 2023-11-20 14:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('type_post', models.CharField(choices=[('Work', 'Work'), ('Teams', 'Teams')], max_length=5)),
                ('description', models.TextField()),
                ('celery', models.PositiveIntegerField()),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='profiles.userprofile')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Forum',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('file', models.FileField(upload_to='forum_file/')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='forum', to='profiles.userprofile')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='forum', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ErCode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('file', models.FileField(upload_to='ercode_file/')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ercode', to='profiles.userprofile')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ercode', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CompanyVacancy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('position', models.CharField(max_length=50)),
                ('celery', models.PositiveIntegerField()),
                ('type_work', models.CharField(choices=[('Work', 'Work'), ('Internship', 'Internship')], max_length=10)),
                ('type_employment', models.CharField(choices=[('Office', 'Office'), ('Online', 'Online')], max_length=6)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='company_vacancy', to='profiles.companyprofile')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='company_vacancy', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CompanyPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('type_post', models.CharField(choices=[('Work', 'Work'), ('Teams', 'Teams')], max_length=5)),
                ('description', models.TextField()),
                ('celery', models.PositiveIntegerField()),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='company_posts', to='profiles.companyprofile')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='company_posts', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
