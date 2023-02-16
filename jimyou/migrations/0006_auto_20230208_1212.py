# Generated by Django 3.2.7 on 2023-02-08 03:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jimyou', '0005_goodtest_lesson_unique'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='goodtest',
            name='lesson_unique',
        ),
        migrations.AddConstraint(
            model_name='goodtest',
            constraint=models.UniqueConstraint(fields=('target', 'user'), name='good_unique'),
        ),
    ]
