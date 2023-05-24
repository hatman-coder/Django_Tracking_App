# Generated by Django 4.2.1 on 2023-05-24 15:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('TrackApi', '0006_remove_deviceassignment_device_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='DeviceUsageList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.RenameModel(
            old_name='PhoneCompany',
            new_name='DeviceBrand',
        ),
        migrations.RenameModel(
            old_name='DeviceAssignment',
            new_name='DeviceLog',
        ),
        migrations.DeleteModel(
            name='Device',
        ),
        migrations.AddField(
            model_name='deviceusagelist',
            name='device_log',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='device_usage_list', to='TrackApi.devicelog'),
        ),
        migrations.AddField(
            model_name='deviceusagelist',
            name='phone_company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TrackApi.devicebrand'),
        ),
    ]
