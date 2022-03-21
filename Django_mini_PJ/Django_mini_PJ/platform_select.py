# -*- coding: utf-8 -*-
 
# from http.client import HTTPResponse
from logging.config import stopListening
from time import gmtime
from django.http import HttpResponse
from platform import platform
from django.shortcuts import render
from django.views.decorators import csrf
from GamesModel.models import Game
import json
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
import matplotlib.pyplot as plt
# from django.template.defaulttags import csrf_token 
# 接收POST请求数据
from django.views.decorators.csrf import csrf_exempt 



#SKLEARN
# @csrf_token
@csrf_exempt
def platform_select(request):
    ctx ={}
    ctx_list=[]
    game_list=[]
    response="" 
    list = Game.objects.all()


    if 'Game1' in request.POST:
        g1=request.POST['Game1']
        list = Game.objects.all()
        if g1!="":
            temp_list=list.filter(Name=g1)
            for i in temp_list:
                game_list.append(i)

    if 'Game2' in request.POST:
        g2=request.POST['Game2']
        list = Game.objects.all()
        if g2!="":
            temp_list=list.filter(Name=g2)
            for i in temp_list:
                game_list.append(i)

    if 'Game3' in request.POST:
        g3=request.POST['Game3']
        list = Game.objects.all()
        if g3!="":
            temp_list=list.filter(Name=g3)
            for i in temp_list:
                game_list.append(i)

    if 'Game4' in request.POST:
        g4=request.POST['Game4']
        list = Game.objects.all()
        if g4!="":
            temp_list=list.filter(Name=g4)
            for i in temp_list:
                game_list.append(i)

    if 'Game5' in request.POST:
        g5=request.POST['Game5']
        list = Game.objects.all()
        if g5!="":
            temp_list=list.filter(Name=g5)
            for i in temp_list:
                game_list.append(i)





    
    name_list=[]
    for var in game_list:
        name_list.append(var.Name)
    ctx_json=json.dumps(name_list)


    PLA_dict={"Wii":0,"NS":0,"NES":0,"PC":0,"GB":0,"DS":0,"X360":0,"SNES":0,"PS3":0,"PS4":0,"3DS":0,"PS2":0,"GBA":0,"GEN":0,"N64":0,"PS":0,"XOne":0,"WiiU":0,"XB":0,"PSP":0,"2600":0,"GC":0,"GBC":0}
    # pla_count=np.zeros()
    for var in game_list:
        PLA_dict[f"{var.Platform}"]+=1;
    ans_pla=max(PLA_dict,key=lambda k:PLA_dict[k])

    sorted(PLA_dict.items(),key=lambda item:item[1])

    ans_pla_ctx={}
    ans_pla_ctx["max"]=ans_pla
    ans_pla_ctx["dict"]=PLA_dict

    ans_pla_ctx_json=json.dumps(ans_pla_ctx)
    ctx_show={}
    ctx_show['list']=ans_pla
    return HttpResponse(ans_pla_ctx_json)  
    # return render(request, "platform_select.html", ctx_show)

