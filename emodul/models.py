from django.db import models
from django.utils.translation import ugettext as _
from django.contrib.auth import get_user_model
from django.conf import settings
from akademik.models import MataKuliah, Jurusan

User = get_user_model()


class EModul(models.Model):

    mata_kuliah = models.ForeignKey("akademik.MataKuliah", verbose_name=_(
        'Mata kuliah'), on_delete=models.CASCADE, related_name='emodul')
    judul = models.CharField(_("Judul modul"), max_length=50)
    jumlah_modul = models.SmallIntegerField(
        _("Jumlah Modul"), null=True, blank=True)
    # penulis = models.ForeignKey(User, verbose_name=_(
    #     "Uploader"), on_delete=models.CASCADE, null=True, blank=True, related_name='emodul')
    tanggal = models.DateField(verbose_name=_("Tanggal Upload"), auto_now=True)

    class Meta:
        verbose_name = 'eModul'
        verbose_name_plural = 'eModul'

    def __str__(self):
        return self.judul


class EModulDetail(models.Model):
    emodul = models.ForeignKey("EModul", verbose_name=_(
        "EModul"), on_delete=models.CASCADE, related_name='details')
    judul = models.CharField(_("Judul dokumen"), max_length=50)
    jumlah_halaman = models.SmallIntegerField(
        _("Jumlah halaman"), null=True, blank=True)
    file = models.FileField(
        _("File"), upload_to="emodul_detail/%Y/%m/%d/", max_length=100)

    class Meta:
        verbose_name = 'eModul detail'
        verbose_name_plural = 'eModul detail'

    def __str__(self):
        return self.judul


class EModulAnnotation(models.Model):
    dokumen = models.ForeignKey("EModulDetail", verbose_name=_(
        "EModul Detail"), on_delete=models.CASCADE, related_name='annotations')
    user = models.ForeignKey(User, verbose_name=_(
        "Pengguna"), on_delete=models.CASCADE, related_name='annotations')
    koordinat = models.CharField(
        _("Koordinat"), max_length=20, null=True, blank=True)
    halaman = models.PositiveSmallIntegerField(_("Halaman"))
    text = models.TextField(_("Text anotasi"))

    class Meta:
        verbose_name = 'eModul annotation'
        verbose_name_plural = 'eModul annotation'

    def __str__(self):
        return f'{self.dokumen.judul} {self.user.username}'


class EModulBookmark(models.Model):
    dokumen = models.ForeignKey("EModulDetail", verbose_name=_(
        "EModul Detail"), on_delete=models.CASCADE, related_name='bookmarks')
    user = models.ForeignKey(User, verbose_name=_(
        "Pengguna"), on_delete=models.CASCADE, related_name='bookmarks')
    halaman = models.PositiveSmallIntegerField(_("Halaman"))
    tanggal = models.DateField(verbose_name=_(
        "Tanggal Bookmark"), auto_now=True)

    class Meta:
        verbose_name = 'eModul bookmark'
        verbose_name_plural = 'eModul bookmark'

    def __str__(self):
        return f'{self.dokumen.judul} {self.user.username}'


class EModulComment(models.Model):
    dokumen = models.ForeignKey("EModulDetail", verbose_name=_(
        "EModul Detail"),  on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, verbose_name=_(
        "Pengguna"),  on_delete=models.CASCADE, related_name='comments')
    comment = models.TextField(_("Komentar"))

    class Meta:
        verbose_name = 'eModul comment'
        verbose_name_plural = 'eModul comment'

    def __str__(self):
        return f'{self.dokumen.judul} {self.user.username}'
