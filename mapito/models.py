from django.conf import settings
from django.db import models
from django.utils import timezone


class Estado(models.Model):
    nome = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    sigla = models.TextField()
    pop = models.PositiveIntegerField()  
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.sigla