# Generated by Django 4.2.7 on 2023-11-20 11:55

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Введите ваше имя', max_length=100, verbose_name='Имя')),
                ('email', models.EmailField(help_text='Введите ваш email', max_length=254, verbose_name='Email')),
                ('subject', models.CharField(help_text='Введите тему сообщения', max_length=200, verbose_name='Тема')),
                ('message', models.TextField(help_text='Введите сообщение', verbose_name='Сообщение')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('is_read', models.BooleanField(default=False, verbose_name='Прочитано')),
            ],
            options={
                'verbose_name': 'Контакт',
                'verbose_name_plural': 'Контакты',
            },
        ),
        migrations.CreateModel(
            name='Me',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(help_text='Введите ваше имя', max_length=100, verbose_name='Имя')),
                ('last_name', models.CharField(help_text='Введите вашу фамилию', max_length=100, verbose_name='Фамилия')),
                ('email', models.EmailField(help_text='Введите ваш email', max_length=254, verbose_name='Email')),
                ('phone', models.CharField(help_text='Введите ваш телефон', max_length=20, verbose_name='Телефон')),
                ('instagram', models.URLField(blank=True, help_text='Введите ваш Instagram', max_length=100, null=True, verbose_name='Instagram')),
                ('github', models.URLField(blank=True, help_text='Введите ваш Github', max_length=100, null=True, verbose_name='Github')),
                ('linkedin', models.URLField(blank=True, help_text='Введите ваш Linkedin', max_length=100, null=True, verbose_name='Linkedin')),
                ('telegram', models.URLField(blank=True, help_text='Введите ваш Telegram', max_length=100, null=True, verbose_name='Telegram')),
                ('education', models.TextField(blank=True, help_text='Введите образование', null=True, verbose_name='Образование')),
                ('work_history', models.TextField(blank=True, help_text='Введите историю работы', null=True, verbose_name='История работы')),
            ],
            options={
                'verbose_name': 'Обо мне',
                'verbose_name_plural': 'Обо мне',
            },
        ),
        migrations.CreateModel(
            name='Pricing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service', models.CharField(help_text='Введите название услуги', max_length=100, verbose_name='Услуга')),
                ('description', models.TextField(help_text='Введите краткое описание услуги', verbose_name='Описание')),
                ('rate_per_hour', models.DecimalField(decimal_places=2, help_text='Укажите ставку в долларах за час работы', max_digits=10, verbose_name='Ставка в час ($)')),
                ('estimated_hours', models.DecimalField(decimal_places=2, help_text='Укажите сколько часов нужно на услугу', max_digits=5, verbose_name='Оценочное время работы(часы)')),
            ],
            options={
                'verbose_name': 'Цена',
                'verbose_name_plural': 'Цены',
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(blank=True, help_text='Загрузите файл', null=True, upload_to='project_file/')),
                ('image', models.ImageField(blank=True, help_text='Загрузите изображение', null=True, upload_to='project_image/')),
                ('title', models.CharField(help_text='Введите название проекта', max_length=100, verbose_name='Название')),
                ('description', models.TextField(help_text='Введите описание проекта', verbose_name='Описание')),
                ('start_date', models.DateField(help_text='Введите дату начала', verbose_name='Дата начала')),
                ('end_date', models.DateField(blank=True, help_text='Введите дату окончания', null=True, verbose_name='Дата окончания')),
                ('url', models.URLField(blank=True, help_text='Введите URL проекта', null=True, verbose_name='Ссылка на проект')),
                ('repository', models.URLField(blank=True, help_text='Введите URL репозитория', null=True, verbose_name='Github репозиторий')),
                ('technologies', models.CharField(blank=True, help_text='Выберите технологии', max_length=100, null=True, verbose_name='Используемые технологии')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата последнего обновления')),
            ],
            options={
                'verbose_name': 'Проект',
                'verbose_name_plural': 'Проекты',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('programming', 'Программирование'), ('design', 'Дизайн'), ('languages', 'Языки программирования'), ('database', 'Базы данных'), ('frameworks', 'Фреймворки'), ('tools', 'Инструменты разработки'), ('soft_skills', 'Soft Skills'), ('web', 'Веб-разработка'), ('mobile', 'Мобильная разработка'), ('cloud', 'Облачные технологии'), ('testing', 'Тестирование и QA'), ('analytics', 'Аналитика данных'), ('machine_learning', 'Машинное обучение и искусственный интеллект'), ('security', 'Информационная безопасность'), ('networking', 'Сетевые технологии'), ('graphics', 'Графический дизайн'), ('audio_video', 'Аудио и видео производство'), ('project_management', 'Управление проектами'), ('communication', 'Коммуникационные навыки'), ('leadership', 'Лидерство'), ('entrepreneurship', 'Предпринимательство'), ('data_science', 'Наука о данных'), ('automation', 'Автоматизация процессов'), ('devops', 'DevOps'), ('blockchain', 'Блокчейн технологии'), ('robotics', 'Робототехника'), ('language', 'Языки')], help_text='Выберите категорию', max_length=100, verbose_name='Категория')),
                ('name', models.CharField(help_text='Введите название навыка', max_length=100, verbose_name='Название навыка')),
                ('percentage', models.PositiveSmallIntegerField(help_text='Введите уровень в процентах', validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='Проценты')),
            ],
            options={
                'verbose_name': 'Навык',
                'verbose_name_plural': 'Навыки',
            },
        ),
    ]
