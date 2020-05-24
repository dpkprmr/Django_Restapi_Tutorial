from fileinput import filename

from django.db import models
from django.conf import settings


def upload_update_image(instance, fillename):
    return "webApp1/{user}/{filename}".format(user=instance.user, filename=filename)

# Create your models here.
class Update_data(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to=upload_update_image, blank=True, null=True)
    updated = models.DateTimeField(auto_now=True)
    timestamp= models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content or " "
