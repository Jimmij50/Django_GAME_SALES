# -*- coding: utf-8 -*-
 
# from http.client import HTTPResponse
from django.http import HttpResponse
from platform import platform
from django.shortcuts import render
from django.views.decorators import csrf
from GamesModel.models import Game
import json
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
# from django.template.defaulttags import csrf_token 
from django.views.decorators.csrf import csrf_exempt 
# 接收POST请求数据







# @csrf_token
@csrf_exempt
def my_search_list(request):
    ctx ={}
    ctx_list=[]
    response="" 
    list = Game.objects.all()


    if 'Name' in request.POST:
        my_name=request.POST['Name']
        if my_name!="":
            list = Game.objects.filter(Name__startswith=my_name).order_by("Global_Sales")
    if 'Platform' in request.POST:
        my_pla=request.POST['Platform']
        if my_pla!="":
            list = list.filter(Platform=my_pla).order_by("Global_Sales")
        # for var in list:
        #     response += var.Name + " "+f"{var.id}"+'<br>'
        # ctx['Year'] = response


    if 'Year' in request.POST:
        my_year=request.POST['Year']
        if my_year=="":
            pass
        else:
            list = list.filter(Year=my_year).order_by("Global_Sales")
        # for var in list:
        #     response += var.Name + " "+f"{var.id}"+'<br>'
        # ctx['Year'] = response
    
    
    if 'Genre' in request.POST:
        G_list=["Sports","Platform","Racing","Role_Playing","Misc","Shooter","Simulation","Action","Puzzle","Fighting","Adventure","Stragegy"]
        my_Genre=request.POST['Genre']
        if my_Genre=="":
            pass
        else:
            list = list.filter(Genre=my_Genre).order_by("Global_Sales")
        # for var in list:
        #     response += var.Name + " "+f"{var.id}"+'<br>'
        # ctx['Year'] = response
    
    
    if 'Publisher' in request.POST:
        my_pub=request.POST['Publisher']
        if my_pub=="":
            pass
        else:
            list = list.filter(Publisher=my_pub).order_by("Global_Sales")
        # for var in list:
        #     response += var.Name + " "+f"{var.id}"+'<br>'
        # ctx['Publisher'] = response



    if 'Area' in request.POST:
        my_Area=request.POST['Area']
        if my_Area!="":
            list = list.order_by("-"+str(my_Area))
    







    for var in list:
        loop_ctx={}
        loop_ctx['id']=var.id
        loop_ctx['Name'] = var.Name
        loop_ctx['Platform']=var.Platform
        loop_ctx['Year']=var.Year
        loop_ctx['Genre']=var.Genre
        loop_ctx['Publisher']=var.Publisher
        loop_ctx['Developer']=var.Developer
        loop_ctx['Critic_Score']=var.Critic_Score
        loop_ctx['User_Score']=var.User_Score
        loop_ctx['NA_Sales']=var.NA_Sales
        loop_ctx['EU_Sales']=var.EU_Sales
        loop_ctx['JP_Sales']=var.JP_Sales
        loop_ctx['Other_Sales']=var.Other_Sales
        loop_ctx['Global_Sales']=var.Global_Sales
        loop_ctx['Card_image']=var.Card_image
        loop_ctx['Full_image']=var.Full_image
        ctx_list.append(loop_ctx) 








    ctx_json=json.dumps(ctx_list)
    print(ctx_json)
    ctx_show={}
    ctx_show['list']=ctx_json
    # return render(request, "plain_list.html", ctx_show)
    return HttpResponse(ctx_json)  

