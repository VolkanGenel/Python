# Generated by Django 5.1.3 on 2024-12-03 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("airlines_app", "0002_alter_reservation_reservation_code"),
    ]

    operations = [
        migrations.AlterField(
            model_name="reservation",
            name="reservation_code",
            field=models.CharField(default="C7BA4150A2", max_length=10, unique=True),
        ),
    ]
