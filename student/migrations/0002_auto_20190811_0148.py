# Generated by Django 2.2.4 on 2019-08-10 20:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='student_user',
            new_name='user',
        ),
    ]
