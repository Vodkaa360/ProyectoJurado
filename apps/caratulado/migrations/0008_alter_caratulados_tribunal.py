# Generated by Django 5.1.2 on 2024-10-30 22:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('caratulado', '0007_alter_caratulados_fecha_inicio_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='caratulados',
            name='tribunal',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7')], max_length=2, null=True),
        ),
    ]
