# Generated by Django 2.2.5 on 2019-09-26 09:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ProposalApp', '0012_auto_20190926_1704'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='unitmodel',
            name='contentInfo',
        ),
    ]