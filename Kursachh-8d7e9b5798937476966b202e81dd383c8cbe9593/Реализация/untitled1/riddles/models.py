from django.db import models
from django.shortcuts import reverse


# Create your models here.
class plane(models.Model):
    name = models.CharField(max_length=128)
    slug = models.SlugField(max_length=128, unique=True)
    type = models.CharField(max_length=128)
    flys = models.ManyToManyField('fly', related_name='planes')


def get_absolute_url(self):
    return reverse('air_detail_url', kwargs={'slug': self.slug})


def __str__(self):
    return self.name


class fly(models.Model):
    time = models.CharField(max_length=50)

    def __str__(self):
        return '{}'.format(self.time)
