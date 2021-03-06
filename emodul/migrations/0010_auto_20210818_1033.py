# Generated by Django 3.1.4 on 2021-08-18 03:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('emodul', '0009_auto_20210802_1541'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emodulcomment',
            name='dokumen',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='emodul.emoduldetail', verbose_name='EModul Detail'),
        ),
        migrations.AlterField(
            model_name='emodulcomment',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to=settings.AUTH_USER_MODEL, verbose_name='Pengguna'),
        ),
        migrations.AlterField(
            model_name='emoduldetail',
            name='file',
            field=models.FileField(upload_to=None, verbose_name='Berkas'),
        ),
    ]
