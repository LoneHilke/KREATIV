# Generated by Django 4.0.4 on 2022-05-04 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meetups', '0006_alter_meetup_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='meetup',
            name='alder',
            field=models.TextField(default='2022-05-04'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='meetup',
            name='materialer',
            field=models.TextField(default='2022-05-04'),
            preserve_default=False,
        ),
    ]