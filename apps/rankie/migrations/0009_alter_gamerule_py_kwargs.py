# Generated by Django 4.0.6 on 2022-08-02 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rankie', '0008_alter_gamerule_py_kwargs'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gamerule',
            name='py_kwargs',
            field=models.JSONField(blank=True, default=dict, null=True),
        ),
    ]
