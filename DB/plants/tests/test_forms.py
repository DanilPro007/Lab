from django.test import TestCase
import unittest
from plants.forms import PlantsForm, IrrigationForm,FirmsForm , WorkerForm, DecoratorForm, TimeForm




class PlantsFormTest(TestCase):
    def test_title_label(self):
        form = PlantsForm()
        self.assertTrue(form.fields['title'].label == None or form.fields['title'].label == 'Название')
    def test_age_label(self):
        form = PlantsForm()
        self.assertTrue(form.fields['age'].label == None or form.fields['age'].label == 'Возраст (в годах)')
    def test_date_label(self):
        form = PlantsForm()
        self.assertTrue(form.fields['date'].label == None or form.fields['date'].label == 'Дата высадки')
    def test_type_label(self):
        form = PlantsForm()
        self.assertTrue(form.fields['type'].label == None or form.fields['type'].label == 'Тип')

    def test_proverka(self):
        form = PlantsForm(data={'title': "Роза", 'age': "1", 'date': "05.01.2020", 'type': "Шиповник"})
        self.assertTrue(form.is_valid())
class IrrigationForm(TestCase):
    def test_plant_label(self):
        form = IrrigationForm()
        self.assertTrue(form.fields['plant'].label == None or form.fields['plant'].label == 'ID Растения')
    def test_water_label(self):
        form = IrrigationForm()
        self.assertTrue(form.fields['water'].label == None or form.fields['water'].label == 'Нома воды')
    def test_time_label(self):
        form = IrrigationForm()
        self.assertTrue(form.fields['time'].label == None or form.fields['time'].label == 'Время полива')
    def test_date_label(self):
        form = IrrigationForm()
        self.assertTrue(form.fields['date'].label == None or form.fields['date'].label == 'Частота полива')

    def test_proverka(self):
        form = IrrigationForm(data={'plant': "1", 'water': "2",'time': "14:00", 'date': "Два раза в неделю"})
        self.assertTrue(form.is_valid())
class FirmsForm(TestCase):
    def test_name_label(self):
        form = FirmsForm()
        self.assertTrue(form.fields['name'].label == None or form.fields['name'].label == 'Название фирмы')
    def test_adress_label(self):
        form = FirmsForm()
        self.assertTrue(form.fields['adress'].label == None or form.fields['adress'].label == 'Юридический адрес')

    def test_proverka(self):
        form = FirmsForm(data={'name': "Зеленая", 'adress': "г. Архангельск"})
        self.assertTrue(form.is_valid())
class WorkerForm(TestCase):
    def test_name_label(self):
        form = WorkerForm()
        self.assertTrue(form.fields['name'].label == None or form.fields['name'].label == 'ФИО')
    def test_adress_label(self):
        form = WorkerForm()
        self.assertTrue(form.fields['adress'].label == None or form.fields['adress'].label == 'Адрес')
    def test_phone_label(self):
        form = WorkerForm()
        self.assertTrue(form.fields['phone'].label == None or form.fields['phone'].label == 'Телефон')
    def test_firm_label(self):
        form = WorkerForm()
        self.assertTrue(form.fields['firm'].label == None or form.fields['firm'].label == 'ID Фирмы')
    def test_plant_label(self):
        form = WorkerForm()
        self.assertTrue(form.fields['plant'].label == None or form.fields['plant'].label == 'ID Растения')

    def test_proverka(self):
        form = WorkerForm(data={'name': "Худяков Данил Алексеевич", 'adress': "г. Архангельск",'phone': "1111111", 'firm': "1",'plant': "1"})
        self.assertTrue(form.is_valid())
class DecoratorForm(TestCase):
    def test_name_label(self):
        form = DecoratorForm()
        self.assertTrue(form.fields['name'].label == None or form.fields['name'].label == 'ФИО')
    def test_adress_label(self):
        form = DecoratorForm()
        self.assertTrue(form.fields['adress'].label == None or form.fields['adress'].label == 'Адрес')
    def test_phone_label(self):
        form = DecoratorForm()
        self.assertTrue(form.fields['phone'].label == None or form.fields['phone'].label == 'Телефон')
    def test_ed_label(self):
        form = DecoratorForm()
        self.assertTrue(form.fields['ed'].label == None or form.fields['ed'].label == 'Образование')
    def test_VUZ_label(self):
        form = DecoratorForm()
        self.assertTrue(form.fields['VUZ'].label == None or form.fields['VUZ'].label == 'ВУЗ')
    def test_category_label(self):
        form = DecoratorForm()
        self.assertTrue(form.fields['category'].label == None or form.fields['category'].label == 'Категория')
    def test_firm_label(self):
        form = DecoratorForm()
        self.assertTrue(form.fields['firm'].label == None or form.fields['firm'].label == 'ID Фирмы')

    def test_proverka(self):
        form = WorkerForm(data={'name': "Худяков Артемий Алексеевич", 'adress': "г. Архангельск",'phone': "11555111", 'ed': "Ландшафтный дизайнер",'VUZ': "МГУ",'category': "Высшая",'firm': "1"})
        self.assertTrue(form.is_valid())
class TimeForm(TestCase):
    def test_date_label(self):
        form = TimeForm()
        self.assertTrue(form.fields['date'].label == None or form.fields['date'].label == 'Дата работы с насаждением')
    def test_name_label(self):
        form = TimeForm()
        self.assertTrue(form.fields['name'].label == None or form.fields['name'].label == 'ID Сотрудника')

    def test_proverka(self):
        form = TimeForm(data={'date': "14:00", 'name': "1"})
        self.assertTrue(form.is_valid())
