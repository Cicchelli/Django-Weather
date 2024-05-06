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


class DailyWeather(models.Model):
    DESCRIPTION_CHOICES = [
        ("Ensolarado", "Ensolarado"),
        ("Nublado", "Nublado"),
        ("Chuvoso", "Chuvoso"),
        ("Parcialmente nublado", "Parcialmente nublado"),
        ("Neve", "Neve"),
        ("Granizo", "Granizo"),
    ]

    city = models.ForeignKey(
        City, on_delete=models.CASCADE, unique_for_date="date"
    )
    date = models.DateField()
    min_temp = models.FloatField()
    max_temp = models.FloatField()
    brief_description = models.CharField(
        max_length=20, choices=DESCRIPTION_CHOICES
    )

    def __str__(self) -> str:
        return f"{self.date.strftime('%d/%m/%Y')} - {self.brief_description}"
