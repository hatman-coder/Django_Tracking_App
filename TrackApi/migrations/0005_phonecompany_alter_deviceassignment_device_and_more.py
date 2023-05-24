# Generated by Django 4.2.1 on 2023-05-24 10:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('TrackApi', '0004_alter_deviceassignment_employee'),
    ]

    operations = [
        migrations.CreateModel(
            name='PhoneCompany',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='deviceassignment',
            name='device',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='device', to='TrackApi.device'),
        ),
        migrations.AddField(
            model_name='device',
            name='phone_company',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='TrackApi.phonecompany'),
            preserve_default=False,
        ),
    ]
