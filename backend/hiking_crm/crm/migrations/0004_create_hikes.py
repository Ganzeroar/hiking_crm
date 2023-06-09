# Generated by Django 4.1.7 on 2023-03-21 10:42

from django.db import migrations
from crm.initial_data import hikes_data


def create_hikes(apps, schema_editor):
    Hikes = apps.get_model('crm', 'Hikes')

    first_hike = Hikes(
        hike_name=hikes_data.first_hike_name,
        hike_description=hikes_data.first_hike_description,
    )
    first_hike.save()

    second_hike = Hikes(
        hike_name=hikes_data.second_hike_name,
        hike_description=hikes_data.second_hike_description,
    )
    second_hike.save()

    third_hike = Hikes(
        hike_name=hikes_data.third_hike_name,
        hike_description=hikes_data.third_hike_description,
    )
    third_hike.save()

    fourth_hike = Hikes(
        hike_name=hikes_data.fourth_hike_name,
        hike_description=hikes_data.fourth_hike_description,
    )
    fourth_hike.save()

    fifth_hike = Hikes(
        hike_name=hikes_data.fifth_hike_name,
        hike_description=hikes_data.fifth_hike_description,
    )
    fifth_hike.save()

    sixth_hike = Hikes(
        hike_name=hikes_data.sixth_hike_name,
        hike_description=hikes_data.sixth_hike_description,
    )
    sixth_hike.save()

    seventh_hike = Hikes(
        hike_name=hikes_data.seventh_hike_name,
        hike_description=hikes_data.seventh_hike_description,
    )
    seventh_hike.save()

    eighth_hike = Hikes(
        hike_name=hikes_data.eighth_hike_name,
        hike_description=hikes_data.eighth_hike_description,
    )
    eighth_hike.save()

    ninth_hike = Hikes(
        hike_name=hikes_data.ninth_hike_name,
        hike_description=hikes_data.ninth_hike_description,
    )
    ninth_hike.save()

    tenth_hike = Hikes(
        hike_name=hikes_data.tenth_hike_name,
        hike_description=hikes_data.tenth_hike_description,
    )
    tenth_hike.save()


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0003_hikes'),
    ]

    operations = [
        migrations.RunPython(create_hikes)
    ]

