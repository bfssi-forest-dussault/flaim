# Generated by Django 3.0.7 on 2020-09-25 13:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0020_auto_20200924_1548'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='referencecategorysupport',
            name='reference_amount',
        ),
        migrations.RemoveField(
            model_name='referencecategorysupport',
            name='reference_amount_extra',
        ),
        migrations.RemoveField(
            model_name='referencecategorysupport',
            name='reference_amount_units',
        ),
    ]