# Generated by Django 5.0a1 on 2023-10-24 03:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("pro13exapp", "0002_alter_jikwon_options"),
    ]

    operations = [
        migrations.AlterField(
            model_name="jikwon",
            name="buser_num",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="pro13exapp.buser"
            ),
        ),
        migrations.AlterModelTable(
            name="jikwon",
            table=None,
        ),
    ]
