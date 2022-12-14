# Generated by Django 4.1 on 2022-08-12 09:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256, verbose_name='title')),
                ('done', models.BooleanField(default=False, verbose_name='done?')),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='create at?')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='update at?')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'task',
                'verbose_name_plural': 'tasks',
            },
        ),
    ]
