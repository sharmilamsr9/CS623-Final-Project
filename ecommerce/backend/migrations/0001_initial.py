# Generated by Django 3.0.6 on 2021-11-10 11:52

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(default='New User', max_length=50)),
                ('last_name', models.CharField(default='New User', max_length=50)),
                ('phone', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=100)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'user_profile',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('description', models.TextField(max_length=2000)),
                ('color', models.CharField(max_length=50)),
                ('category', models.CharField(default='Something', max_length=255)),
                ('image', models.ImageField(upload_to='images/')),
                ('quantity', models.IntegerField(default=1)),
                ('created_at', models.DateTimeField(default=datetime.datetime.now)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'item',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=255)),
                ('subject', models.CharField(max_length=255)),
                ('message', models.CharField(max_length=2000)),
                ('created_at', models.DateTimeField(default=datetime.datetime.now)),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'contact_details',
                'managed': True,
            },
        ),
    ]
