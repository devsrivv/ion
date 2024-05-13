# Generated by Django 3.2.18 on 2023-08-16 16:43

from django.conf import settings
from django.db import migrations, models
import intranet.utils.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='EnrichmentActivity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=10000)),
                ('added', models.DateTimeField(auto_now=True)),
                ('time', models.DateTimeField(blank=True, null=True)),
                ('location', models.CharField(max_length=300)),
                ('capacity', models.SmallIntegerField(default=28)),
                ('presign', models.BooleanField(default=False)),
                ('attending', models.ManyToManyField(blank=True, related_name='enrichments_attending', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(null=True, on_delete=intranet.utils.deletion.set_historical_user, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['time'],
            },
        ),
    ]