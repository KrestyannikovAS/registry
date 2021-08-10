from django.shortcuts import render, redirect

from .forms import DocumentForm
from .models import Documents
from django.db.models import Q


def index(request):
    order_by = request.GET.get('order_by', 'approval_date')
    documents = Documents.objects.all().order_by(order_by)
    return render(request, 'main/index.html', {'title': 'Главная страница сайта', 'documents': documents})


def search(request):
    query = request.GET.get('q')
    if query is None:
        query = ''
    documents = Documents.objects.filter(Q(title__icontains=query) | Q(doc_author__icontains=query) |
                                         Q(approval_date__icontains=query) | Q(note__icontains=query))
    return render(request, 'main/search_results.html', {'title': 'Результат поиска', 'documents': documents})


def about(request):
    return render(request, 'main/about.html')


def create(request):
    error = ''
    if request.method == 'POST':
        form = DocumentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма была неверной'

    form = DocumentForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/create.html', context)
