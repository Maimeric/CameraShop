# Generated by Django 3.1.1 on 2020-09-16 23:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0008_auto_20200917_0205'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='camera',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='comment', to='catalog.camera'),
        ),
    ]
