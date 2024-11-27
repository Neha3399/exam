# Generated by Django 5.1.3 on 2024-11-27 06:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('new_app', '0006_blog'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='sellerName',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='new_app.seller'),
            preserve_default=False,
        ),
    ]