from django.shortcuts import render, get_object_or_404, redirect, Http404
from academy.models import Notice, Event, Success
from .forms import OnlineForm_Form
# from .tasks import post_event_on_telegram

def index(request):
    return render(request, 'academy/index.html')


def introduce(request):
    return render(request, 'academy/introduce.html')


def course(request):
    return render(request, 'academy/course.html')

def notice(request):
    notice_list = Notice.objects.exclude(display=False).order_by('-create_date', '?').distinct()
    context = {
        'notice_list': notice_list,
    }
    return render(request, 'academy/notice.html', context)


def notice_article(request, notice_id):
    notice = get_object_or_404(Notice, pk=notice_id)
    if not notice.display:
        raise Http404
    context = {'notice': notice, }
    return render(request, 'academy/notice_article.html', context)


def event(request):
    event_list = Event.objects.exclude(display=False).order_by('-create_date', '?').distinct()
    context = {
        'event_list': event_list,
    }
    return render(request, 'academy/event.html', context)


def event_article(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    if not event.display:
        raise Http404
    context = {'event': event}
    return render(request, 'academy/event_article.html', context)


def success(request):
    success_list = Success.objects.exclude(display=False).order_by('-create_date', '?').distinct()
    context = {
        'success_list': success_list
    }
    return render(request, 'academy/success.html', context)


def success_article(request, success_id):
    success = get_object_or_404(Success, pk=success_id)
    if not success.display:
        raise Http404
    context = {'success': success}
    return render(request, 'academy/success_article.html', context)


def onlineform(request):
    if request.method == 'POST':
        onlineform = OnlineForm_Form(request.POST)
        if onlineform.is_valid():
            onlineformquestion = onlineform.save(commit=False)
            onlineformquestion.save()
            # post_event_on_telegram(onlineformquestion)
            return redirect('academy:onlineform_success')
    elif request.method == 'GET':
        onlineform = OnlineForm_Form()
        get_context = {
            'onlineform': onlineform
        }
        return render(request, 'academy/onlineform.html', get_context)
    else:
        onlineform = OnlineForm_Form()
    context = {'onlineform': onlineform}
    return render(request, 'academy/onlineform.html', context)


def onlineform_success(request):
    return render(request, 'academy/onlineform_success.html')

