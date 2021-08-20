# Generated by Django 3.1.4 on 2021-08-20 08:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('akademik', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='matakuliah',
            name='pengajar',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pengajar_matakuliah', to=settings.AUTH_USER_MODEL, verbose_name='Pengajar'),
        ),
    ]
