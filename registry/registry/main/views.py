from django.shortcuts import render, redirect
from .forms import DocumentForm
from .models import Documents
from django.db.models import Q
import datetime


def index(request):
    now = datetime.date.today()
    begin_time = now - datetime.timedelta(days=3650)
    order_by = request.GET.get('order_by', 'approval_date')
    query = request.GET.get('q')
    if query is None:
        query = ''
    date_start = request.GET.get('date_start')
    if date_start is None:
        date_start = begin_time
    date_end = request.GET.get('date_end')
    if date_end is None:
        date_end = now
    if date_start <= date_end:
        documents = Documents.objects.filter(Q(title__icontains=query) |
                                             Q(doc_author__icontains=query) |
                                             Q(approval_date__icontains=query) |
                                             Q(note__icontains=query)).filter(Q(approval_date__gte=date_start) &
                                                                              Q(approval_date__lte=date_end)).\
            order_by(order_by)
        return render(request, 'main/index.html', {'title': 'Результат поиска', 'documents': documents,
                                                            'q': query})
    else:
        error = 'Форма была неверной'
        return render(request, 'main/index.html', {'title': 'Результат поиска', 'error': error})


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
