# Generated by Django 2.2.7 on 2019-11-20 18:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='application',
            old_name='application_date',
            new_name='date',
        ),
    ]