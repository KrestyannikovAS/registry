from django.forms import ModelForm, TextInput
from .models import Documents


class DocumentForm(ModelForm):
    class Meta:
        model = Documents
        fields = ["title", "doc_author", "doc_author_department", "approval_date", "revision_date", "doc_source",
                  "doc_url", "note"]
        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите название документа'
            }),
            "doc_author": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите ФИО автора'
            }),
            "doc_author_department": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите отдел (по умолчанию "СПАК")'
            }),
            "approval_date": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите дату утверждения'
            }),
            "revision_date": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите дату пересмотра'
            }),
            "doc_source": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите источники (по умолчанию "АСДОУ")'
            }),
            "doc_url": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите ссылку на документ'
            }),
            "note": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите комментарий (по умолчанию "НЕТ")'
            }),
        }
