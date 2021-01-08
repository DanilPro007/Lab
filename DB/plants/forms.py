from .models import Articles,Irrigation,Firms,Worker,Decorator,Time
from django.forms import ModelForm, TextInput, NumberInput, DateInput, ModelChoiceField,TimeInput,Textarea
class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['title','age','date','type']

        widgets={
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder':'Название'
            }),
            "age": NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Возраст (в годах)'
            }),
            "date": DateInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата высадки'
            }),
            "type": TextInput(attrs={
                'class': 'form-control',
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
                'placeholder':'ID Растения'
            }),
            "water": NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Нома воды'
            }),
            "time": TimeInput(attrs={

                'class': 'form-control',
                'placeholder': 'Время полива',
            }),
            "date": TextInput(attrs={
                'class': 'form-control',
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
                'placeholder': 'Название фирмы'
            }),
            "adress": TextInput(attrs={
                'class': 'form-control',
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
                'placeholder': 'ФИО'
            }),
            "adress": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Адрес'
            }),
            "phone": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Телефон'
            }),
            "plant": NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'ID Растения'
            }),
            "firm": NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'ID Фирмы'
            }),

        }


class DecoratorForm(ModelForm):
    class Meta:
        model = Decorator
        fields = ['name','adress','phone','VUZ','category','firm']

        widgets={
            "name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'ФИО'
            }),
            "adress": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Адрес'
            }),
            "phone": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Телефон'
            }),
            "VUZ": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'ВУЗ'
            }),
            "category": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Категория'
            }),
            "firm": NumberInput(attrs={
                'class': 'form-control',
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
                'placeholder': 'Дата работы с насаждением'
            }),
            "name": NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'ID Сотрудника'
            }),


        }