# Generated by Django 4.2 on 2023-07-16 01:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='message',
            field=models.TextField(blank=True, null=True),
        ),
    ]
