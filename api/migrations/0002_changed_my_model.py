# Generated by Django 4.2.1 on 2024-08-27 23:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anuncio',
            name='fechaEvento',
            field=models.DateTimeField(null=True),
        ),
    ]
