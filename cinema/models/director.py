from django.db import models

class Director(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=300)
    birt_date = models.DateField(null=True, blank=True)
    bio = models.CharField(max_length=400)

    def __str__(self):
        return self.first_name
