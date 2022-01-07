from django.shortcuts import render, redirect
from .forms import DocumentForm
from .models import Documents
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.http import HttpResponseNotFound
import datetime


def index(request):
    now = datetime.date.today()
    warn_time = now + datetime.timedelta(days=60)
    order_by = request.GET.get('order_by', 'revision_date')
    query = request.GET.get('q')
    revision = request.GET.get('r')
    person = request.GET.get('person')
    authors = Documents.objects.values_list('doc_author', flat=True).distinct('doc_author')
    count_all = Documents.objects.values_list('id').count()
    count_ok = Documents.objects.filter(revision_date__gt=warn_time).count()
    count_warn = Documents.objects.filter(revision_date__lte=warn_time, revision_date__gt=now).count()
    count_err = Documents.objects.filter(revision_date__lte=now).count()
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
    if revision is None:
        if date_start <= date_end:
            documents = Documents.objects.filter(Q(title__icontains=query) |
                                                 Q(doc_author__icontains=query) |
                                                 Q(approval_date__icontains=query) |
                                                 Q(note__icontains=query)).filter(Q(approval_date__gte=date_start) &
                                                                                  Q(approval_date__lte=date_end) &
                                                                                  Q(doc_author__icontains=person)).\
                order_by(order_by)
            return render(request, 'main/index.html', {'documents': documents, 'warn': warn_time,
                                                       'authors': authors, 'now': now, 'count_all': count_all,
                                                       'count_ok': count_ok, 'count_warn': count_warn,
                                                       'count_err': count_err})
        else:
            error = 'Даты утверждения в форме поиска указан не верно!'
            return render(request, 'main/index.html', {'error': error})
    elif revision == 'ok':
        documents = Documents.objects.filter(Q(revision_date__gt=warn_time))
        return render(request, 'main/index.html', {'documents': documents, 'warn': warn_time,
                                                   'authors': authors, 'now': now, 'count_all': count_all,
                                                   'count_ok': count_ok, 'count_warn': count_warn,
                                                   'count_err': count_err})
    elif revision == 'warn':
        documents = Documents.objects.filter(Q(revision_date__lte=warn_time) & Q(revision_date__gt=now))
        return render(request, 'main/index.html', {'documents': documents, 'warn': warn_time,
                                                   'authors': authors, 'now': now, 'count_all': count_all,
                                                   'count_ok': count_ok, 'count_warn': count_warn,
                                                   'count_err': count_err})
    elif revision == 'err':
        documents = Documents.objects.filter(Q(revision_date__lte=now))
        return render(request, 'main/index.html', {'documents': documents, 'warn': warn_time,
                                                   'authors': authors, 'now': now, 'count_all': count_all,
                                                   'count_ok': count_ok, 'count_warn': count_warn,
                                                   'count_err': count_err})


def delete_conf(request, id):
    document = Documents.objects.get(id=id)
    return render(request, 'main/delete_conf.html', {"document": document})


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
            document.doc_author_department = request.POST.get("doc_author_department")
            document.approval_date = request.POST.get("approval_date")
            document.revision_date = request.POST.get("revision_date")
            document.doc_source = request.POST.get("doc_source")
            document.doc_url = request.POST.get("doc_url")
            document.note = request.POST.get("note")
            document.save()
            return HttpResponseRedirect("/")
        else:
            return render(request, "main/change.html", {"document": document})
    except Documents.DoesNotExist:
        return HttpResponseNotFound("<h2>Документ для изменения не найден</h2>")


# удаление данных из бд
def delete(request, id):
    try:
        document = Documents.objects.get(id=id)
        document.delete()
        return HttpResponseRedirect("/")
    except Documents.DoesNotExist:
        return HttpResponseNotFound("<h2>Документ для удаления не найден</h2>")
