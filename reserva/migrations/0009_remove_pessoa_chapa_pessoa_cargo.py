# Generated by Django 4.0.3 on 2022-04-01 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reserva', '0008_alter_pessoa_chapa'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pessoa',
            name='chapa',
        ),
        migrations.AddField(
            model_name='pessoa',
            name='cargo',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
