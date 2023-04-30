# Generated by Django 4.1 on 2022-10-20 01:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0017_comment_listing'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='listing',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='listing_comment', to='auctions.listing'),
        ),
    ]
