from django.db import models

# Create your models here.

class Location(models.Model):
    location = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def is_location_invalid(self):
        if location == None:
            return true
        elif location == "":
            return True
        else:
            return False

    def __str__(self):
        return self.location
