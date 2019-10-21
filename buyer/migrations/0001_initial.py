# Generated by Django 2.2.5 on 2019-10-07 06:37

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('generic', '0001_initial'),
        ('authjwt', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default=None, max_length=50, null=True, verbose_name='Receiver')),
                ('mobile', models.CharField(blank=True, default=None, max_length=20, null=True, verbose_name='Mobile')),
                ('area', models.CharField(blank=True, default=None, max_length=30, null=True, verbose_name='Area')),
                ('text', models.TextField(verbose_name='Address')),
            ],
        ),
        migrations.CreateModel(
            name='Buyer',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('authjwt.baseuser',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default=None, max_length=40, null=True, verbose_name='Name')),
                ('avatar', models.OneToOneField(blank=True, default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='generic.Image', verbose_name='Avatar')),
                ('now_addr', models.OneToOneField(blank=True, default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='buyer.Address', verbose_name='Current Address')),
                ('owner', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='address',
            name='owner',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='addresses', to='buyer.Profile', verbose_name='Owner'),
        ),
    ]