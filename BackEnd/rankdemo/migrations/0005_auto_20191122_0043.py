# Generated by Django 2.2.7 on 2019-11-21 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rankdemo', '0004_auto_20191122_0039'),
    ]

    operations = [
        migrations.AddField(
            model_name='rank',
            name='score',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='rank',
            name='userclearence',
            field=models.IntegerField(choices=[(1, 'Normal'), (2, 'VIP'), (3, 'SVIP')], default=1),
        ),
        migrations.AddField(
            model_name='rank',
            name='username',
            field=models.CharField(default='Unknown', max_length=32),
        ),
        migrations.DeleteModel(
            name='Scores',
        ),
        migrations.DeleteModel(
            name='Userinfo',
        ),
    ]