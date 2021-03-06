# Generated by Django 2.2.6 on 2019-10-16 05:08

from django.db import migrations, models
import django.utils.timezone
import register.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email address')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('nick_name', models.CharField(max_length=30, verbose_name='ニックネーム')),
                ('image', models.ImageField(blank=True, upload_to='media/', verbose_name='トップ画像')),
                ('twitter', models.URLField(blank=True, verbose_name='Twitterアカウント')),
                ('instagram', models.URLField(blank=True, max_length=150, verbose_name='Instagramアカウント')),
                ('skill', models.CharField(blank=True, choices=[('1', 'Webデザイナー'), ('2', 'PG(フロントサイド)'), ('3', 'PG(サーバーサイド)'), ('4', 'デザイナー'), ('5', 'フォトグラファー'), ('6', 'イラストレーター'), ('7', 'ライター'), ('8', 'ブロガー')], max_length=150, verbose_name='スキル')),
                ('area', models.CharField(choices=[('1', 'オンライン'), ('2', '北海道'), ('3', '青森県'), ('4', '岩手県'), ('5', '宮城県'), ('6', '秋田県'), ('7', '山形県'), ('8', '福島県'), ('9', '茨城県'), ('10', '栃木県'), ('11', '群馬県'), ('12', '埼玉県'), ('13', '千葉県'), ('14', '東京都'), ('15', '神奈川県'), ('16', '新潟県'), ('17', '富山県'), ('18', '石川県'), ('19', '福井県'), ('20', '山梨県'), ('21', '長野県'), ('22', '岐阜県'), ('23', '静岡県'), ('24', '愛知県'), ('25', '三重県'), ('26', '滋賀県'), ('27', '京都府'), ('28', '大阪府'), ('29', '兵庫県'), ('30', '奈良県'), ('31', '和歌山県'), ('32', '鳥取県'), ('33', '島根県'), ('34', '岡山県'), ('35', '広島県'), ('36', '山口県'), ('37', '徳島県'), ('38', '香川県'), ('39', '愛媛県'), ('40', '高知県'), ('41', '福岡県'), ('42', '佐賀県'), ('43', '長崎県'), ('44', '熊本県'), ('45', '大分県'), ('46', '宮崎県'), ('47', '鹿児島県'), ('48', '沖縄県')], max_length=150, verbose_name='活動範囲')),
                ('request_fee', models.CharField(choices=[('1', '応相談'), ('2', '無料'), ('3', '〜10,000円'), ('4', '10,000円〜'), ('5', '50,000円〜'), ('6', '100,000円〜'), ('7', '500,000円〜')], max_length=20, verbose_name='依頼料')),
                ('portfolio', models.CharField(blank=True, max_length=150, verbose_name='ポートフォリオ')),
                ('self_introduction', models.CharField(blank=True, max_length=500, verbose_name='自己PR')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
            managers=[
                ('objects', register.models.UserManager()),
            ],
        ),
    ]
