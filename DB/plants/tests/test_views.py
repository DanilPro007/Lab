from django.test import TestCase
import unittest
from django.contrib.auth.models import User
from plants.models import Plants,Irrigation,Firms,Worker,Decorator,Time
from django.urls import reverse
class PlantsViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Plants.objects.create(title='Роза', age='1',date='05.01.2020', type='Шиповник')

    def test_view_url_exists_at_desired_location(self): # существование url по адресу
        resp = self.client.get('plants/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self): # существование url по имени
        resp = self.client.get(reverse('plt'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self): # соответствие шаблону
        resp = self.client.get(reverse('plt'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'plants/plants.html')
class IrrigationViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Irrigation.objects.create(plant='1', water='2', time='14:00', date='Два раза в неделю')
    def test_view_url_exists_at_desired_location(self): # существование url по адресу
        resp = self.client.get('irrigation/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self): # существование url по имени
        resp = self.client.get(reverse('irr'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self): # соответствие шаблону
        resp = self.client.get(reverse('irr'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'irrigation/irrigation.html')
class WorkerViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Worker.objects.create(name='Худяков Данил Алексеевич', adress='г. Архангельск',phone='1111111',firm='1', plant='1')
    def test_view_url_exists_at_desired_location(self): # существование url по адресу
        resp = self.client.get('worker/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self): # существование url по имени
        resp = self.client.get(reverse('wrk'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self): # соответствие шаблону
        resp = self.client.get(reverse('wrk'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'worker/worker.html')
class FirmsViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Firms.objects.create(name='Зеленая', adress='г. Архангельск')
    def test_view_url_exists_at_desired_location(self): # существование url по адресу
        resp = self.client.get('firms/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self): # существование url по имени
        resp = self.client.get(reverse('frm'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self): # соответствие шаблону
        resp = self.client.get(reverse('frm'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'firms/firms.html')
class DecoratorViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Decorator.objects.create(name='Худяков Артемий Алексеевич', adress='г. Архангельск',phone='11555111',ed='Ландшафтный дизайнер', VUZ='МГУ',category='Высшая', firm='1')
    def test_view_url_exists_at_desired_location(self): # существование url по адресу
        resp = self.client.get('decorator/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self): # существование url по имени
        resp = self.client.get(reverse('dcr'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self): # соответствие шаблону
        resp = self.client.get(reverse('dcr'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'decorator/decorator.html')
class TimeViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Time.objects.create(date='14:00', name='1')
    def test_view_url_exists_at_desired_location(self): # существование url по адресу
        resp = self.client.get('time/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self): # существование url по имени
        resp = self.client.get(reverse('tm'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self): # соответствие шаблону
        resp = self.client.get(reverse('tm'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'time/time.html')
class LogInTest(TestCase):
    def setUp(self):
        self.credentials = {
            'username': 'admin',
            'password': 'admin'}
        User.objects.create_user(**self.credentials)
    def test_login(self):
        # send login data
        response = self.client.post('login/', self.credentials, follow=True)
        # should be logged in now
        self.assertTrue(response.context['user'].is_active)
