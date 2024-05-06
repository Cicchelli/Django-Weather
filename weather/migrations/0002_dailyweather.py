from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("weather", "0001_init"),
    ]

    operations = [
        migrations.CreateModel(
            name="DailyWeather",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("date", models.DateTimeField()),
                ("min_temp", models.FloatField()),
                ("max_temp", models.FloatField()),
                ("brief_description", models.CharField(max_length=20)),
                (
                    "city",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="weather.city",
                        unique_for_date="date",
                    ),
                ),
            ],
        ),
    ]
