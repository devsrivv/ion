# Generated by Django 3.2.25 on 2024-03-23 23:35

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('enrichment', '0003_auto_20240307_2313'),
    ]

    operations = [
        migrations.AddField(
            model_name='enrichmentactivity',
            name='attended',
            field=models.ManyToManyField(blank=True, related_name='enrichments_attended', to=settings.AUTH_USER_MODEL),
        ),
    ]