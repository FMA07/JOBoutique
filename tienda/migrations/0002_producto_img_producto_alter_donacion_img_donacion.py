# Generated by Django 5.0.6 on 2024-07-02 23:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='img_producto',
            field=models.ImageField(null=True, upload_to='productos'),
        ),
        migrations.AlterField(
            model_name='donacion',
            name='img_donacion',
            field=models.ImageField(null=True, upload_to='productos'),
        ),
    ]
