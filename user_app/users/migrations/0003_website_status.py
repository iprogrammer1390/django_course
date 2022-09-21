# Generated by Django 4.1.1 on 2022-09-21 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_website'),
    ]

    operations = [
        migrations.AddField(
            model_name='website',
            name='status',
            field=models.CharField(choices=[('R', 'Reviewed'), ('N', 'Not reviewed'), ('E', 'Error'), ('A', 'Accepted')], default='R', max_length=1),
            preserve_default=False,
        ),
    ]