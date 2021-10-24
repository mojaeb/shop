# Generated by Django 3.2.8 on 2021-10-23 12:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0029_remove_product_delivery_mode'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='authority',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='address',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='orders', to='api.address'),
        ),
    ]
