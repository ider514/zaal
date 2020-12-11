# Generated by Django 3.1.3 on 2020-12-11 05:39

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
            name='Court',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(blank=True, max_length=200)),
                ('created_at', models.DateTimeField()),
                ('modified_at', models.DateTimeField()),
                ('category', models.CharField(choices=[('EX', 'Exclusive'), ('ST', 'Standart'), ('NI', 'Night'), ('NO', 'None')], default='NO', max_length=2)),
                ('rating', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=8)),
                ('password', models.CharField(max_length=50)),
                ('court', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='manager', to='main.court')),
            ],
        ),
        migrations.CreateModel(
            name='UserPaymentInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('method', models.CharField(choices=[('MO', 'Mobile'), ('CS', 'Cash'), ('CA', 'Card')], default='MO', max_length=2)),
                ('info', models.CharField(max_length=200)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'UserPaymentInfo',
            },
        ),
        migrations.CreateModel(
            name='UserLocation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('longitude', models.DecimalField(decimal_places=6, max_digits=9)),
                ('latitude', models.DecimalField(decimal_places=6, max_digits=9)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review', models.CharField(max_length=200)),
                ('rating', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('court', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.court')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Reservations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date_time', models.DateTimeField()),
                ('end_date_time', models.DateTimeField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('description', models.CharField(blank=True, max_length=200)),
                ('category', models.CharField(choices=[('FU', 'Full'), ('HA', 'Half')], default='FU', max_length=2)),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('cancellation_fee', models.DecimalField(decimal_places=2, max_digits=8)),
                ('cancelled_at', models.DateTimeField()),
                ('status', models.CharField(choices=[('PA', 'Paid'), ('UN', 'Unpaid'), ('CA', 'Cancelled')], default='UN', max_length=2)),
                ('payment_date_time', models.DateTimeField()),
                ('cancellation_date_time', models.DateTimeField()),
                ('court', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.court')),
                ('manager', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.manager')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Reservations',
            },
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('method', models.CharField(choices=[('MO', 'Mobile'), ('CS', 'Cash'), ('CA', 'Card')], default='MO', max_length=2)),
                ('date_time', models.DateTimeField(auto_now_add=True)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=8)),
                ('reservation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.reservations')),
            ],
        ),
        migrations.CreateModel(
            name='CourtPaymentInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('method', models.CharField(choices=[('MO', 'Mobile'), ('CS', 'Cash'), ('CA', 'Card')], default='MO', max_length=2)),
                ('info', models.CharField(max_length=200)),
                ('court', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.court')),
            ],
            options={
                'verbose_name_plural': 'CourtPaymentInfo',
            },
        ),
        migrations.CreateModel(
            name='CourtLocation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('longitude', models.DecimalField(decimal_places=6, max_digits=9)),
                ('latitude', models.DecimalField(decimal_places=6, max_digits=9)),
                ('court', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.court')),
            ],
        ),
        migrations.CreateModel(
            name='CourtFiles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
                ('court', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.court')),
            ],
            options={
                'verbose_name_plural': 'CourtFiles',
            },
        ),
        migrations.CreateModel(
            name='Calendar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timeline', models.IntegerField()),
                ('court', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.court')),
            ],
        ),
        migrations.CreateModel(
            name='Amenities',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amenitites', models.CharField(max_length=20)),
                ('court', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.court')),
            ],
            options={
                'verbose_name_plural': 'Amenities',
            },
        ),
    ]
