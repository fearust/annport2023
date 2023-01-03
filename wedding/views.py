from django.shortcuts import render, get_object_or_404, redirect
from wedding.models import Mc, McTag
from .forms import CastForm
from django.utils import timezone


def index(request):
    return render(request, 'wedding/home.html')


def service(request):
    return render(request, 'wedding/wedding_service.html')


def detail(request, mc_id):
    mc = get_object_or_404(Mc, pk=mc_id)
    tag_list = list(mc.tags.all())
    context = {'mc': mc, 'tag_list': tag_list}
    return render(request, 'wedding/mc_detail.html', context)


def mc_list(request):
    mc_search_name = request.GET.get('mc_search_name', '')
    mc_search_tag = request.GET.get('mc_search_tag', '')
    mclist0 = Mc.objects.exclude(mcdisplay=False).order_by('-mcmain', '?').distinct()
    if mc_search_name:
        mclist0 = mclist0.filter(name__icontains=mc_search_name).order_by().distinct()
    if mc_search_tag:
        mc_search_tag_list = [tag.strip() for tag in mc_search_tag.split(',')]
        mclist0 = mclist0.filter(tags__name__in=mc_search_tag_list).order_by().distinct()

    mclist = mclist0
    all_tag_list = list(McTag.objects.all())

    context = {
        'mclist': mclist,
        'all_tag_list': all_tag_list,
        'mc_search_name': mc_search_name,
        'mc_search_tag': mc_search_tag
    }
    return render(request, 'wedding/mc_list.html', context)


def cast(request):
    if request.method == 'POST':
        castform = CastForm(request.POST)
        if castform.is_valid():
            castformquestion = castform.save(commit=False)
            castformquestion.create_date = timezone.now()
            castformquestion.save()
            return redirect('wedding:cast_success')
    elif request.method == 'GET':
        mc_cast_name = request.GET.get('mc_cast_name', '')
        castform = CastForm()
        get_context = {
            'wish_mc': mc_cast_name,
            'castform': castform
        }
        return render(request, 'wedding/cast.html', get_context)
    else:
        castform = CastForm()
    context = {'castform': castform}
    return render(request, 'wedding/cast.html', context)


def cast_success(request):
    return render(request, 'wedding/cast_success.html')
