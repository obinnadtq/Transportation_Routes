# Generated by Django 3.2.2 on 2021-06-03 12:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('transport', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Station',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
                ('accessible', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Stop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stop_number', models.PositiveIntegerField()),
                ('line', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='transport.line')),
                ('station', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='transport.station')),
            ],
            options={
                'unique_together': {('line', 'stop_number')},
            },
        ),
    ]
