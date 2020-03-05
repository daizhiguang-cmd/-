import json
import os.path
import uuid
from django.shortcuts import render,HttpResponse,redirect
from dzg_houtaiapp.models import Lunbo
from django.views.decorators.csrf import csrf_exempt
import re
from DZG_cfmw import settings
from utils.dzg_send import Yun
from utils.random import Codes
import datetime
from redis import Redis
Re = Redis(host='localhost',port=6379)


# Create your views here.
def hthome(request):
    return render(request,'houtai.html')

def dzg_login(request):
    return render(request,'dzg_login.html')

@csrf_exempt
def get_code(request):
    mobile = request.POST.get('mobile')
    print('111')
    Res = Re.get(mobile+'a')
    if Res:
        print('222')
        return HttpResponse('0')
    else:
        print('333')
        ret = re.match(r"^1[35678]\d{9}$", mobile)
        if ret:
            print('444')
            code = Codes().result
            yunpian = Yun(settings.APIKEY)
            yunpian.send_message(mobile, code)
            Re.set(mobile+'a',code,ex=60)
            Re.set(mobile+'b',code,ex=60)
            print(code)
            print('5555')
            return HttpResponse('1')


@csrf_exempt
def check_user(request):
    mobile = request.POST.get('mobile')
    code = request.POST.get('code')

    Res = Re.get(mobile+'b')
    print(Res)
    if Res:
        Res=Res.decode('utf-8')
        if code==Res:
            return HttpResponse('1')
        else:
            return HttpResponse('2')
    else:
        return HttpResponse('3')


@csrf_exempt
def add_banner(request):
    title = request.POST.get('title')
    print(title)
    status = request.POST.get('status')
    print(status)
    times = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    pic = request.FILES.get('pic')
    head = os.path.splitext(pic.name)[1]
    pic.name = str(uuid.uuid4()) + head
    Lunbo.objects.create(title=title, status=status, times=times, pic=pic)
    print(pic)
    return HttpResponse('0')


@csrf_exempt
def show_banner(request):
    print('1231')
    lunbo = Lunbo.objects.all().values()
    print('4444444')
    json_str = json.dumps(list(lunbo))
    print(json_str)
    print('321321321')
    return HttpResponse(json_str)


@csrf_exempt
def del_banner(request):
    id = request.GET.get('id')
    res = Lunbo.objects.filter(id=id)
    if res:
        res[0].delete()
        return HttpResponse('1')
    else:
        return HttpResponse('0')


def query_banner(request):
    id = request.GET.get('idx')
    request.session['id'] = id
    res = Lunbo.objects.filter(id=int(id))
    if res:
        rest=res.values()
        json_str = json.dumps(list(rest))
        return HttpResponse(json_str)


def change_banner(request):
    id = request.session.get('id')
    title = request.GET.get('title')
    status = request.GET.get('status')
    times = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    try:
        res = Lunbo.objects.filter(id=id)[0]
        res.title = title
        res.status = status
        res.times = times
        res.save()
        print('ok')
        return HttpResponse('ok')
    except:
        return HttpResponse(0)






