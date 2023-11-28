# Generated by Django 4.2.5 on 2023-11-27 15:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompanyProfile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='company_profile', serialize=False, to=settings.AUTH_USER_MODEL)),
                ('about_company', models.TextField(blank=True)),
                ('achievements', models.TextField(blank=True)),
                ('direction', models.TextField(blank=True)),
                ('image', models.ImageField(blank=True, upload_to='company/')),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='user_profile', serialize=False, to=settings.AUTH_USER_MODEL)),
                ('languages', models.CharField(blank=True, max_length=256)),
                ('programming_languages', models.CharField(blank=True, max_length=256)),
                ('education', models.TextField(blank=True)),
                ('stack', models.CharField(blank=True, max_length=50)),
                ('about', models.TextField(blank=True)),
                ('age', models.PositiveIntegerField(blank=True, default=18)),
                ('work_experience', models.TextField(blank=True)),
                ('achievements', models.TextField(blank=True)),
                ('profile_image', models.ImageField(blank=True, upload_to='profile_image/')),
            ],
        ),
    ]
