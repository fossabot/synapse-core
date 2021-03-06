# Generated by Django 2.0.8 on 2018-10-26 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transfer', '0004_transferfile_retries'),
    ]

    operations = [
        migrations.AddField(
            model_name='transferbatch',
            name='status',
            field=models.CharField(choices=[('PD', 'pending'), ('RN', 'running'), ('ER', 'complete with errors'), ('CP', 'complete')], default='PD', max_length=2),
        ),
        migrations.AlterField(
            model_name='transferfile',
            name='status',
            field=models.CharField(choices=[('PD', 'pending'), ('DL', 'downloading'), ('DF', 'download failed'), ('DS', 'download succeeded'), ('UP', 'uploading'), ('UF', 'upload failed'), ('US', 'upload succeeded'), ('CP', 'complete')], default='PD', max_length=2),
        ),
    ]
