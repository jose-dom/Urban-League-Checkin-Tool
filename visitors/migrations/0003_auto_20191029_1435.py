# Generated by Django 2.2.2 on 2019-10-29 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visitors', '0002_auto_20191021_1249'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visitor',
            name='household_income',
            field=models.CharField(choices=[('under $25,000', 'under $25,000'), ('$25,000 - $35,000', '$25,000 - $35,000'), ('$35,000 - $45,000', '$35,000 - $45,000'), ('$45,000 - $55,000', '$45,000 - $55,000'), ('$55,000 - $65,000', '$55,000 - $65,000'), ('$65,000 - $75,000', '$65,000 - $75,000'), ('$75,000 - $85,000', '$75,000 - $85,000'), ('over $85,000', 'over $85,000')], max_length=100, verbose_name='Household Income'),
        ),
    ]
