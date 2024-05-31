# Generated by Django 3.2 on 2024-03-31 03:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NFT',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, null=True)),
                ('description', models.CharField(max_length=100, null=True)),
                ('created_by', models.CharField(max_length=20, null=True)),
                ('creative_url', models.TextField(null=True)),
                ('is_active', models.BooleanField(null=True)),
                ('account_id', models.CharField(max_length=100, null=True)),
                ('nft_id', models.CharField(max_length=100, null=True)),
                ('created_on', models.DateTimeField(auto_now_add=True, null=True)),
                ('modified_on', models.DateTimeField(auto_now_add=True, null=True)),
            ],
            options={
                'db_table': 'nft',
            },
        ),
        migrations.CreateModel(
            name='Ownership',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('recipient_id', models.CharField(max_length=100, null=True)),
                ('created_on', models.DateTimeField(auto_now_add=True, null=True)),
                ('modified_on', models.DateTimeField(auto_now_add=True, null=True)),
                ('nft_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.nft')),
            ],
            options={
                'db_table': 'ownership',
            },
        ),
    ]
