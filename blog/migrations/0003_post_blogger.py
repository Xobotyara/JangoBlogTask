# Generated by Django 3.0 on 2019-12-14 16:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_blogger'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='blogger',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='blog.Blogger'),
        ),
    ]
