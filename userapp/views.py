from django.shortcuts import render,HttpResponse
from django.http import JsonResponse
from dzg_houtaiapp.models import Users
import time,datetime
# Create your views here.
def user_echarts(request):
    return render(request,'echarts.html')

def user_map(request):
    return render(request,'map.html')



def get_echarts(request):
    result = str(datetime.datetime.now().date())

    res = request.session.get('data1')
    if res != result:
        print('bbbb')
        a,b,c,d,e = 0,0,0,0,0
        nowtimes = time.time()
        print(nowtimes,type(nowtimes))
        time5 = nowtimes-5*7*24*60*60
        time4 = nowtimes-4*7*24*60*60
        time3 = nowtimes-3*7*24*60*60
        time2 = nowtimes-2*7*24*60*60
        time1 = nowtimes-1*7*24*60*60
        users = Users.objects.all()
        for i in users:
            timeArray = time.strptime(i.times, "%Y-%m-%d %H:%M:%S")
            print(timeArray, type(timeArray))
            # 转换为时间戳
            timeStamp = int(time.mktime(timeArray))
            print(timeStamp)
            if time5<timeStamp<time4:
                a+=1
            elif time4<timeStamp<time3:
                b+=1
            elif time3<timeStamp<time2:
                c+=1
            elif time2<timeStamp<time1:
                d+=1
            elif time1<timeStamp<nowtimes:
                e+=1
        data = {
            'x' : ['第一周', '第二周', '第三周', '第四周', '第五周'],
            'y' : [a,b,c,d,e]
        }
        request.session['data1'] = str(datetime.datetime.now().date())
        request.session['data11'] = data

        return JsonResponse(data)
    else:
        data = request.session.get('data11')
        print('aaaaa')
        print(data)
        print('aaaaaaaaa')
        return JsonResponse(data)


def get_map(request):
    result = str(datetime.datetime.now().date())
    print('ccccc')
    res = request.session.get('data2')
    if res != result:
        print('bbbbb')
        list = ['北京','天津','上海','重庆','河北','山西','辽宁','吉林','黑龙江','江苏','浙江','安徽','福建','江西','山东','新疆','广西','宁夏','内蒙古','西藏','河南','湖北','湖南','广东','海南','四川','贵州','云南','陕西','甘肃','青海','台湾','香港','澳门']
        dict = {'北京':0,'天津':0,'上海':0,'重庆':0,'河北':0,'山西':0,'辽宁':0,'吉林':0,'黑龙江':0,'江苏':0,'浙江':0,'安徽':0,'福建':0,'江西':0,'山东':0,'新疆':0,'广西':0,'宁夏':0,'内蒙古':0,'西藏':0,'河南':0,'湖北':0,'湖南':0,'广东':0,'海南':0,'四川':0,
                '贵州':0,'云南':0,'陕西':0,'甘肃':0,'青海':0,'台湾':0,'香港':0,'澳门':0}
        user = Users.objects.all()
        for i in user:
            for j in list:
                if i.address == j:
                    dict[j] = int(dict[j]) + 1
        data = []
        for i in list:
            re = {'name':i,'value':str(dict[i])}
            data.append(re)
        request.session['data2'] = str(datetime.datetime.now().date())
        request.session['data22'] = data
        return JsonResponse(data,safe=False)
    else:
        data = request.session.get('data22')
        print('aaaaa')
        print(data)
        print('aaaaaaaaa')
        return JsonResponse(data,safe=False)

