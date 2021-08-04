from django.forms import ModelForm, TextInput

from .models import Documents


class DocumentForm(ModelForm):
    class Meta:
        model = Documents
        fields = ["title", "doc_author", "approval_date", "doc_url", "note"]
        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите название документа'
            }),
            "doc_author": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите ФИО автора'
            }),
            "approval_date": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите дату утверждения'
            }),
            "doc_url": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите ссылку на документ'
            }),
            "note": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите описание'
            }),
        }
