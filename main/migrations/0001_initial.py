# Generated by Django 4.1.7 on 2023-03-14 09:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_cryptography.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PrivateKey',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('key', django_cryptography.fields.encrypt(models.CharField(max_length=64))),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ETHAddress',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('address', django_cryptography.fields.encrypt(models.CharField(max_length=64))),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
                ('private_key', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='main.privatekey')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='BTCAddress',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('address', django_cryptography.fields.encrypt(models.CharField(max_length=64))),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
                ('private_key', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='main.privatekey')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]