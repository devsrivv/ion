# Generated by Django 3.2.18 on 2023-06-02 04:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('announcements', '0029_alter_warningannouncement_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='warningannouncement',
            name='type',
            field=models.CharField(choices=[('login', 'Login Warning (displays on login page)'), ('dashboard_login', 'Dashboard and Login Warning (displays on dashboard and login pages)'), ('dashboard', 'Dashboard Warning (displays on dashboard)'), ('global', 'Global Warning (displays on all pages)')], max_length=31),
        ),
    ]