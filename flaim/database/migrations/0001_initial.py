# Generated by Django 3.0.6 on 2020-05-26 17:50

import django.contrib.postgres.fields
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion
import flaim.database.models
import simple_history.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AmazonProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('bullet_points', models.TextField(blank=True, null=True)),
                ('manufacturer_reference', models.CharField(blank=True, max_length=100, null=True)),
                ('speciality', models.CharField(blank=True, max_length=100, null=True)),
                ('units', models.CharField(blank=True, max_length=30, null=True)),
                ('item_weight', models.CharField(blank=True, max_length=30, null=True)),
                ('parcel_dimensions', models.CharField(blank=True, max_length=30, null=True)),
                ('date_first_available', models.DateField(blank=True, null=True)),
                ('image_directory', models.CharField(blank=True, max_length=1000, null=True)),
            ],
            options={
                'verbose_name': 'Amazon Product',
                'verbose_name_plural': 'Amazon Products',
            },
        ),
        migrations.CreateModel(
            name='AmazonProductReview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('review_title', models.CharField(max_length=300)),
                ('review_text', models.TextField(blank=True, null=True)),
                ('reviewer_username', models.CharField(max_length=100)),
                ('rating', models.FloatField()),
                ('helpful', models.BooleanField()),
            ],
            options={
                'verbose_name': 'Amazon Product Review',
                'verbose_name_plural': 'Amazon Product Reviews',
            },
        ),
        migrations.CreateModel(
            name='AmazonSearchResult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('search_string', models.CharField(max_length=500)),
                ('page', models.IntegerField()),
                ('item_number', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Amazon Search Result',
                'verbose_name_plural': 'Amazon Search Results',
            },
        ),
        migrations.CreateModel(
            name='FrontOfPackLabel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('classifier_result_json', django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True)),
                ('label_detected', models.BooleanField()),
                ('label_type', models.CharField(blank=True, choices=[('FC', 'FOOD_COLOURING')], max_length=30, null=True)),
                ('classified_image_path', models.ImageField(max_length=1000, upload_to=flaim.database.models.upload_fop_image)),
            ],
            options={
                'verbose_name': 'FOP Label',
                'verbose_name_plural': 'FOP Labels',
            },
        ),
        migrations.CreateModel(
            name='HistoricalAmazonProduct',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('created', models.DateTimeField(blank=True, editable=False)),
                ('modified', models.DateTimeField(blank=True, editable=False)),
                ('bullet_points', models.TextField(blank=True, null=True)),
                ('manufacturer_reference', models.CharField(blank=True, max_length=100, null=True)),
                ('speciality', models.CharField(blank=True, max_length=100, null=True)),
                ('units', models.CharField(blank=True, max_length=30, null=True)),
                ('item_weight', models.CharField(blank=True, max_length=30, null=True)),
                ('parcel_dimensions', models.CharField(blank=True, max_length=30, null=True)),
                ('date_first_available', models.DateField(blank=True, null=True)),
                ('image_directory', models.CharField(blank=True, max_length=1000, null=True)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
            ],
            options={
                'verbose_name': 'historical Amazon Product',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalLoblawsProduct',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('created', models.DateTimeField(blank=True, editable=False)),
                ('modified', models.DateTimeField(blank=True, editable=False)),
                ('upc_list', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=300), blank=True, null=True, size=None)),
                ('api_data', django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
            ],
            options={
                'verbose_name': 'historical Loblaws Product',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalNutritionFacts',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('created', models.DateTimeField(blank=True, editable=False)),
                ('modified', models.DateTimeField(blank=True, editable=False)),
                ('total_size', models.CharField(blank=True, max_length=200, null=True)),
                ('serving_size_raw', models.CharField(blank=True, max_length=200, null=True)),
                ('serving_size', models.IntegerField(blank=True, null=True)),
                ('serving_size_units', models.CharField(blank=True, choices=[('g', 'grams'), ('mL', 'millilitres')], max_length=11, null=True)),
                ('ingredients', models.TextField(blank=True, null=True)),
                ('calories', models.IntegerField(blank=True, null=True)),
                ('sodium', models.FloatField(blank=True, null=True)),
                ('sodium_dv', models.FloatField(blank=True, null=True)),
                ('calcium', models.FloatField(blank=True, null=True)),
                ('calcium_dv', models.FloatField(blank=True, null=True)),
                ('totalfat', models.FloatField(blank=True, null=True)),
                ('totalfat_dv', models.FloatField(blank=True, null=True)),
                ('monounsaturated_fat', models.FloatField(blank=True, null=True)),
                ('polyunsaturated_fat', models.FloatField(blank=True, null=True)),
                ('omega3fattyacids', models.FloatField(blank=True, null=True)),
                ('saturatedfat', models.FloatField(blank=True, null=True)),
                ('saturatedfat_dv', models.FloatField(blank=True, null=True)),
                ('transfat', models.FloatField(blank=True, null=True)),
                ('transfat_dv', models.FloatField(blank=True, null=True)),
                ('potassium', models.FloatField(blank=True, null=True)),
                ('potassium_dv', models.FloatField(blank=True, null=True)),
                ('totalcarbohydrate', models.FloatField(blank=True, null=True)),
                ('totalcarbohydrate_dv', models.FloatField(blank=True, null=True)),
                ('othercarbohydrates', models.FloatField(blank=True, null=True)),
                ('dietaryfiber', models.FloatField(blank=True, null=True)),
                ('dietaryfiber_dv', models.FloatField(blank=True, null=True)),
                ('sugar', models.FloatField(blank=True, null=True)),
                ('protein', models.FloatField(blank=True, null=True)),
                ('cholesterol', models.FloatField(blank=True, null=True)),
                ('vitamina', models.FloatField(blank=True, null=True)),
                ('vitamina_dv', models.FloatField(blank=True, null=True)),
                ('vitaminc', models.FloatField(blank=True, null=True)),
                ('vitaminc_dv', models.FloatField(blank=True, null=True)),
                ('vitamind', models.FloatField(blank=True, null=True)),
                ('vitamine', models.FloatField(blank=True, null=True)),
                ('niacin', models.FloatField(blank=True, null=True)),
                ('vitaminb6', models.FloatField(blank=True, null=True)),
                ('folacin', models.FloatField(blank=True, null=True)),
                ('folate', models.FloatField(blank=True, null=True)),
                ('vitaminb12', models.FloatField(blank=True, null=True)),
                ('pantothenicacid', models.FloatField(blank=True, null=True)),
                ('pantothenate', models.FloatField(blank=True, null=True)),
                ('alcohol', models.FloatField(blank=True, null=True)),
                ('erythritol', models.FloatField(blank=True, null=True)),
                ('glycerol', models.FloatField(blank=True, null=True)),
                ('isomalt', models.FloatField(blank=True, null=True)),
                ('lactitol', models.FloatField(blank=True, null=True)),
                ('maltitol', models.FloatField(blank=True, null=True)),
                ('mannitol', models.FloatField(blank=True, null=True)),
                ('polydextrose', models.FloatField(blank=True, null=True)),
                ('sorbitol', models.FloatField(blank=True, null=True)),
                ('xylitol', models.FloatField(blank=True, null=True)),
                ('iron', models.FloatField(blank=True, null=True)),
                ('iron_dv', models.FloatField(blank=True, null=True)),
                ('riboflavin', models.FloatField(blank=True, null=True)),
                ('selenium', models.FloatField(blank=True, null=True)),
                ('magnesium', models.FloatField(blank=True, null=True)),
                ('phosphorus', models.FloatField(blank=True, null=True)),
                ('thiamine', models.FloatField(blank=True, null=True)),
                ('zinc', models.FloatField(blank=True, null=True)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
            ],
            options={
                'verbose_name': 'historical Product Nutrition',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalProduct',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('created', models.DateTimeField(blank=True, editable=False)),
                ('modified', models.DateTimeField(blank=True, editable=False)),
                ('product_code', models.CharField(db_index=True, max_length=500)),
                ('name', models.CharField(blank=True, max_length=500, null=True)),
                ('brand', models.CharField(blank=True, max_length=500, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('breadcrumbs_text', models.CharField(blank=True, max_length=600, null=True)),
                ('breadcrumbs_array', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=300), blank=True, null=True, size=None)),
                ('store', models.CharField(choices=[('LOBLAWS', 'Loblaws'), ('WALMART', 'Walmart'), ('AMAZON', 'Amazon')], max_length=20)),
                ('price', models.CharField(blank=True, max_length=200, null=True)),
                ('price_float', models.FloatField(blank=True, null=True)),
                ('price_units', models.CharField(blank=True, max_length=20, null=True)),
                ('upc_code', models.CharField(blank=True, max_length=500, null=True)),
                ('nutrition_available', models.BooleanField(blank=True, null=True)),
                ('unidentified_nft_format', models.BooleanField(default=False)),
                ('nielsen_product', models.BooleanField(blank=True, null=True)),
                ('url', models.URLField(blank=True, max_length=1000, null=True)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
            ],
            options={
                'verbose_name': 'historical Product',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalWalmartProduct',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('created', models.DateTimeField(blank=True, editable=False)),
                ('modified', models.DateTimeField(blank=True, editable=False)),
                ('image_directory', models.CharField(blank=True, max_length=500, null=True)),
                ('sku', models.CharField(blank=True, max_length=100, null=True)),
                ('bullets', models.TextField(blank=True, null=True)),
                ('dietary_info', models.TextField(blank=True, null=True)),
                ('nutrition_facts_json', django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
            ],
            options={
                'verbose_name': 'historical Walmart Product',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('product_code', models.CharField(max_length=500, unique=True)),
                ('name', models.CharField(blank=True, max_length=500, null=True)),
                ('brand', models.CharField(blank=True, max_length=500, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('breadcrumbs_text', models.CharField(blank=True, max_length=600, null=True)),
                ('breadcrumbs_array', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=300), blank=True, null=True, size=None)),
                ('store', models.CharField(choices=[('LOBLAWS', 'Loblaws'), ('WALMART', 'Walmart'), ('AMAZON', 'Amazon')], max_length=20)),
                ('price', models.CharField(blank=True, max_length=200, null=True)),
                ('price_float', models.FloatField(blank=True, null=True)),
                ('price_units', models.CharField(blank=True, max_length=20, null=True)),
                ('upc_code', models.CharField(blank=True, max_length=500, null=True)),
                ('nutrition_available', models.BooleanField(blank=True, null=True)),
                ('unidentified_nft_format', models.BooleanField(default=False)),
                ('nielsen_product', models.BooleanField(blank=True, null=True)),
                ('url', models.URLField(blank=True, max_length=1000, null=True)),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
            },
        ),
        migrations.CreateModel(
            name='ProductLink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ScrapeBatch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('scrape_date', models.DateField(null=True)),
                ('store', models.CharField(choices=[('LOBLAWS', 'Loblaws'), ('WALMART', 'Walmart'), ('AMAZON', 'Amazon')], max_length=7)),
                ('scraper_version', models.CharField(blank=True, max_length=15, null=True)),
                ('total_products', models.IntegerField(blank=True, null=True)),
                ('new_products', models.IntegerField(blank=True, null=True)),
                ('missing_products', models.IntegerField(blank=True, null=True)),
                ('notes', models.TextField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Scrape Batch',
                'verbose_name_plural': 'Scrape Batches',
            },
        ),
        migrations.CreateModel(
            name='WalmartProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('image_directory', models.CharField(blank=True, max_length=500, null=True)),
                ('sku', models.CharField(blank=True, max_length=100, null=True)),
                ('bullets', models.TextField(blank=True, null=True)),
                ('dietary_info', models.TextField(blank=True, null=True)),
                ('nutrition_facts_json', django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True)),
                ('product', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='walmart_product', to='database.Product')),
            ],
            options={
                'verbose_name': 'Walmart Product',
                'verbose_name_plural': 'Walmart Products',
            },
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('image_path', models.ImageField(max_length=1200, unique=True, upload_to=flaim.database.models.upload_product_image)),
                ('image_number', models.IntegerField(blank=True, null=True)),
                ('image_label', models.CharField(blank=True, max_length=50, null=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_image', to='database.Product')),
            ],
            options={
                'verbose_name': 'Product Image',
                'verbose_name_plural': 'Product Images',
            },
        ),
        migrations.AddField(
            model_name='product',
            name='batch',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='database.ScrapeBatch'),
        ),
        migrations.CreateModel(
            name='NutritionLabelClassification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('classification', models.CharField(blank=True, choices=[('N', 'NUTRITION'), ('I', 'INGREDIENTS'), ('O', 'OTHER')], max_length=15, null=True)),
                ('product_image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='image_classification', to='database.ProductImage')),
            ],
            options={
                'verbose_name': 'Image Classification',
                'verbose_name_plural': 'Image Classifications',
            },
        ),
        migrations.CreateModel(
            name='NutritionFacts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('total_size', models.CharField(blank=True, max_length=200, null=True)),
                ('serving_size_raw', models.CharField(blank=True, max_length=200, null=True)),
                ('serving_size', models.IntegerField(blank=True, null=True)),
                ('serving_size_units', models.CharField(blank=True, choices=[('g', 'grams'), ('mL', 'millilitres')], max_length=11, null=True)),
                ('ingredients', models.TextField(blank=True, null=True)),
                ('calories', models.IntegerField(blank=True, null=True)),
                ('sodium', models.FloatField(blank=True, null=True)),
                ('sodium_dv', models.FloatField(blank=True, null=True)),
                ('calcium', models.FloatField(blank=True, null=True)),
                ('calcium_dv', models.FloatField(blank=True, null=True)),
                ('totalfat', models.FloatField(blank=True, null=True)),
                ('totalfat_dv', models.FloatField(blank=True, null=True)),
                ('monounsaturated_fat', models.FloatField(blank=True, null=True)),
                ('polyunsaturated_fat', models.FloatField(blank=True, null=True)),
                ('omega3fattyacids', models.FloatField(blank=True, null=True)),
                ('saturatedfat', models.FloatField(blank=True, null=True)),
                ('saturatedfat_dv', models.FloatField(blank=True, null=True)),
                ('transfat', models.FloatField(blank=True, null=True)),
                ('transfat_dv', models.FloatField(blank=True, null=True)),
                ('potassium', models.FloatField(blank=True, null=True)),
                ('potassium_dv', models.FloatField(blank=True, null=True)),
                ('totalcarbohydrate', models.FloatField(blank=True, null=True)),
                ('totalcarbohydrate_dv', models.FloatField(blank=True, null=True)),
                ('othercarbohydrates', models.FloatField(blank=True, null=True)),
                ('dietaryfiber', models.FloatField(blank=True, null=True)),
                ('dietaryfiber_dv', models.FloatField(blank=True, null=True)),
                ('sugar', models.FloatField(blank=True, null=True)),
                ('protein', models.FloatField(blank=True, null=True)),
                ('cholesterol', models.FloatField(blank=True, null=True)),
                ('vitamina', models.FloatField(blank=True, null=True)),
                ('vitamina_dv', models.FloatField(blank=True, null=True)),
                ('vitaminc', models.FloatField(blank=True, null=True)),
                ('vitaminc_dv', models.FloatField(blank=True, null=True)),
                ('vitamind', models.FloatField(blank=True, null=True)),
                ('vitamine', models.FloatField(blank=True, null=True)),
                ('niacin', models.FloatField(blank=True, null=True)),
                ('vitaminb6', models.FloatField(blank=True, null=True)),
                ('folacin', models.FloatField(blank=True, null=True)),
                ('folate', models.FloatField(blank=True, null=True)),
                ('vitaminb12', models.FloatField(blank=True, null=True)),
                ('pantothenicacid', models.FloatField(blank=True, null=True)),
                ('pantothenate', models.FloatField(blank=True, null=True)),
                ('alcohol', models.FloatField(blank=True, null=True)),
                ('erythritol', models.FloatField(blank=True, null=True)),
                ('glycerol', models.FloatField(blank=True, null=True)),
                ('isomalt', models.FloatField(blank=True, null=True)),
                ('lactitol', models.FloatField(blank=True, null=True)),
                ('maltitol', models.FloatField(blank=True, null=True)),
                ('mannitol', models.FloatField(blank=True, null=True)),
                ('polydextrose', models.FloatField(blank=True, null=True)),
                ('sorbitol', models.FloatField(blank=True, null=True)),
                ('xylitol', models.FloatField(blank=True, null=True)),
                ('iron', models.FloatField(blank=True, null=True)),
                ('iron_dv', models.FloatField(blank=True, null=True)),
                ('riboflavin', models.FloatField(blank=True, null=True)),
                ('selenium', models.FloatField(blank=True, null=True)),
                ('magnesium', models.FloatField(blank=True, null=True)),
                ('phosphorus', models.FloatField(blank=True, null=True)),
                ('thiamine', models.FloatField(blank=True, null=True)),
                ('zinc', models.FloatField(blank=True, null=True)),
                ('product', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='nutrition_facts', to='database.Product')),
            ],
            options={
                'verbose_name': 'Product Nutrition',
                'verbose_name_plural': 'Product Nutrition',
            },
        ),
        migrations.CreateModel(
            name='LoblawsProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('upc_list', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=300), blank=True, null=True, size=None)),
                ('api_data', django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True)),
                ('product', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='loblaws_product', to='database.Product')),
            ],
            options={
                'verbose_name': 'Loblaws Product',
                'verbose_name_plural': 'Loblaws Products',
            },
        ),
    ]
