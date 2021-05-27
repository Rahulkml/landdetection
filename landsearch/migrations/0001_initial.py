# Generated by Django 2.2.19 on 2021-05-15 07:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FamMember',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('maritial_status', models.CharField(choices=[('s', 'Single'), ('m', 'Married')], help_text='Choose your maritial status.', max_length=1)),
                ('relation', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('job', models.CharField(max_length=100)),
                ('income', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='LookUp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('district', models.CharField(max_length=100)),
                ('a', models.FloatField()),
                ('b', models.FloatField()),
                ('c', models.FloatField()),
                ('d', models.FloatField()),
                ('e', models.FloatField()),
                ('f', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='RationCard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_no', models.CharField(max_length=20)),
                ('house_name', models.CharField(max_length=200)),
                ('place', models.CharField(max_length=200)),
                ('pin_no', models.IntegerField()),
                ('taluk', models.CharField(max_length=100)),
                ('district', models.CharField(blank=True, choices=[('AL', 'Alappuzha'), ('ER', 'Ernakulam'), ('ID', 'Idukk'), ('KN', 'Kannur'), ('KS', 'Kasaragod'), ('KL', 'Kollam'), ('KT', 'Kottayam'), ('KZ', 'Kozhikode'), ('MA', 'Malappuram'), ('PL', 'Palakkad'), ('PT', 'Pathanamthitta'), ('TV', 'Thiruvananthapuram'), ('TS', 'Thrissur'), ('WA', 'Wayanad')], help_text='Select the district', max_length=2)),
                ('Card_Type', models.CharField(blank=True, choices=[('y', 'Yellow Card'), ('p', 'Pink Card'), ('b', 'Blue Card'), ('w', 'White Card')], default='w', help_text='The type of the card', max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='RevenueDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('land', models.IntegerField()),
                ('district', models.CharField(choices=[('AL', 'Alappuzha'), ('ER', 'Ernakulam'), ('ID', 'Idukk'), ('KN', 'Kannur'), ('KS', 'Kasaragod'), ('KL', 'Kollam'), ('KT', 'Kottayam'), ('KZ', 'Kozhikode'), ('MA', 'Malappuram'), ('PL', 'Palakkad'), ('PT', 'Pathanamthitta'), ('TV', 'Thiruvananthapuram'), ('TS', 'Thrissur'), ('WA', 'Wayanad')], help_text='Select the district', max_length=2)),
                ('land_type', models.CharField(choices=[('a', 'Thengu'), ('b', 'Kavungu'), ('c', 'Kurukulaku'), ('d', 'Kashumavu'), ('e', 'Others'), ('f', 'Palliyal')], help_text='Select the district', max_length=1)),
                ('name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='landsearch.FamMember')),
            ],
        ),
        migrations.AddField(
            model_name='fammember',
            name='card',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='landsearch.RationCard'),
        ),
    ]
