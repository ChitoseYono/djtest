from django.db import models

# Create your models here.
from django.utils.timezone import now
from django.contrib.auth.models import User


class Log(models.Model):
    user = models.ForeignKey(User, to_field='id', on_delete=models.CASCADE)
    name = models.CharField(max_length=32, default='Title')
    target = models.CharField(null=True, max_length=256)
    status = models.BooleanField(default=True)
    create_time = models.DateTimeField(default=now)
    end_time = models.CharField(null=True, max_length=32)

    def __str__(self):
        return self.name


class Flag(models.Model):
    seq = models.IntegerField()
    log = models.ForeignKey(Log, to_field='id', on_delete=models.CASCADE)
    name = models.CharField(max_length=32, default='Flag')
    content = models.TextField(null=True)
    create_time = models.DateTimeField(default=now)

    def __str__(self):
        return self.log.name + " " + str(self.seq) + ":" + self.name
