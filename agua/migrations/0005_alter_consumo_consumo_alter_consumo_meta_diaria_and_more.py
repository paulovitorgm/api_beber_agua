# Generated by Django 4.2.4 on 2023-08-09 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agua', '0004_consumo_percentual_consumido'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consumo',
            name='consumo',
            field=models.IntegerField(choices=[(250, 250), (350, 350), (500, 500)], default=0),
        ),
        migrations.AlterField(
            model_name='consumo',
            name='meta_diaria',
            field=models.IntegerField(default=0, editable=False),
        ),
        migrations.AlterField(
            model_name='consumo',
            name='percentual_consumido',
            field=models.DecimalField(decimal_places=2, default=0, editable=False, max_digits=5),
        ),
    ]
