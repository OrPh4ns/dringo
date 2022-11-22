# Generated by Django 4.1.3 on 2022-11-22 21:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('hospital', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Emergency',
            fields=[
                ('case_id', models.IntegerField(primary_key=True, serialize=False)),
                ('created_dt', models.DateTimeField(auto_now_add=True)),
                ('hospital', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='emergencies', to='hospital.hospital')),
            ],
        ),
    ]
