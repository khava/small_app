from django.db import models

from app.utils import get_upload_path


class Picture(models.Model):
    login = models.CharField(max_length=255, verbose_name='login')
    picture = models.ImageField(upload_to=get_upload_path, verbose_name='picture')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='created date')

    def __str__(self):
        return f'{self.login}`s image_{self.pk}'


class PictureHistory(models.Model):
    changed_date = models.DateTimeField(auto_now_add=True, verbose_name='changed date')
    old_path = models.CharField(max_length=300, verbose_name='old name')
    picture = models.ForeignKey(Picture, on_delete=models.CASCADE, related_name='picture_history')

    def __str__(self):
        return self.old_path
