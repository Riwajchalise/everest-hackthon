# Generated by Django 2.0.3 on 2019-07-19 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20180609_0258'),
    ]

    operations = [
        migrations.CreateModel(
            name='Desktops',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=200)),
                ('price', models.IntegerField()),
                ('status', models.CharField(choices=[('AVAILABLE', 'Item ready to be purchased'), ('SOLD', 'Item already purchased'), ('RESTOCKING', 'Item restocking in few days')], default='SOLD', max_length=10)),
                ('issues', models.CharField(default='No Issues', max_length=50)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Laptops',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=200)),
                ('price', models.IntegerField()),
                ('status', models.CharField(choices=[('AVAILABLE', 'Item ready to be purchased'), ('SOLD', 'Item already purchased'), ('RESTOCKING', 'Item restocking in few days')], default='SOLD', max_length=10)),
                ('issues', models.CharField(default='No Issues', max_length=50)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Mobiles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=200)),
                ('price', models.IntegerField()),
                ('status', models.CharField(choices=[('AVAILABLE', 'Item ready to be purchased'), ('SOLD', 'Item already purchased'), ('RESTOCKING', 'Item restocking in few days')], default='SOLD', max_length=10)),
                ('issues', models.CharField(default='No Issues', max_length=50)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.DeleteModel(
            name='products',
        ),
    ]