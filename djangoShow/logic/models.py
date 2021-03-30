from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


class Rank(models.TextChoices):
    """Звания, которые могут быть у курируемых"""
    ONE = '01', _('Рядовой соботыльник')
    TWO = '02', _('Младший сержант бота')
    THREE = '03', _('Сержант олимпиад')
    FOUR = '04', _('Старшина перечней')
    FIVE = '05', _('Товарищ прапорщик')
    SIX = '06', _('Старший соботыльник')
    SEVEN = '07', _('Лейтенант учёбы')
    EIGHT = '08', _('Капитан региона')
    NINE = '09', _('Майор тайм-менеджмента')
    TEN = '10', _('Полковник-бвишник')
    ELEVEN = '11', _('Генерал всерос(с)а')
    TWELVE = '12', _('Магистр книг и пособий')
    THIRTEEN = '13', _('Повелитель бота')
    FOURTEEN = '14', _('Император всея Бота и Учёбы')


class WeekDay(models.TextChoices):
    """День недели"""
    MONDAY = '1', _('понедельник')
    TUESDAY = '2', _('вторник')
    WEDNESDAY = '3', _('среда')
    THURSDAY = '4', _('четверг')
    FRIDAY = '5', _('пятница')
    SATURDAY = '6', _('суббота')
    SUNDAY = '7', _('воскресенье')


class Group(models.TextChoices):
    """Группа"""
    PRO = 'P', _('Pro')
    LITE = 'L', _('Lite')


class CuratorProfile(models.Model):
    """
        Профиль куратора (для того, чтобы не возится с User тут лежит вся нужная инфа)
        user.username - ник в телеге (обязательное поле)
        user.first_name - имя
        user.last_name - фамилия
        user.email - мыло (хз зачем, но оно есть)
        user.password - хэш и метаданные о пароле (обязательное поле)
        user.is_staff - булево, показывает, что это куратор
        user.is_active - булево, позволяет банить учетки (не перманентно)
        user.is_superuser - не трогать, на будующее
        user.last_login - не трогать, на будующее
        user.date_joined - дата создания аккаунта
    """

    notes = models.TextField('заметки', blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='сuratorProfile', null=True)

    def __str__(self):
        return f'{self.user.username} {self.user.get_full_name()}'

    class Meta:
        verbose_name = 'Куратор'
        verbose_name_plural = 'Кураторы'


class PadawanProfile(models.Model):
    """
        Профиль человека (для того, чтобы не возится с User тут лежит вся нужная инфа)
        user.username - ник в телеге (обязательное поле)
        user.first_name - имя
        user.last_name - фамилия
        user.email - мыло (хз зачем, но оно есть)
        user.password - хэш и метаданные о пароле (обязательное поле)
        user.is_staff - булево, показывает, что это куратор
        user.is_active - булево, позволяет банить учетки (не перманентно)
        user.is_superuser - не трогать, на будующее
        user.last_login - показывает время последних действий (для чека подъема)
        user.date_joined - дата создания аккаунта
    """

    telephone = models.CharField('телефон', max_length=16, blank=True)
    notes = models.TextField('заметки', blank=True)
    rank = models.CharField('звание', choices=Rank.choices, default=Rank.ONE, max_length=2)
    off_date = models.DateField('окончание оплаченного периода', auto_now=True)
    weekend = models.CharField('выходной', choices=WeekDay.choices, default=WeekDay.SUNDAY, max_length=1)
    group = models.CharField('группа', choices=Group.choices, default=Group.LITE, max_length=1)
    utc = models.IntegerField('временной сдвиг', default=3, validators=[MinValueValidator(-12), MaxValueValidator(12)])
    rating = models.IntegerField('рейтинг', default=0, validators=[MinValueValidator(-20)])
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='padawanProfile', null=True)
    curator = models.ForeignKey(CuratorProfile, on_delete=models.SET_NULL, related_name='padawans', null=True)

    def __str__(self):
        return self.user.get_full_name()

    class Meta:
        verbose_name = 'Подаван'
        verbose_name_plural = 'Подваны'
        ordering = ["-off_date"]


class Code(models.Model):

    days = models.IntegerField('время', default=0, validators=[MinValueValidator(0)])
    activations = models.IntegerField('активации', default=0, validators=[MinValueValidator(0)])
    text = models.SlugField('текст')
    users = models.ManyToManyField(PadawanProfile, blank=True, related_name='activatedCodes')

    def __str__(self) -> str:
        return f'{self.text} на {self.days} сталось: {self.activations - len(self.users.all())}'

    class Meta:
        verbose_name = 'Код'
        verbose_name_plural = 'Коды'
        ordering = ["-days"]
