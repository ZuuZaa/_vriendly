# Generated by Django 3.1.2 on 2020-11-11 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_auto_20201111_0927'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='last_logout',
            field=models.DateTimeField(null=True),
        ),
    ]
