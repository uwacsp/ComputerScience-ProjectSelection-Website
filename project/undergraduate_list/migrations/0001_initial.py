# Generated by Django 2.2.4 on 2019-08-25 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('projectID', models.CharField(max_length=250)),
                ('description', models.CharField(max_length=500)),
            ],
        ),
    ]
