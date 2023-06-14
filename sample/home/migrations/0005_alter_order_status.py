# Generated by Django 4.2.1 on 2023-06-09 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_alter_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Ordered', 'Ordered')], default='Pending', max_length=10),
        ),
    ]
