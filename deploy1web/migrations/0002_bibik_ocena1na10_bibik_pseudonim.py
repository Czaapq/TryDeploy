# Generated by Django 5.0 on 2023-12-14 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deploy1web', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bibik',
            name='ocena1na10',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=3, null=True),
        ),
        migrations.AddField(
            model_name='bibik',
            name='pseudonim',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]
