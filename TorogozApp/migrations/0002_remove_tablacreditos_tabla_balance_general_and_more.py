# Generated by Django 5.0.4 on 2024-04-08 23:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TorogozApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tablacreditos',
            name='tabla_balance_general',
        ),
        migrations.RemoveField(
            model_name='tablarenovaciones',
            name='tabla_balance_general',
        ),
        migrations.AlterField(
            model_name='tablacreditos',
            name='id_tabla_general',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='TorogozApp.tablabalancegeneral'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='tablarenovaciones',
            name='id_tabla_general',
            field=models.ForeignKey(default=33, on_delete=django.db.models.deletion.CASCADE, to='TorogozApp.tablabalancegeneral'),
            preserve_default=False,
        ),
    ]
