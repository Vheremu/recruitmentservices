# Generated by Django 5.0.4 on 2024-08-15 13:46

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Vaccancy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vaccancyid', models.IntegerField(unique=True)),
                ('title', models.CharField(blank=True, max_length=100)),
                ('date_posted', models.DateTimeField()),
                ('expiry_date', models.DateTimeField()),
                ('recruiter', models.CharField(blank=True, max_length=100)),
                ('employmenttype', models.CharField(blank=True, max_length=100)),
                ('location', models.CharField(blank=True, max_length=100)),
                ('dutation', models.CharField(blank=True, max_length=100)),
                ('responsibilities', models.CharField(blank=True, max_length=500)),
                ('attributes', models.CharField(blank=True, max_length=300)),
                ('requirements', models.CharField(blank=True, max_length=500)),
                ('offer', models.CharField(blank=True, max_length=100)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
