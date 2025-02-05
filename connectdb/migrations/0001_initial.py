# Generated by Django 5.0.6 on 2024-09-29 10:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LogType',
            fields=[
                ('log_id', models.AutoField(primary_key=True, serialize=False)),
                ('log_type', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='RFIDTag',
            fields=[
                ('rfidTag_id', models.AutoField(primary_key=True, serialize=False)),
                ('tag_type', models.CharField(max_length=50)),
                ('issue_date', models.DateTimeField()),
                ('expiry_time', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Sector',
            fields=[
                ('sector_id', models.AutoField(primary_key=True, serialize=False)),
                ('sector_name', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Logs',
            fields=[
                ('logs_id', models.AutoField(primary_key=True, serialize=False)),
                ('time_in', models.DateTimeField()),
                ('time_out', models.DateTimeField()),
                ('log_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='connectdb.logtype')),
            ],
        ),
        migrations.CreateModel(
            name='Personnel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('f_name', models.CharField(max_length=50)),
                ('l_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.CharField(max_length=255)),
                ('contact_number', models.CharField(max_length=20)),
                ('rfid_tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='connectdb.rfidtag')),
            ],
        ),
        migrations.AddField(
            model_name='logtype',
            name='rfid_tag',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='connectdb.rfidtag'),
        ),
        migrations.AddField(
            model_name='rfidtag',
            name='sector',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='connectdb.sector'),
        ),
        migrations.CreateModel(
            name='Visitors',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('f_name', models.CharField(max_length=50)),
                ('l_name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=255)),
                ('contact_number', models.CharField(max_length=20)),
                ('rfid_tags', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='connectdb.rfidtag')),
                ('sector', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='connectdb.sector')),
            ],
        ),
    ]
