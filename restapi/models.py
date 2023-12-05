from typing import Any
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Me(models.Model):
    first_name = models.CharField(max_length=100, verbose_name="Имя", help_text="Введите ваше имя")
    
    last_name = models.CharField(max_length=100, verbose_name="Фамилия", help_text="Введите вашу фамилию")
    
    email = models.EmailField(verbose_name="Email", help_text="Введите ваш email")
    
    phone = models.CharField(max_length=20, verbose_name="Телефон", help_text="Введите ваш телефон")
    
    instagram = models.URLField(max_length=100, verbose_name="Instagram", help_text="Введите ваш Instagram", blank=True, null=True)
    
    github = models.URLField(max_length=100, verbose_name="Github", help_text="Введите ваш Github", blank=True, null=True)

    linkedin = models.URLField(max_length=100, verbose_name="Linkedin", help_text="Введите ваш Linkedin", blank=True, null=True)

    telegram = models.URLField(max_length=100, verbose_name="Telegram", help_text="Введите ваш Telegram", blank=True, null=True)
    
    education = models.TextField(verbose_name="Образование", help_text="Введите образование", blank=True, null=True)
    
    work_history = models.TextField(verbose_name="История работы", help_text="Введите историю работы", blank=True, null=True)
    
    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"
    
    class Meta:
        verbose_name = "Обо мне"
        verbose_name_plural = "Обо мне"
        
class Project(models.Model):
    file = models.FileField(upload_to="project_file/", help_text="Загрузите файл", blank=True, null=True)    

    image = models.ImageField(upload_to="project_image/", help_text="Загрузите изображение", blank=True, null=True)
    
    title = models.CharField(max_length=100, verbose_name="Название", help_text="Введите название проекта")
    
    description = models.TextField(verbose_name="Описание", help_text="Введите описание проекта")
    
    start_date = models.DateField(verbose_name="Дата начала", help_text="Введите дату начала")
    
    end_date = models.DateField(verbose_name="Дата окончания", help_text="Введите дату окончания", blank=True, null=True)
    
    url = models.URLField(verbose_name="Ссылка на проект", help_text="Введите URL проекта", blank=True, null=True)
    
    repository = models.URLField(verbose_name="Github репозиторий", help_text="Введите URL репозитория", blank=True, null=True)

    technologies = models.CharField(max_length=100, verbose_name="Используемые технологии", help_text="Выберите технологии", blank=True, null=True)
    
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата последнего обновления")
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Проект"
        verbose_name_plural = "Проекты"
        ordering = ["-created_at"]
        
class Skill(models.Model):
    CATEGORY_CHOICES = [
        ("programming", "Программирование"),
        ("design", "Дизайн"),
        ('languages', 'Языки программирования'),
        ('database', 'Базы данных'),
        ('frameworks', 'Фреймворки'),
        ('tools', 'Инструменты разработки'),
        ('soft_skills', 'Soft Skills'),
        ('web', 'Веб-разработка'),
        ('mobile', 'Мобильная разработка'),
        ('cloud', 'Облачные технологии'),
        ('testing', 'Тестирование и QA'),
        ('analytics', 'Аналитика данных'),
        ('machine_learning', 'Машинное обучение и искусственный интеллект'),
        ('security', 'Информационная безопасность'),
        ('networking', 'Сетевые технологии'),
        ('graphics', 'Графический дизайн'),
        ('audio_video', 'Аудио и видео производство'),
        ('project_management', 'Управление проектами'),
        ('communication', 'Коммуникационные навыки'),
        ('leadership', 'Лидерство'),
        ('entrepreneurship', 'Предпринимательство'),
        ('data_science', 'Наука о данных'),
        ('automation', 'Автоматизация процессов'),
        ('devops', 'DevOps'),
        ('blockchain', 'Блокчейн технологии'),
        ('robotics', 'Робототехника'),
        ('language', 'Языки'),
    ]
    
    category = models.CharField(max_length=100, verbose_name="Категория", help_text="Выберите категорию", choices=CATEGORY_CHOICES)
    
    name = models.CharField(max_length=100, verbose_name="Название навыка", help_text="Введите название навыка")
    
    percentage = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(100)], verbose_name="Проценты", help_text="Введите уровень в процентах"
    )
    
    def __str__(self) -> str:
        return f"{self.name} ({self.percentage}%)"
    
    class Meta:
        verbose_name = "Навык"
        verbose_name_plural = "Навыки"
        
class Pricing(models.Model):
    service = models.CharField(max_length=100, verbose_name="Услуга", help_text="Введите название услуги")
    description = models.TextField(verbose_name="Описание", help_text="Введите краткое описание услуги")
    
    rate_per_hour = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Ставка в час ($)", help_text="Укажите ставку в долларах за час работы")
    
    estimated_hours = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Оценочное время работы(часы)", help_text="Укажите сколько часов нужно на услугу")
    
    def total_cost(self):
        """
        Метод total_cost вычисляет общую стоимость на основе почасовой ставки и расчётных часов.
        """
        return self.rate_per_hour * self.estimated_hours
    
    def __str__(self):
        return f"{self.service} - {self.total_cost()}"
    
    class Meta:
        verbose_name = "Цена"
        verbose_name_plural = "Цены"
        
class Contact(models.Model):
    name = models.CharField(max_length=100, verbose_name="Имя", help_text="Введите ваше имя")
    
    email = models.EmailField(verbose_name="Email", help_text="Введите ваш email")
    
    subject = models.CharField(max_length=200, verbose_name="Тема", help_text="Введите тему сообщения")
    
    message = models.TextField(verbose_name="Сообщение", help_text="Введите сообщение")
    
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    
    is_read = models.BooleanField(default=False, verbose_name="Прочитано")
    
    def __str__(self):
        return f"{self.subject} - {self.name} - {self.email}"
    
    class Meta:
        verbose_name = "Контакт"
        verbose_name_plural = "Контакты"