# Generated by Django 3.1.1 on 2020-09-16 14:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_auto_20200916_1528'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cameraimg',
            name='Camera',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='imgs', to='catalog.camera'),
        ),
    ]
