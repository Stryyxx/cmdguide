# Generated by Django 4.2.11 on 2024-03-27 02:49

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("app", "0002_remove_quiz_creator_remove_quiz_description_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="quiz",
            name="user",
            field=models.ForeignKey(
                default=django.contrib.auth.models.User,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="quizzes",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]