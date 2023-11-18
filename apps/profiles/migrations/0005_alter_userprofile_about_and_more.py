# Generated by Django 4.2.5 on 2023-11-18 12:32

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("profiles", "0004_alter_userprofile_about_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="userprofile",
            name="about",
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name="userprofile",
            name="achievements",
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name="userprofile",
            name="age",
            field=models.PositiveIntegerField(blank=True, default=18),
        ),
        migrations.AlterField(
            model_name="userprofile",
            name="education",
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name="userprofile",
            name="languages",
            field=models.CharField(blank=True, max_length=256),
        ),
        migrations.AlterField(
            model_name="userprofile",
            name="profile_image",
            field=models.ImageField(blank=True, upload_to="profile_image/"),
        ),
        migrations.AlterField(
            model_name="userprofile",
            name="programming_languages",
            field=models.CharField(blank=True, max_length=256),
        ),
        migrations.AlterField(
            model_name="userprofile",
            name="stack",
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name="userprofile",
            name="work_experience",
            field=models.TextField(blank=True),
        ),
    ]
