from django.shortcuts import render, get_object_or_404, redirect
from agency.models import Announcer, AnnouncerTag, AnnouncerTag2
from .forms import OnlineForm_Form


def index(request):
    return render(request, 'agency/index.html')


def introduce(request):
    return render(request, 'agency/introduce.html')


def detail(request, announcer_id):
    mc = get_object_or_404(Announcer, pk=announcer_id)
    tag_list = list(mc.tags.all())
    tag2_list = list(mc.tags2.all())
    context = {'mc': mc, 'tag_list': tag_list, 'tag2_list': tag2_list}
    return render(request, 'agency/detail.html', context)


def mc_list(request):
    mc_search_name = request.GET.get('mc_search_name', '')
    mc_search_tag = request.GET.get('mc_search_tag', '')
    mc_search_tag2 = request.GET.get('mc_search_tag2', '')
    mainmclist = Announcer.objects.exclude(announcermain=False).order_by('?').distinct()
    mclist0 = Announcer.objects.exclude(announcerdisplay=False).order_by('?').distinct()
    if mc_search_name:
        mclist0 = mclist0.filter(name__icontains=mc_search_name).order_by().distinct()
    if mc_search_tag:
        mc_search_tag_list = [tag.strip() for tag in mc_search_tag.split(',')]
        mclist0 = mclist0.filter(tags__name__in=mc_search_tag_list).order_by().distinct()
    if mc_search_tag2:
        mc_search_tag2_list = [tag.strip() for tag in mc_search_tag2.split(',')]
        mclist0 = mclist0.filter(tags__name__in=mc_search_tag2_list).order_by().distinct()

    mclist = mclist0
    all_tag_list = list(AnnouncerTag.objects.all())
    all_tag2_list = list(AnnouncerTag2.objects.all())

    context = {
        'mclist': mclist,
        'mainmclist': mainmclist,
        'all_tag_list': all_tag_list,
        'all_tag2_list': all_tag2_list,
        'mc_search_name': mc_search_name,
        'mc_search_tag': mc_search_tag,
        'mc_search_tag2': mc_search_tag2
    }
    return render(request, 'agency/announcer_list.html', context)


def onlineform(request):
    if request.method == 'POST':
        onlineform = OnlineForm_Form(request.POST)
        if onlineform.is_valid():
            onlineformquestion = onlineform.save(commit=False)
            onlineformquestion.save()
            # post_event_on_telegram(onlineformquestion)
            return redirect('agency:onlineform_success')
    elif request.method == 'GET':
        onlineform = OnlineForm_Form()
        get_context = {
            'onlineform': onlineform
        }
        return render(request, 'agency/onlineform.html', get_context)
    else:
        onlineform = OnlineForm_Form()
    context = {'onlineform': onlineform}
    return render(request, 'agency/onlineform.html', context)


def onlineform_success(request):
    return render(request, 'agency/onlineform_success.html')
