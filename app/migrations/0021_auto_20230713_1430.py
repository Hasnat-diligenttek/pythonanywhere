# Generated by Django 3.2.19 on 2023-07-13 14:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0020_alter_appointment_address'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='apparence',
            options={'verbose_name_plural': '06. Theme Apparence'},
        ),
        migrations.AlterModelOptions(
            name='appointment',
            options={'verbose_name_plural': '03. Appointment'},
        ),
        migrations.AlterModelOptions(
            name='contact',
            options={'verbose_name_plural': '04. Contact'},
        ),
        migrations.AlterModelOptions(
            name='farm',
            options={'verbose_name_plural': '02. Farms'},
        ),
        migrations.AlterModelOptions(
            name='savechats',
            options={'verbose_name_plural': '05. Save Chats'},
        ),
        migrations.CreateModel(
            name='EmailVerified',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_email', models.EmailField(default='', max_length=254)),
                ('verify', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': '13. Email Verify',
            },
        ),
    ]