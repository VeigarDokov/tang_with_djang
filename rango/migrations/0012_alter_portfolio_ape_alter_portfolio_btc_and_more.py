# Generated by Django 5.0 on 2024-03-04 18:01

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("rango", "0011_portfolio"),
    ]

    operations = [
        migrations.AlterField(
            model_name="portfolio",
            name="ape",
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name="portfolio",
            name="btc",
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name="portfolio",
            name="xmr",
            field=models.FloatField(default=0),
        ),
    ]
