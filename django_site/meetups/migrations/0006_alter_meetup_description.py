# Generated by Django 4.0.4 on 2022-04-25 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meetups', '0005_meetup_date_meetup_organizer_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meetup',
            name='description',
            field=models.TextField(),
        ),
    ]
