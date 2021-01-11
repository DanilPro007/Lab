from .models import Plants,Irrigation,Firms,Worker,Decorator,Time
from django.forms import ModelForm, TextInput, NumberInput, DateInput, ModelChoiceField,TimeInput,Textarea
class PlantsForm(ModelForm):
    class Meta:
        model = Plants
        fields = ['title','age','date','type']

        widgets={
            "title": TextInput(attrs={
                'class': 'form-control',
                'label': 'Название',
                'placeholder':'Название'
            }),
            "age": NumberInput(attrs={
                'class': 'form-control',
                'label': 'Возраст (в годах)',
                'placeholder': 'Возраст (в годах)'
            }),
            "date": DateInput(attrs={
                'class': 'form-control',
                'label': 'Дата высадки',
                'placeholder': 'Дата высадки'
            }),
            "type": TextInput(attrs={
                'class': 'form-control',
                'label': 'Тип',
                'placeholder': 'Тип'
            }),
        }

class IrrigationForm(ModelForm):
    class Meta:
        model = Irrigation
        fields = ['plant','water','time','date']

        widgets={
            "plant": NumberInput(attrs={
                'class': 'form-control',
                'label': 'ID Растения',
                'placeholder':'ID Растения'
            }),
            "water": NumberInput(attrs={
                'class': 'form-control',
                'label': 'Нома воды',
                'placeholder': 'Нома воды'
            }),
            "time": TimeInput(attrs={

                'class': 'form-control',
                'label': 'Время полива',
                'placeholder': 'Время полива',
            }),
            "date": TextInput(attrs={
                'class': 'form-control',
                'label': 'Частота полива',
                'placeholder': 'Частота полива'
            }),
        }



class FirmsForm(ModelForm):
    class Meta:
        model = Firms
        fields = ['name','adress']

        widgets={
            "name": TextInput(attrs={
                'class': 'form-control',
                'label': 'Название фирмы',
                'placeholder': 'Название фирмы'
            }),
            "adress": TextInput(attrs={
                'class': 'form-control',
                'label': 'Юридический адрес',
                'placeholder': 'Юридический адрес'
            }),
        }

class WorkerForm(ModelForm):
    class Meta:
        model = Worker
        fields = ['name','adress','phone','firm','plant']

        widgets={
            "name": TextInput(attrs={
                'class': 'form-control',
                'label': 'ФИО',
                'placeholder': 'ФИО'
            }),
            "adress": TextInput(attrs={
                'class': 'form-control',
                'label': 'Адрес',
                'placeholder': 'Адрес'
            }),
            "phone": TextInput(attrs={
                'class': 'form-control',
                'label': 'Телефон',
                'placeholder': 'Телефон'
            }),
            "plant": NumberInput(attrs={
                'class': 'form-control',
                'label': 'ID Растения',
                'placeholder': 'ID Растения'
            }),
            "firm": NumberInput(attrs={
                'class': 'form-control',
                'label': 'ID Фирмы',
                'placeholder': 'ID Фирмы'
            }),

        }


class DecoratorForm(ModelForm):
    class Meta:
        model = Decorator
        fields = ['name','adress','phone','ed','VUZ','category','firm']

        widgets={
            "name": TextInput(attrs={
                'class': 'form-control',
                'label': 'ФИО',
                'placeholder': 'ФИО'
            }),
            "adress": TextInput(attrs={
                'class': 'form-control',
                'label': 'Адрес',
                'placeholder': 'Адрес'
            }),
            "phone": TextInput(attrs={
                'class': 'form-control',
                'label': 'Телефон',
                'placeholder': 'Телефон'
            }),
            "ed": TextInput(attrs={
                'class': 'form-control',
                'label': 'Образование',
                'placeholder': 'Образование'
            }),
            "VUZ": TextInput(attrs={
                'class': 'form-control',
                'label': 'ВУЗ',
                'placeholder': 'ВУЗ'
            }),
            "category": TextInput(attrs={
                'class': 'form-control',
                'label': 'Категория',
                'placeholder': 'Категория'
            }),
            "firm": NumberInput(attrs={
                'class': 'form-control',
                'label': 'ID Фирмы',
                'placeholder': 'ID Фирмы'
            }),

        }

class TimeForm(ModelForm):
    class Meta:
        model = Time
        fields = ['date','name']

        widgets={
            "date": DateInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата работы с насаждением',
                'label': 'Дата работы с насаждением'
            }),
            "name": NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'ID Сотрудника',
                'label': 'ID Сотрудника'
            }),


        }