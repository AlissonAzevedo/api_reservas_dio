# Generated by Django 4.0.3 on 2022-04-01 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reserva', '0011_alter_reserva_data_devolucao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reserva',
            name='data_devolucao',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
