# Generated by Django 2.2.5 on 2019-10-12 02:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ProposalApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='projectmodel',
            old_name='viewable',
            new_name='archived',
        ),
    ]