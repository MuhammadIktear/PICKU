# Generated by Django 5.0.6 on 2024-07-14 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pet', '0010_alter_pet_details_alter_pet_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pet',
            name='breed',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='pet',
            name='color',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='pet',
            name='sex',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='pet',
            name='size',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='pet',
            name='species',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='pet',
            name='status',
            field=models.CharField(max_length=20),
        ),
        migrations.DeleteModel(
            name='UserBankAccount',
        ),
    ]
