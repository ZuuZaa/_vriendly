from django.db import models

# Create your models here.
class MyApp(models.Model):

    name = models.CharField(max_length=200)
    version = models.CharField(max_length=200)
    download_link_for_windows = models.CharField(max_length=200)
    download_link_for_linux = models.CharField(max_length=200)
    download_link_for_macos = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'App'
        verbose_name_plural = 'Apps'

    def __str__(self):
        return f"{self.name}"

class Manager_ID(models.Model):

    manager_id = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'Manager ID'
        verbose_name_plural = 'Manager ID'
    