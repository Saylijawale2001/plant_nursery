# Generated by Django 4.2.4 on 2024-01-13 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_alter_product_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlantSeeds',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('selling_price', models.FloatField()),
                ('discounted_price', models.FloatField()),
                ('description', models.TextField()),
                ('brand', models.CharField(max_length=100)),
                ('category', models.CharField(choices=[('VS', 'Vegitable Seeds'), ('FS', 'Flower Seeds'), ('OS', 'Organic Seeds'), ('HS', 'Herbs seeds')], max_length=2)),
                ('product_image', models.ImageField(upload_to='productimg')),
            ],
        ),
    ]
