# Generated by Django 2.1.2 on 2019-05-07 04:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accountsetup', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='amount',
            field=models.PositiveIntegerField(blank=True),
        ),
    ]
