# Generated by Django 3.1.2 on 2020-11-18 09:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20201015_1240'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Manager_ID',
            new_name='Master_IP',
        ),
        migrations.AlterModelOptions(
            name='master_ip',
            options={'verbose_name': 'Master IP', 'verbose_name_plural': 'Master IP'},
        ),
        migrations.RenameField(
            model_name='master_ip',
            old_name='manager_id',
            new_name='master_IP',
        ),
        migrations.AddField(
            model_name='myapp',
            name='master_IP',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.master_ip'),
        ),
    ]