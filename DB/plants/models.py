from django.db import models

class Plants(models.Model):
    title = models.CharField('Название', max_length=100)
    age = models.IntegerField('Возраст')
    date = models.DateField('Дата высадки')
    type = models.CharField('Tип',max_length=1000)

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return f'/plants'
    class Meta:
        verbose_name ='Растение'
        verbose_name_plural = 'Растения'


class Irrigation(models.Model):

    plant = models.OneToOneField(Plants, on_delete=models.CASCADE,verbose_name ='ID Растение')
    water = models.IntegerField('Нома воды')
    time = models.TimeField('Время полива', default='00:00')
    date= models.CharField(verbose_name ='Частота полива',max_length=100)

    def __int__(self):
        return self.water
    def get_absolute_url(self):
        return f'/irrigation'
    class Meta:
        verbose_name ='Полив растений'
        verbose_name_plural = 'Полив растений'

class Firms(models.Model):
    name= models.CharField(verbose_name ='Название фирмы',max_length=100)
    adress = models.CharField(verbose_name='Юридический адрес', max_length=100)

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return f'/firms'
    class Meta:
        verbose_name ='Фирма'
        verbose_name_plural = 'Фирмы'

class Worker(models.Model):
    name= models.CharField(verbose_name ='ФИО',max_length=100)
    adress = models.CharField(verbose_name='Адрес', max_length=100)
    phone = models.CharField(verbose_name='Телефон',max_length=255 )
    firm = models.ForeignKey(Firms, on_delete=models.CASCADE, verbose_name='Фирмы')
    plant = models.OneToOneField(Plants, on_delete=models.CASCADE, verbose_name='Растения')

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return f'/worker'
    class Meta:
        verbose_name ='Рабочий'
        verbose_name_plural = 'Рабочие'

class Decorator(models.Model):
    name = models.CharField(verbose_name ='ФИО',max_length=100)
    adress = models.CharField(verbose_name='Адрес', max_length=100)
    phone = models.CharField(verbose_name='Телефон', max_length=11)
    ed = models.CharField(verbose_name='Образование', max_length=255)
    VUZ = models.CharField(verbose_name='ВУЗ', max_length=100)
    category = models.CharField(verbose_name='Категория', max_length=100)
    firm = models.ForeignKey(Firms, on_delete=models.CASCADE, verbose_name='Фирмы')

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return f'/decorator'
    class Meta:
        verbose_name ='Декоратор'
        verbose_name_plural = 'Декораторы'

class Time(models.Model):
    date = models.DateField('Дата работы с насаждением')
    name = models.ForeignKey(Worker, on_delete=models.CASCADE, verbose_name='Рабочий')


    def __int__(self):
        return self.name
    def get_absolute_url(self):
        return f'/time'
    class Meta:
        verbose_name ='График'
        verbose_name_plural = 'Графики'