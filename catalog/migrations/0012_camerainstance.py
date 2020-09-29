# Generated by Django 3.1.1 on 2020-09-25 22:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0011_basket'),
    ]

    operations = [
        migrations.CreateModel(
            name='CameraInstance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('s', 'In stok'), ('b', 'Booked')], default='s', max_length=1)),
                ('camera', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.camera')),
            ],
        ),
    ]