# Generated by Django 4.2.1 on 2023-05-31 04:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_customaccount_groups_customaccount_is_superuser_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customaccount',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
    ]
