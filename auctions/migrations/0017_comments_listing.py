# Generated by Django 5.1 on 2024-09-30 06:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0016_remove_comments_listing'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='listing',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='auctions.auction_listings'),
        ),
    ]
