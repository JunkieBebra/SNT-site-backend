# Generated by Django 3.2.13 on 2023-09-29 20:27

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
            name='ImportantMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header', models.CharField(max_length=128)),
                ('content', models.TextField()),
                ('date_add', models.DateField()),
            ],
            options={
                'verbose_name': 'событие',
                'verbose_name_plural': 'События',
            },
        ),
        migrations.CreateModel(
            name='ProminentOnes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_start', models.DateField()),
                ('date_end', models.DateField()),
                ('type', models.CharField(choices=[('CR', 'Председатель'), ('GV', 'В составе правления'), ('GP', 'Член правления'), ('OB', 'В составе ревизионной комиссии')], max_length=2, verbose_name='Тип')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'ключевое лицо',
                'verbose_name_plural': 'Ключевые лица',
            },
        ),
    ]
