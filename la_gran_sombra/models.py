from django.db import models


class Sombra(models.Model):
    cadaver = models.TextField()

    def __unicode__(self):
        return self.cadaver
