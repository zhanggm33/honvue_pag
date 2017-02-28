# -*- coding: utf-8 -*-
import json
from django.shortcuts import render
from django.http import HttpResponse
# from django.http import HttpResponseRedirect
from . import configs
from .models import Game, New, JobCategory, Job, HyMember
from django.http import Http404
from django.shortcuts import get_object_or_404


def login(request):
    info = {
        'flag': False,
        'username': '',
        'errmsg': '',
    }
    try:
        m = HyMember.objects.get(username=str(request.POST['username']))
    except:
        info['errmsg'] =  u"用户名不存在"
    else:
        if m.password != m.dim_password(request.POST['password']):
            info['errmsg'] = u"密码不正确"
        else:
            request.session['member_id'] = m.member_id
            info['flag'] = True
            info['username'] = m.username
    return HttpResponse(json.dumps(info))
    

def register(request): 
    info = {
        'flag': False,
        'username': '',
        'errormsg': '',
    }
    try:
        username = str(request.POST['username'])
    except UnicodeEncodeError:
        info['errmsg'] = u'用户名必须由字母和数字组成'
        return HttpResponse(json.dumps(info))
    try:
        pw = str(request.POST['password']) 
    except UnicodeEncodeError:
        info['errmsg'] = u'密码必须由字母数字符号组成'
        return HttpResponse(json.dumps(info))
    # 密码不为空
    if pw == '':
        info['errmsg'] = u'密码不能为空'
        return HttpResponse(json.dumps(info))
    try:
        m = HyMember.objects.get(username=username)
    except:
        m = HyMember.create_new_user(username, pw)
        info['flag'] = True
        info['username'] = m.username
        request.session['member_id'] = m.member_id
    else:
        info['errmsg'] =  u"用户名已存在"
    return HttpResponse(json.dumps(info))


def index(request):
    return home(request)


def home(request):
    games = Game.objects.order_by('index')
    context = {'games': games, 'toptag': 'home'}
    return render(request, 'home.html', context)

def games(request, pag=1):
    gap = 3
    pag = int(pag)
    all_games = Game.objects.order_by('index') 
    games = all_games[(pag -1)*gap:gap*pag]
    total_pags = range(1, ((len(all_games) - 1) // gap + 2))
    pre_pag = (pag - 1) if pag > 1 else 1
    next_pag = (pag + 1) if pag < total_pags[-1] else total_pags[-1]
    context = {'toptag': 'games', 'games': games, 'pag': pag, 'total_pags': total_pags, 'pre_pag': pre_pag, 'next_pag': next_pag}
    return render(request, 'games.html', context)

def news(request, pag=1):
    gap = 3 
    pag = int(pag)
    all_news = New.objects.order_by('-pub_date')
    news = all_news[(pag -1)*gap: gap*pag]
    total_pags = range(1, ((len(all_news) - 1) // gap + 2))
    pre_pag = (pag - 1) if pag > 1 else 1
    next_pag = (pag + 1) if pag < total_pags[-1] else total_pags[-1]
    context = {'toptag': 'news', 'news': news, 'pag': pag, 'total_pags': total_pags, 'pre_pag': pre_pag, 'next_pag': next_pag}

    return render(request, 'news.html', context)

def business(request):
    context = {'toptag': 'business'}
    return render(request, 'business.html', context)

def joinUs(request):
    categorys = JobCategory.objects.order_by('index')
    context = {'toptag': 'joinUs', 'categorys': categorys}
    return render(request, 'joinUs.html', context)

def aboutUs(request):
    context = {'toptag': 'aboutUs'}
    return render(request, 'aboutUs.html', context)

def gameDetail(request, game_index):
    game_index = int(game_index) 
    game = get_object_or_404(Game, index=game_index)
    context = {'toptag': 'games', 'game': game}
    return render(request, 'gameDetail.html', context)

def newsDetail(request, new_id):
    new_id = int(new_id) 
    new = get_object_or_404(New, id=new_id)
    context = {'toptag': 'news', 'new': new}
    return render(request, 'newsDetail.html', context)

def jobDesc(request, job_id):
    try:
        job = get_object_or_404(Job, id=job_id)
    except IndexError:
        raise Http404("Job does not exist")
    return HttpResponse(job.desc.lstrip())
