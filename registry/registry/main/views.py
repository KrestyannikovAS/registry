from django.shortcuts import render, redirect
from .forms import DocumentForm
from .models import Documents
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.http import HttpResponseNotFound
import datetime


def index(request):
    now = datetime.date.today()
    warn_time = now - datetime.timedelta(days=1065)
    err_time = now - datetime.timedelta(days=1095)
    order_by = request.GET.get('order_by', 'approval_date')
    query = request.GET.get('q')
    person = request.GET.get('person')
    authors = Documents.objects.values_list('doc_author', flat=True).distinct('doc_author')
    if query is None:
        query = ''
    if person is None:
        person = ''
    date_start = request.GET.get('date_start')
    if date_start is None:
        date_start = now - datetime.timedelta(days=3650)
    date_end = request.GET.get('date_end')
    if date_end is None:
        date_end = now
    if date_start <= date_end:
        documents = Documents.objects.filter(Q(title__icontains=query) |
                                             Q(doc_author__icontains=query) |
                                             Q(approval_date__icontains=query) |
                                             Q(note__icontains=query)).filter(Q(approval_date__gte=date_start) &
                                                                              Q(approval_date__lte=date_end) &
                                                                              Q(doc_author__icontains=person)).\
            order_by(order_by)
        return render(request, 'main/index.html', {'documents': documents, 'warn': warn_time,
                                                   'err': err_time, 'authors': authors})
    else:
        error = 'Даты утверждения в форме поиска указан не верно!'
        return render(request, 'main/index.html', {'error': error})


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


# изменение данных в бд
def change(request, id):
    try:
        document = Documents.objects.get(id=id)

        if request.method == "POST":
            document.title = request.POST.get("title")
            document.doc_author = request.POST.get("doc_author")
            document.approval_date = request.POST.get("approval_date")
            document.doc_url = request.POST.get("doc_url")
            document.note = request.POST.get("note")
            document.save()
            return HttpResponseRedirect("/")
        else:
            return render(request, "main/change.html", {"document": document})
    except Documents.DoesNotExist:
        return HttpResponseNotFound("<h2>Документ для изменения не найден</h2>")


# удаление данных из бд
def delete(id):
    try:
        document = Documents.objects.get(id=id)
        document.delete()
        return HttpResponseRedirect("/")
    except Documents.DoesNotExist:
        return HttpResponseNotFound("<h2>Документ для удаления не найден</h2>")
