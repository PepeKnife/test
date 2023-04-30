# Generated by Django 4.1 on 2022-10-16 01:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0012_alter_listing_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listing',
            name='watchlist',
        ),
        migrations.AddField(
            model_name='listing',
            name='watchlist',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='user_watchlist', to=settings.AUTH_USER_MODEL),
        ),
    ]