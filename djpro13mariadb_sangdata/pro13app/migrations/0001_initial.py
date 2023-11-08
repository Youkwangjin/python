# Generated by Django 5.0a1 on 2023-10-23 07:21

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Sangdata",
            fields=[
                ("code", models.IntegerField(primary_key=True, serialize=False)),
                ("sang", models.CharField(blank=True, max_length=20, null=True)),
                ("su", models.IntegerField(blank=True, null=True)),
                ("dan", models.IntegerField(blank=True, null=True)),
            ],
            options={
                "db_table": "sangdata",
                "managed": False,
            },
        ),
    ]
