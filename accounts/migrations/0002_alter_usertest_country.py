# Generated by Django 3.2.7 on 2023-02-16 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usertest',
            name='country',
            field=models.CharField(choices=[('ja', '日本'), ('us', 'アメリカ'), ('uk', 'イギリス'), ('ch', '中国')], max_length=50, null=True, verbose_name='国籍'),
        ),
    ]
