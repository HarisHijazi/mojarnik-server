# Generated by Django 3.1.4 on 2021-08-21 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_remove_customuser_foto'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='foto',
            field=models.ImageField(blank=True, default='images/foto_profil/default.jpg', null=True, upload_to='images/foto_profil/', verbose_name='Foto'),
        ),
    ]