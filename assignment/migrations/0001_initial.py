# Generated by Django 2.2.3 on 2019-08-02 20:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('instructions', models.CharField(max_length=100)),
                ('due_date', models.DateTimeField()),
                ('assigned_date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='AssignmentsImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filename', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='images/')),
                ('assignment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='assignment.Assignment')),
            ],
        ),
    ]
