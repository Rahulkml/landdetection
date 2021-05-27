# Generated by Django 2.2.19 on 2021-05-15 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landsearch', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='revenuedetail',
            name='land',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='revenuedetail',
            name='land_type',
            field=models.CharField(choices=[('a', 'Thengu'), ('b', 'Kavungu'), ('c', 'Kurumulaku'), ('d', 'Kashumavu'), ('e', 'Others'), ('f', 'Palliyal')], help_text='Select the district', max_length=1),
        ),
    ]