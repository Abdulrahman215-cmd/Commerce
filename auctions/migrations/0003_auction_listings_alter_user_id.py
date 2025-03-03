# Generated by Django 5.1 on 2024-09-26 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0002_alter_user_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='auction_listings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('image_url', models.URLField()),
                ('description', models.TextField()),
                ('category', models.CharField(choices=[('ELEC', 'Electronic'), ('TY', 'Toys'), ('ARM', 'Armour'), ('WEAP', 'Weapons'), ('BPD', 'Body Powered Devices')], max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
