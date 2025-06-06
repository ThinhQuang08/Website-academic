# Generated by Django 5.0.4 on 2024-05-14 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site1', '0012_alter_fruit_classification'),
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('calories', models.IntegerField()),
                ('classification', models.CharField(choices=[('high_calories', 'Nhiều Calo'), ('low_calories', 'Ít Calo'), ('medium_calories', 'Calo Vừa Phải')], max_length=50)),
                ('image', models.ImageField(upload_to='foods_images/')),
            ],
        ),
    ]
