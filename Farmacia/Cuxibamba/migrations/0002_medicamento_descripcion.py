# Generated by Django 5.1.5 on 2025-01-27 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cuxibamba', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='medicamento',
            name='descripcion',
            field=models.TextField(blank=True, null=True),
        ),
    ]
