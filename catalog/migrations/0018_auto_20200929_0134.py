# Generated by Django 3.1.1 on 2020-09-28 22:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0017_auto_20200929_0046'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'ordering': ('-created',), 'verbose_name': 'Orders', 'verbose_name_plural': 'Order'},
        ),
    ]