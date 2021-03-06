# Generated by Django 2.0.3 on 2018-03-10 13:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lastname', models.CharField(max_length=45)),
                ('firstname', models.CharField(max_length=45)),
                ('birthdaydate', models.DateField()),
                ('weight', models.IntegerField(blank=True, null=True)),
                ('picture', models.TextField(blank=True, null=True)),
                ('email', models.CharField(max_length=255)),
                ('phone', models.CharField(blank=True, max_length=45, null=True)),
                ('adress1', models.CharField(blank=True, db_column='Adress1', max_length=255, null=True)),
                ('adress2', models.CharField(blank=True, db_column='Adress2', max_length=255, null=True)),
                ('np', models.CharField(blank=True, max_length=45, null=True)),
                ('city', models.CharField(blank=True, max_length=255, null=True)),
                ('created_at', models.DateTimeField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'contacts',
            },
        ),
        migrations.CreateModel(
            name='Countries',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, max_length=45, null=True)),
                ('created_at', models.DateTimeField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'countries',
            },
        ),
        migrations.CreateModel(
            name='Titles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=45)),
                ('created_at', models.DateTimeField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'titles',
            },
        ),
        migrations.AddField(
            model_name='contacts',
            name='country',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='office.Countries'),
        ),
        migrations.AddField(
            model_name='contacts',
            name='title',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='office.Titles'),
        ),
    ]
