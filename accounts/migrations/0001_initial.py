# Generated by Django 3.1.4 on 2021-08-28 09:27

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    # dependencies = [
    #     ('akademik', '0002_matakuliah_pengajar'),
    #     ('auth', '0012_alter_user_first_name_max_length'),
    # ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('role', models.PositiveSmallIntegerField(choices=[(1, 'Mahasiswa'), (2, 'Dosen')], default=1, verbose_name='Role')),
                ('gender', models.PositiveSmallIntegerField(choices=[(1, 'Pria'), (2, 'Wanita')], default=1, verbose_name='Gender')),
                ('no_hp', models.CharField(default='+62123456789', help_text='Gunakan format internasional (+628XXXXXX)', max_length=16, verbose_name='Nomor HP/WA')),
                ('foto', models.ImageField(blank=True, default='images/foto_profil/default.jpg', null=True, upload_to='images/foto_profil/', verbose_name='Foto')),
                ('profil_user_lengkap', models.BooleanField(default=False, verbose_name='Profil user lengkap')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='ProfilMahasiswa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('semester', models.CharField(blank=True, choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8')], max_length=5, null=True, verbose_name='Semester')),
                ('nim', models.CharField(blank=True, max_length=15, null=True, verbose_name='NIM')),
                ('kelas', models.CharField(blank=True, max_length=5, null=True, verbose_name='Kelas')),
                ('no_absen', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='No. Absen')),
                ('profil_mahasiswa_lengkap', models.BooleanField(default=False, verbose_name='Profil mahasiswa lengkap')),
                ('prodi', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='akademik.programstudi', verbose_name='Program studi')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='profil_mahasiswa', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'profil mahasiswa',
                'verbose_name_plural': 'profil mahasiswa',
            },
        ),
        migrations.CreateModel(
            name='ProfilDosen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nidn', models.CharField(max_length=12, verbose_name='NIDN')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='profil_dosen', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'profil dosen',
                'verbose_name_plural': 'profil dosen',
            },
        ),
    ]
