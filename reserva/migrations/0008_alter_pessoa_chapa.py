# Generated by Django 4.0.3 on 2022-04-01 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reserva', '0007_reserva_pessoas'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pessoa',
            name='chapa',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
