# Generated by Django 5.1.3 on 2024-12-01 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehiculos', '0005_alter_mantenimiento_evidencia_fotografica_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='mantenimiento',
            name='miniatura',
            field=models.ImageField(blank=True, null=True, upload_to='miniaturas/'),
        ),
    ]
