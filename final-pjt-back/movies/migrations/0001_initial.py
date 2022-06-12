# Generated by Django 3.2.12 on 2022-05-24 11:41

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adult', models.BooleanField(default=False)),
                ('backdrop_path', models.CharField(max_length=100)),
                ('original_language', models.CharField(max_length=10)),
                ('overview', models.TextField()),
                ('popularity', models.FloatField()),
                ('poster_path', models.CharField(max_length=100)),
                ('released_date', models.DateField()),
                ('title', models.CharField(max_length=50)),
                ('vote_average', models.FloatField()),
                ('is_active', models.BooleanField()),
                ('genres', models.JSONField(default=dict)),
                ('director', models.CharField(max_length=100, null=True)),
                ('actors', models.JSONField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.FloatField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)])),
                ('content', models.CharField(max_length=30)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='scores', to='movies.movie')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='scores', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]