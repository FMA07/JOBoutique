# Generated by Django 5.0.6 on 2024-07-13 03:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0007_alter_donacion_img_donacion_alter_tela_img_tela'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='donacion',
            name='descripcion',
        ),
    ]
