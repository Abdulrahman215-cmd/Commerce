# Generated by Django 5.1 on 2024-10-17 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0027_alter_auction_listings_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auction_listings',
            name='category',
            field=models.CharField(choices=[('Toys', 'Toys'), ('Armor', 'Armor'), ('Weapons', 'Weapons'), ('Body Powered Devices', 'Body Powered Devices'), ('Treasure', 'Treasure')], max_length=100),
        ),
    ]
