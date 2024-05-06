from django.db import models


# Create your models here.
class City(models.Model):
    name = models.CharField(max_length=60)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self) -> str:
        return f"{self.name}"

    def slugify(self) -> str:
        return f"{self.name.lower().replace(' ', '-')}"

    def save(self, *args, **kwargs):
        self.name = self.name.title()
        super(City, self).save(*args, **kwargs)
