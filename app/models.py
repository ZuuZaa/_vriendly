from django.db import models

# Create your models here.
class Master_IP(models.Model):

    name = models.CharField(max_length=200)
    IP = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'Master IP'
        verbose_name_plural = 'Master IP'
        
    def __str__(self):
        return f"{self.name}"

class MyApp(models.Model):

    name = models.CharField(max_length=200)
    version = models.CharField(max_length=200)
    download_link_for_windows = models.CharField(max_length=200)
    download_link_for_linux = models.CharField(max_length=200)
    download_link_for_macos = models.CharField(max_length=200)
    master_IP = models.ForeignKey(Master_IP, on_delete = models.CASCADE, null=True)

    class Meta:
        verbose_name = 'App'
        verbose_name_plural = 'Apps'

    def __str__(self):
        return f"{self.name}"


    