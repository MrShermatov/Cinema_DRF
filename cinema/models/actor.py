from django.db import models


class Actor(models.Model):
    full_name = models.CharField(max_length=250)
    birth_date = models.DateField()

    def __str__(self):
        return self.full_name