# Generated by Django 5.1.1 on 2024-11-11 18:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_employee'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='company',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='api.company'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='about',
            field=models.TextField(),
        ),
    ]
