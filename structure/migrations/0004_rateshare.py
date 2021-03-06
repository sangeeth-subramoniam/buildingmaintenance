# Generated by Django 3.2.5 on 2021-07-19 02:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('structure', '0003_auto_20210716_1639'),
    ]

    operations = [
        migrations.CreateModel(
            name='RateShare',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ProcessingYYYY', models.CharField(default='2021', max_length=4)),
                ('ProcessingMM', models.CharField(default='7', max_length=2)),
                ('Rate', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('Remarks', models.CharField(blank=True, max_length=200)),
                ('DeleteFlg', models.CharField(blank=True, max_length=1)),
                ('InsUserID', models.CharField(blank=True, default=None, max_length=20, null=True)),
                ('UpdUserID', models.CharField(blank=True, default=None, max_length=20, null=True)),
                ('UpdDate', models.DateTimeField(auto_now=True)),
                ('MeterID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='structure.metermaster')),
                ('StoreNO', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='structure.storemaster')),
            ],
            options={
                'unique_together': {('MeterID', 'StoreNO', 'ProcessingYYYY', 'ProcessingMM')},
            },
        ),
    ]
