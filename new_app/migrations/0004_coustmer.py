# Generated by Django 5.1.3 on 2024-11-27 05:43

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('new_app', '0003_alter_seller_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='coustmer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=20)),
                ('Age', models.CharField(max_length=3)),
                ('phone', models.CharField(max_length=10)),
                ('email', models.CharField(max_length=30)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='coustmer', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
