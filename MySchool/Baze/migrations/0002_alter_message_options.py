# Generated by Django 4.2.9 on 2024-01-13 09:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Baze', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='message',
            options={'ordering': ['-updated', '-created']},
        ),
    ]
