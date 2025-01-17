# Generated by Django 5.0.6 on 2024-07-13 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pet', '0009_pet_details_pet_rehoming_fee_pet_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pet',
            name='details',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='pet',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Available To Adopt', 'Available To Adopt'), ('Processing', 'Processing'), ('Adopted', 'Adopted')], max_length=20),
        ),
    ]
