# Generated by Django 2.2.2 on 2019-10-21 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visitors', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visitor',
            name='household_number',
            field=models.CharField(choices=[('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5 or above', '5 or above')], max_length=3000, verbose_name='Number of People in Household'),
        ),
        migrations.AlterField(
            model_name='visitor',
            name='race',
            field=models.CharField(choices=[('White', 'White'), ('Black/Afro America', 'Black/Afro American'), ('Hispanic', 'Hispanic'), ('Asian', 'Asian'), ('Mixed', 'Mixed'), ('Other', 'Other')], max_length=3000, verbose_name='Ethnicity'),
        ),
    ]