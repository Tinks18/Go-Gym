# Generated by Django 3.2.16 on 2023-02-02 21:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gymtrainer', '0012_auto_20230202_2102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gymslot',
            name='event_date',
            field=models.CharField(max_length=120, verbose_name='Event Date'),
        ),
    ]