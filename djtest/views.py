import datetime

from django.shortcuts import render

# Create your views here.
from django.utils.timezone import now

from djtest import models


def index(request):
    return render(request, 'test.html', {'user': 'motherfucker~'})


def new_page(request):
    return render(request, 'newLog.html')


def myLogs(request):
    logs = models.Log.objects.all()
    return render(request, 'logs.html', {'logs': logs})


def log_page(request, log_id):
    log = models.Log.objects.get(pk=log_id)
    origin_flags = models.Flag.objects.filter(log_id=log_id)
    flags = []
    for flag in origin_flags:
        flags.append({"flag": flag, "flag_time": flag.create_time - log.create_time})
    return render(request, 'log.html', {'log': log, 'flags': flags, 'flags_num': flags.__len__() + 1})


def add_flag(request):
    name = "请输入任务断点名称"
    create_time = now()
    log_id = request.POST.get("log_id")
    origin_flags = models.Flag.objects.filter(log_id=log_id)
    seq = len(origin_flags) + 1
    models.Flag.objects.create(seq=seq, name=name, create_time=create_time, log_id=log_id)

    log = models.Log.objects.get(pk=log_id)
    origin_flags = models.Flag.objects.filter(log_id=log_id)
    flags = []
    for flag in origin_flags:
        flags.append({"flag": flag, "flag_time": flag.create_time - log.create_time})
    return render(request, 'log.html', {'log': log, 'flags': flags})


def modify_flag(request):
    pk = request.POST.get("flag_id")
    log_id = request.POST.get("log_id")
    name = request.POST.get("flag_name", "Fuck")
    flag = models.Flag.objects.get(pk=pk)
    flag.name = name
    flag.save()
    log = models.Log.objects.get(pk=log_id)
    origin_flags = models.Flag.objects.filter(log_id=log_id)
    flags = []
    for flag in origin_flags:
        flags.append({"flag": flag, "flag_time": flag.create_time - log.create_time})
    return render(request, 'log.html', {'log': log, 'flags': flags})


def end_log(request):
    log_id = request.POST.get("log_id")
    log = models.Log.objects.get(pk=log_id)
    log.end_time = now() - log.create_time
    log.status = False
    log.save()
    origin_flags = models.Flag.objects.filter(log_id=log_id)
    flags = []
    for flag in origin_flags:
        flags.append({"flag": flag, "flag_time": flag.create_time - log.create_time})
    return render(request, 'log.html', {'log': log, 'flags': flags})


def new_log(request):
    name = request.POST.get("name")
    target = request.POST.get("mission")
    status = True
    user_id = 1
    create_time = now()
    models.Log.objects.create(name=name, target=target, create_time=create_time, status=status, user_id=user_id)
    logs = models.Log.objects.all()
    return render(request, 'logs.html', {'logs': logs})

# def newFlag(request):
#     id = request.POST.get("id")
#     flag = models.Flag.objects.get(pk=id)
#     name = request.POST.get("name")
#     flag.name = name
#     flag.save()
#     return render(request, 'logs.html')
