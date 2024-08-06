# Generated by Django 4.2.1 on 2024-07-12 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_changed_my_model'),
    ]

    operations = [
        migrations.AddField(
            model_name='factura',
            name='usuarioVendedor',
            field=models.CharField(default=0),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='rol1',
            field=models.CharField(blank=True, choices=[('EXTERNO', 'EXTERNO'), ('APRENDIZ', 'APRENDIZ'), ('INSTRUCTOR', 'INSTRUCTOR'), ('FUNCIONARIO', 'FUNCIONARIO'), ('VENDEDOR', 'VENDEDOR'), ('TUTOR', 'TUTOR'), ('LIDER', 'LIDER'), ('PUNTO', 'PUNTO')], default='APRENDIZ', max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='rol2',
            field=models.CharField(blank=True, choices=[('EXTERNO', 'EXTERNO'), ('APRENDIZ', 'APRENDIZ'), ('INSTRUCTOR', 'INSTRUCTOR'), ('FUNCIONARIO', 'FUNCIONARIO'), ('VENDEDOR', 'VENDEDOR'), ('TUTOR', 'TUTOR'), ('LIDER', 'LIDER'), ('PUNTO', 'PUNTO')], default='APRENDIZ', max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='rol3',
            field=models.CharField(blank=True, choices=[('EXTERNO', 'EXTERNO'), ('APRENDIZ', 'APRENDIZ'), ('INSTRUCTOR', 'INSTRUCTOR'), ('FUNCIONARIO', 'FUNCIONARIO'), ('VENDEDOR', 'VENDEDOR'), ('TUTOR', 'TUTOR'), ('LIDER', 'LIDER'), ('PUNTO', 'PUNTO')], default='APRENDIZ', max_length=15, null=True),
        ),
    ]
