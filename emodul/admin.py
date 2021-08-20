from django.contrib import admin
from .models import EModul, EModulComment, EModulDetail, EModulBookmark, EModulAnnotation

@admin.register(EModul)
class EModulAdmin(admin.ModelAdmin):
    list_display = ['mata_kuliah', 'judul', 'jumlah_modul','tanggal']

    def queryset(self, request):
        qs = super(admin.ModelAdmin, self).queryset(request)

        if request.user.is_superuser:
            return qs

        user_qs = penulis.objects.filter(user=request.user)
        return qs.filter(managers__in=user_qs)


@admin.register(EModulDetail)
class EModulDetailAdmin(admin.ModelAdmin):
    list_display = ['emodul', 'judul', 'jumlah_halaman', 'file']

@admin.register(EModulAnnotation)
class EModulAnnotationAdmin(admin.ModelAdmin):
    list_display = ['dokumen', 'user', 'halaman', 'text']

@admin.register(EModulBookmark)
class EModulBookmarkAdmin(admin.ModelAdmin):
    list_display = ['dokumen', 'user', 'halaman','tanggal']

@admin.register(EModulComment)
class EModulCommentAdmin(admin.ModelAdmin):
    list_display = ['dokumen', 'user', 'comment']




