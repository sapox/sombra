from django.db import models

# Create your models here.
class Sombra(models.Model):
	cadaver = models.TextField()
	def __str__(self):
		return self.cadaver