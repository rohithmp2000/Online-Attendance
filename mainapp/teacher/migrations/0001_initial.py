# Generated by Django 4.1 on 2022-09-03 18:10

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
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('subject', models.CharField(blank=True, choices=[('1', 'Computer Science'), ('2', 'Physics'), ('3', 'Chemistry'), ('4', 'Biology'), ('5', 'Maths'), ('6', 'English')], max_length=1)),
                ('email', models.EmailField(max_length=254)),
                ('roletype', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='teacher', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]