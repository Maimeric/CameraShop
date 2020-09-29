# Generated by Django 3.1.1 on 2020-09-16 12:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_auto_20200916_1204'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='categories',
            name='camera',
        ),
        migrations.AddField(
            model_name='camera',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.categories'),
        ),
    ]