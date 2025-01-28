from django.db import models

# Create your models here.
class Link(models.Model):

    def __str__(self):
        if self.name == None:
            return "NULL Name"
        return self.name

    address = models.CharField(max_length=1000, null=True, blank=True)
    name = models.CharField(max_length=1000, null=True, blank=True)