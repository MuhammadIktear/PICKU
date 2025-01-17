# Generated by Django 5.0.6 on 2024-07-14 14:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filter', '0001_initial'),
        ('pet', '0011_alter_pet_breed_alter_pet_color_alter_pet_sex_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pet',
            name='breed',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='filter.breed'),
        ),
        migrations.AlterField(
            model_name='pet',
            name='color',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='filter.color'),
        ),
        migrations.AlterField(
            model_name='pet',
            name='sex',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='filter.sex'),
        ),
        migrations.AlterField(
            model_name='pet',
            name='size',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='filter.size'),
        ),
        migrations.AlterField(
            model_name='pet',
            name='species',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='filter.species'),
        ),
        migrations.AlterField(
            model_name='pet',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='filter.status'),
        ),
    ]
