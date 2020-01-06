from django.db import models

# Create your models here.
class plane (models.Model):
    name = models.CharField(max_length=128)
    slug = models.SlugField(max_length=128, unique=True)
    type = models.CharField(max_length=128)

    def __str__(self):
        return '{}'.format(self.name)


