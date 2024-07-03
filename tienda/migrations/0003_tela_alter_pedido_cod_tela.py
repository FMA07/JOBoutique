# Generated by Django 5.0.6 on 2024-07-03 01:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0002_producto_img_producto_alter_donacion_img_donacion'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tela',
            fields=[
                ('cod_tela', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('img_tela', models.ImageField(null=True, upload_to='producto')),
                ('nomb_tela', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='pedido',
            name='cod_tela',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tienda.tela'),
        ),
    ]
