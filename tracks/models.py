from django.db import models
from django.urls import reverse


class Music(models.Model):
    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    album = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    release_date = models.DateField()
    image = models.ImageField(upload_to='images/')
    audio_file = models.FileField(upload_to='files/')

    def get_detail_url(self):
        return reverse('tracks:detail', args=[self.pk])

    def get_update_url(self):
        return reverse('tracks:update', args=[self.pk])

    def get_delete_url(self):
        return reverse('tracks:delete', args=[self.pk])