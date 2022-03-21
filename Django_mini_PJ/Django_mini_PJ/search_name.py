# -*- coding: utf-8 -*-
 
import json
from platform import platform
from django.shortcuts import render
from django.views.decorators import csrf
from django.http import HttpResponse
from GamesModel.models import Game
# from django.template.defaulttags import csrf_token 
from django.views.decorators.csrf import csrf_exempt 
# 接收POST请求数据
# @csrf_token
@csrf_exempt
def search_name(request):
    ctx ={}
    response="" 
    # list = Game.objects.all()

    if 'Name' in request.POST:
        my_name=request.POST['Name']
        list = Game.objects.filter(Name__startswith=my_name).order_by("id")
        for var in list:
            response += var.Name + " "+f"{var.id}"+'<br>'
        ctx['Name'] = response
    if 'id' in request.POST:
        my_id=request.POST['id']
        list = Game.objects.filter(id=my_id).order_by("id")
        # ll=["Name","Platform","Year","Genre","Publisher","NA_Sales","EU_Sales","JP_Sales","Other_Sales","Global_Sales"]
        for var in list:
            ctx['id']=var.id
            ctx['Name'] = var.Name
            ctx['Platform']=var.Platform
            ctx['Year']=var.Year
            ctx['Genre']=var.Genre
            ctx['Publisher']=var.Publisher
            ctx['Developer']=var.Developer
            ctx['Critic_Score']=var.Critic_Score
            ctx['User_Score']=var.User_Score
            ctx['NA_Sales']=var.NA_Sales
            ctx['EU_Sales']=var.EU_Sales
            ctx['JP_Sales']=var.JP_Sales
            ctx['Other_Sales']=var.Other_Sales
            ctx['Global_Sales']=var.Global_Sales
            ctx['Card_image']=var.Card_image
            ctx['Full_image']=var.Full_image
            
             
    ctx_json=json.dumps(ctx)
    return HttpResponse(ctx_json)  
    return render(request, "by_name.html", ctx)



