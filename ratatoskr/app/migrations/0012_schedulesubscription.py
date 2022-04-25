# Generated by Django 3.2.12 on 2022-04-11 14:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0011_rename_uuid_reservation_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='ScheduleSubscription',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('schedule', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.schedule')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
