from django.contrib import admin
from .models import EModul, EModulComment, EModulDetail, EModulBookmark, EModulAnnotation
from akademik.models import MataKuliah
from accounts.models import CustomUser


@admin.register(EModul)
class EModulAdmin(admin.ModelAdmin):
    list_display = ['mata_kuliah', 'judul', 'jumlah_modul', 'tanggal']

    def get_queryset(self, request):
        qs = super(admin.ModelAdmin, self).get_queryset(request)

        if request.user.is_superuser:
            return qs

        logged_in_user = CustomUser.objects.filter(
            username=request.user.username).get()
        filter_matakuliah = MataKuliah.objects.filter(pengajar=logged_in_user)
        emodul_terfilter = EModul.objects.filter(
            mata_kuliah__in=filter_matakuliah)
        return emodul_terfilter


@admin.register(EModulDetail)
class EModulDetailAdmin(admin.ModelAdmin):
    list_display = ['emodul', 'judul', 'jumlah_halaman', 'file']


@admin.register(EModulAnnotation)
class EModulAnnotationAdmin(admin.ModelAdmin):
    list_display = ['dokumen', 'user', 'koordinat', 'halaman', 'text']


@admin.register(EModulBookmark)
class EModulBookmarkAdmin(admin.ModelAdmin):
    list_display = ['dokumen', 'user', 'halaman', 'tanggal']


@admin.register(EModulComment)
class EModulCommentAdmin(admin.ModelAdmin):
    list_display = ['dokumen', 'user', 'comment']
