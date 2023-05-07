# Generated by Django 3.1.1 on 2023-03-17 16:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='KunciJawaban',
            fields=[
                ('nomor', models.IntegerField(default=1, primary_key=True, serialize=False)),
                ('kunci', models.TextField(blank=True, null=True)),
                ('bobot', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Siswa',
            fields=[
                ('nomor', models.IntegerField(default=1, primary_key=True, serialize=False)),
                ('nama', models.TextField(blank=True, null=True)),
                ('nilai', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='JawabanSiswa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jawaban', models.TextField(blank=True, null=True)),
                ('noSiswa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scoring.siswa')),
                ('noSoal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scoring.kuncijawaban')),
            ],
        ),
    ]