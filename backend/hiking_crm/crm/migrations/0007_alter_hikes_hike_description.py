# Generated by Django 4.1.7 on 2023-03-21 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0006_create_clients'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hikes',
            name='hike_description',
            field=models.CharField(max_length=2000),
        ),
    ]
