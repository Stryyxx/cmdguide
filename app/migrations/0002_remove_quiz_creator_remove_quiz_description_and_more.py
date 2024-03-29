# Generated by Django 4.2.11 on 2024-03-26 01:01

import builtins
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("app", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="quiz",
            name="creator",
        ),
        migrations.RemoveField(
            model_name="quiz",
            name="description",
        ),
        migrations.RemoveField(
            model_name="quiz",
            name="title",
        ),
        migrations.AddField(
            model_name="quiz",
            name="completed",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="quiz",
            name="correctlyAnswered",
            field=models.JSONField(blank=True, default=dict, null=True),
        ),
        migrations.AddField(
            model_name="quiz",
            name="incorrectlyAnswered",
            field=models.JSONField(blank=True, default=dict, null=True),
        ),
        migrations.AddField(
            model_name="quiz",
            name="unanswered",
            field=models.JSONField(default=dict),
        ),
        migrations.AddField(
            model_name="quiz",
            name="user",
            field=models.ForeignKey(
                default=2,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="quizzes",
                to=settings.AUTH_USER_MODEL,
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="quiz",
            name="id",
            field=models.UUIDField(
                default=uuid.uuid4, editable=False, primary_key=True, serialize=False
            ),
        ),
    ]
