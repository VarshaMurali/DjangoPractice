# Generated by Django 2.1.2 on 2019-02-16 03:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registry', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='name',
            new_name='student_name',
        ),
        migrations.RenameField(
            model_name='teacher',
            old_name='name',
            new_name='teacher_name',
        ),
    ]
