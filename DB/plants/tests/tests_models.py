from django.test import TestCase
import unittest
from plants.models import Plants,Irrigation,Firms,Worker,Decorator,Time
class PlantsModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Plants.objects.create(title='Роза', age='1',date='05.01.2020', type='Шиповник')
    def test_title_label(self):
        plants = Plants.objects.get(id=1)
        field_label = plants._meta.get_field('title').verbose_name
        self.assertEquals(field_label == 'title')
    def test_title_max_length(self):
        plants = Plants.objects.get(id=1)
        max_length = plants._meta.get_field('title').max_length
        self.assertEquals(max_length, 100)
    def test_age_label(self):
        plants = Plants.objects.get(id=1)
        field_label = plants._meta.get_field('age').verbose_name
        self.assertEquals(field_label,'age')
    def test_date_label(self):
        plants = Plants.objects.get(id=1)
        field_label = plants._meta.get_field('date').verbose_name
        self.assertEquals(field_label,'date')
    def test_type_label(self):
        plants = Plants.objects.get(id=1)
        field_label = plants._meta.get_field('title').verbose_name
        self.assertEquals(field_label,'title')
    def test_type_max_length(self):
        plants = Plants.objects.get(id=1)
        max_length = plants._meta.get_field('type').max_length
        self.assertEquals(max_length, 1000)

class IrrigationModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Irrigation.objects.create(plant='1',water='2', time='14:00', date='Два раза в неделю')
    def test_plantir_label(self):
        plants = Irrigation.objects.get(id=1)
        field_label = plants._meta.get_field('plant').verbose_name
        self.assertEquals(field_label,'ID Растение')
    def test_water_label(self):
        plants = Irrigation.objects.get(id=1)
        field_label = plants._meta.get_field('water').verbose_name
        self.assertEquals(field_label,'Нома воды')
    def test_time_label(self):
        plants = Irrigation.objects.get(id=1)
        field_label = plants._meta.get_field('time').verbose_name
        self.assertEquals(field_label,'Время полива')
    def test_date_label(self):
        plants = Irrigation.objects.get(id=1)
        field_label = plants._meta.get_field('date').verbose_name
        self.assertEquals(field_label,'Частота полива')
    def test_date_max_length(self):
        plants = Irrigation.objects.get(id=1)
        max_length = plants._meta.get_field('date').max_length
        self.assertEquals(max_length, 100)
class FirmsModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Firms.objects.create(name='Зеленая', adress='г. Архангельск')

    def test_name_label(self):
        plants = Firms.objects.get(id=1)
        field_label = plants._meta.get_field('name').verbose_name
        self.assertEquals(field_label,'Название фирмы')
    def test_name_max_length(self):
        plants = Firms.objects.get(id=1)
        max_length = plants._meta.get_field('name').max_length
        self.assertEquals(max_length, 100)
    def test_adress_label(self):
        plants = Firms.objects.get(id=1)
        field_label = plants._meta.get_field('adress').verbose_name
        self.assertEquals(field_label,'Юридический адрес')
    def test_adress_max_length(self):
        plants = Firms.objects.get(id=1)
        max_length = plants._meta.get_field('adress').max_length
        self.assertEquals(max_length, 100)
class WorkerModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Worker.objects.create(name='Худяков Данил Алексеевич', adress='г. Архангельск',phone='1111111',firm='1', plant='1')
    def test_name_label(self):
        plants = Worker.objects.get(id=1)
        field_label = plants._meta.get_field('name').verbose_name
        self.assertEquals(field_label,'ФИО')
    def test_name_max_length(self):
        plants = Worker.objects.get(id=1)
        max_length = plants._meta.get_field('name').max_length
        self.assertEquals(max_length, 100)
    def test_adress_label(self):
        plants = Worker.objects.get(id=1)
        field_label = plants._meta.get_field('adress').verbose_name
        self.assertEquals(field_label,'Адрес')
    def test_adress_max_length(self):
        plants = Worker.objects.get(id=1)
        max_length = plants._meta.get_field('adress').max_length
        self.assertEquals(max_length, 100)
    def test_phone_label(self):
        plants = Worker.objects.get(id=1)
        field_label = plants._meta.get_field('phone').verbose_name
        self.assertEquals(field_label,'Телефон')
    def test_phone_max_length(self):
        plants = Worker.objects.get(id=1)
        max_length = plants._meta.get_field('phone').max_length
        self.assertEquals(max_length, 255)
    def test_firmwr_label(self):
        plants = Worker.objects.get(id=1)
        field_label = plants._meta.get_field('firm').verbose_name
        self.assertEquals(field_label,'Фирмы')
    def test_plantwr_label(self):
        plants = Worker.objects.get(id=1)
        field_label = plants._meta.get_field('plant').verbose_name
        self.assertEquals(field_label,'Растения')
class DecoratorModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Decorator.objects.create(name='Худяков Артемий Алексеевич', adress='г. Архангельск',phone='11555111',ed='Ландшафтный дизайнер', VUZ='МГУ',category='Высшая', firm='1')
    def test_name_label(self):
        plants = Decorator.objects.get(id=1)
        field_label = plants._meta.get_field('name').verbose_name
        self.assertEquals(field_label,'ФИО')
    def test_name_max_length(self):
        plants = Decorator.objects.get(id=1)
        max_length = plants._meta.get_field('name').max_length
        self.assertEquals(max_length, 100)
    def test_adress_label(self):
        plants = Decorator.objects.get(id=1)
        field_label = plants._meta.get_field('adress').verbose_name
        self.assertEquals(field_label,'Адрес')
    def test_adress_max_length(self):
        plants = Decorator.objects.get(id=1)
        max_length = plants._meta.get_field('adress').max_length
        self.assertEquals(max_length, 100)
    def test_phone_label(self):
        plants = Decorator.objects.get(id=1)
        field_label = plants._meta.get_field('phone').verbose_name
        self.assertEquals(field_label,'Телефон')
    def test_phone_max_length(self):
        plants = Decorator.objects.get(id=1)
        max_length = plants._meta.get_field('phone').max_length
        self.assertEquals(max_length, 11)
    def test_ed_label(self):
        plants = Decorator.objects.get(id=1)
        field_label = plants._meta.get_field('ed').verbose_name
        self.assertEquals(field_label,'Образование')
    def test_ed_max_length(self):
        plants = Decorator.objects.get(id=1)
        max_length = plants._meta.get_field('ed').max_length
        self.assertEquals(max_length, 255)
    def test_VUZ_label(self):
        plants = Decorator.objects.get(id=1)
        field_label = plants._meta.get_field('VUZ').verbose_name
        self.assertEquals(field_label,'ВУЗ')
    def test_VUZ_max_length(self):
        plants = Decorator.objects.get(id=1)
        max_length = plants._meta.get_field('VUZ').max_length
        self.assertEquals(max_length, 100)
    def test_category_label(self):
        plants = Decorator.objects.get(id=1)
        field_label = plants._meta.get_field('category').verbose_name
        self.assertEquals(field_label,'Категория')
    def test_category_max_length(self):
        plants = Decorator.objects.get(id=1)
        max_length = plants._meta.get_field('category').max_length
        self.assertEquals(max_length, 100)
    def test_firmdr_label(self):
        plants = Decorator.objects.get(id=1)
        field_label = plants._meta.get_field('firm').verbose_name
        self.assertEquals(field_label,'Фирмы')
class TimeModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Time.objects.create(date='14:00', name='1')
    def test_date_label(self):
        plants = Time.objects.get(id=1)
        field_label = plants._meta.get_field('date').verbose_name
        self.assertEquals(field_label,'Дата работы с насаждением')
    def test_name_label(self):
        plants = Decorator.objects.get(id=1)
        field_label = plants._meta.get_field('name').verbose_name
        self.assertEquals(field_label,'Рабочий')


