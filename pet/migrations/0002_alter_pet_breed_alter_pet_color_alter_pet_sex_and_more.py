# Generated by Django 5.0.6 on 2024-07-13 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pet', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pet',
            name='breed',
            field=models.CharField(choices=[('Labrador', 'Labrador'), ('Persian', 'Persian')], max_length=50),
        ),
        migrations.AlterField(
            model_name='pet',
            name='color',
            field=models.CharField(choices=[('Black', 'Black'), ('White', 'White')], max_length=50),
        ),
        migrations.AlterField(
            model_name='pet',
            name='sex',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=50),
        ),
        migrations.AlterField(
            model_name='pet',
            name='size',
            field=models.CharField(choices=[('Small', 'Small'), ('Medium', 'Medium')], max_length=50),
        ),
        migrations.AlterField(
            model_name='pet',
            name='species',
            field=models.CharField(choices=[('Dog', 'Dog'), ('Cat', 'Cat')], max_length=50),
        ),
    ]
