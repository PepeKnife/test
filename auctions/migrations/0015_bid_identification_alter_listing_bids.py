# Generated by Django 4.1 on 2022-10-16 02:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0014_remove_listing_bids_remove_listing_watchlist_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='bid',
            name='identification',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='listing',
            name='bids',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='listing_bid', to='auctions.bid'),
        ),
    ]
