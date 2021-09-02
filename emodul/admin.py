from django.contrib import admin
from .models import EModul, EModulComment, EModulDetail, EModulBookmark, EModulAnnotation
from akademik.models import MataKuliah
from accounts.models import CustomUser
from allauth.account.models import EmailAddress
from django.contrib.sites.models import Site

# Sembunyikan allauth account app
admin.site.unregister(EmailAddress)

# Semubnyikan app situs dari admin
admin.site.unregister(Site)
@admin.register(EModul)
class EModulAdmin(admin.ModelAdmin):
    list_display = ['mata_kuliah', 'judul', 'cover', 'jumlah_modul','tanggal']

    def get_queryset(self, request):
        qs = super(admin.ModelAdmin, self).get_queryset(request)

        if request.user.is_superuser:  # Jika user adalah superuser
            return qs                 # tampilkan semua emodul

        # Jika buka superuser, dapatkan objek user yang logged in (asumsinya adalah dosen)
       
        # filter matakuliah yang diajar oleh user logged in
        filter_matakuliah = MataKuliah.objects.filter(pengajar=request.user)

        # filter semua emodul dari mata kuliah yang diajar oleh user logged in
        emodul_terfilter = EModul.objects.filter(
            mata_kuliah__in=filter_matakuliah)

        return emodul_terfilter

    def formfield_for_foreignkey(self, db_field, request, **kwargs):

        # custom entri pada dropdown pilihan matakuliah
        # hanya menampilkan matakuliah yang diajar oleh user yang logged in
        if db_field.name == "mata_kuliah":

            # filter jika user logged in bukan superuser
            if not request.user.is_superuser:
                kwargs["queryset"] = MataKuliah.objects.filter(
                    pengajar=request.user)

            return super().formfield_for_foreignkey(db_field, request, **kwargs)

@admin.register(EModulDetail)
class EModulDetailAdmin(admin.ModelAdmin):
    list_display = ['emodul', 'judul', 'jumlah_halaman', 'file']

    def get_queryset(self, request):
        qs = super(admin.ModelAdmin, self).get_queryset(request)

        if request.user.is_superuser:  # Jika user adalah superuser
            return qs                 # tampilkan semua emodul

        # Jika buka superuser, dapatkan objek user yang logged in (asumsinya adalah dosen)
        # logged_in_user = CustomUser.objects.filter(
            # username=request.user.username).get()

        # filter matakuliah yang diajar oleh user logged in
        filter_matakuliah = MataKuliah.objects.filter(pengajar=request.user)

        # filter emodul dari mata kuliah yang diajar oleh user logged in
        filter_emodul = EModul.objects.filter(
            mata_kuliah__in=filter_matakuliah)

        # filter semua emoduldetail dari emodul mata kuliah yang diajar oleh user logged in
        emoduldetail_terfilter = EModulDetail.objects.filter(
            emodul__in=filter_emodul)

        return emoduldetail_terfilter

    def formfield_for_foreignkey(self, db_field, request, **kwargs):

        # custom entri pada dropdown pilihan emodul
        # hanya menampilkan emodul dari mata kuliah yang diajar oleh user yang logged in
        if db_field.name == "emodul":

            # filter jika user logged in bukan superuser
            if not request.user.is_superuser:
                # logged_in_user = CustomUser.objects.filter(
                #     username=request.user.username).get()

                # filter matakuliah yang diajar oleh user logged in
                filter_matakuliah = MataKuliah.objects.filter(
                    pengajar=request.user)

                # filter emodul dari mata kuliah yang diajar oleh user logged in
                kwargs["queryset"] = EModul.objects.filter(
                    mata_kuliah__in=filter_matakuliah)

            return super().formfield_for_foreignkey(db_field, request, **kwargs)


@admin.register(EModulAnnotation)
class EModulAnnotationAdmin(admin.ModelAdmin):
    list_display = ['dokumen', 'user', 'koordinat', 'halaman', 'text']

@admin.register(EModulBookmark)
class EModulBookmarkAdmin(admin.ModelAdmin):
    list_display = ['dokumen', 'user', 'halaman','tanggal']

@admin.register(EModulComment)
class EModulCommentAdmin(admin.ModelAdmin):
    list_display = ['dokumen', 'user', 'comment']




