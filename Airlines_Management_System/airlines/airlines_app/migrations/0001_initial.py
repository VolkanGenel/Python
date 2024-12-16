# Generated by Django 5.1.3 on 2024-12-02 20:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Airplane",
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
                ("tail_number", models.CharField(max_length=50, unique=True)),
                ("model", models.CharField(max_length=150)),
                ("capacity", models.PositiveIntegerField(default=0)),
                ("production_year", models.PositiveIntegerField(default=0)),
                ("status", models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name="Flight",
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
                ("flight_number", models.CharField(max_length=50, unique=True)),
                ("departure", models.CharField(max_length=200)),
                ("destination", models.CharField(max_length=200)),
                ("departure_time", models.DateTimeField()),
                ("arrival_time", models.DateTimeField()),
                (
                    "airplane",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="flights",
                        to="airlines_app.airplane",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Reservation",
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
                ("passenger_name", models.CharField(max_length=50)),
                ("passenger_email", models.EmailField(max_length=200)),
                (
                    "reservation_code",
                    models.CharField(default="9F165476A0", max_length=10, unique=True),
                ),
                ("status", models.BooleanField(default=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "flight",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="reservations",
                        to="airlines_app.flight",
                    ),
                ),
            ],
        ),
    ]
