# Generated by Django 2.2.4 on 2019-08-15 18:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('department', models.CharField(blank=True, choices=[('', 'Select Department'), ('CD', 'Computer Department'), ('EE', 'Electrical Department'), ('ECD', 'Electronics and Communication Department'), ('MD', 'Mechanical Department'), ('PD', 'Production and Industial Department'), ('CD', 'Civil Department')], default='', max_length=50)),
                ('phone', models.IntegerField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'permissions': (('can_create_classroom', 'can create a classroom'), ('can_create_assignment', '')),
            },
        ),
        migrations.CreateModel(
            name='TeachersClassRoom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_id', models.SlugField(max_length=10, unique=True)),
                ('title', models.CharField(max_length=20)),
                ('section', models.CharField(max_length=10)),
                ('subject', models.CharField(max_length=30)),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teacher.Teacher')),
            ],
        ),
    ]
