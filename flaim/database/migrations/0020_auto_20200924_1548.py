# Generated by Django 3.0.7 on 2020-09-24 19:46

from django.db import migrations
from pathlib import Path
from django.conf import settings
import pandas as pd

REFERENCE_CSV = Path(settings.ROOT_DIR) / 'docs' / 'reference' / 'reference_amounts_2016.csv'
assert REFERENCE_CSV.exists()


def populate_category_support_table(apps, scheme_editor):
    """
    Method to auto-populate the ReferenceCategorySupport table upon migration
    :param apps:
    :param scheme_editor:
    :return:
    """
    df = pd.read_csv(REFERENCE_CSV)
    ReferenceCategorySupport = apps.get_model('database', 'ReferenceCategorySupport')
    for i, row in df.iterrows():
        obj, created = ReferenceCategorySupport.objects.get_or_create(
            category_id=row['major_category_id'],
            category=row['major_category'],
            subcategory_id=row['subcategory_id'],
            subcategory=row['subcategory'],
            reference_amount_raw=row['reference_amount']
        )
        if created:
            obj.save()


class Migration(migrations.Migration):
    dependencies = [
        ('database', '0019_auto_20200922_1451'),
    ]

    operations = [
        migrations.RunPython(populate_category_support_table, migrations.RunPython.noop)
    ]
