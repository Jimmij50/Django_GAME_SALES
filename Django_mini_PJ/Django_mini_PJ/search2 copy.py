# -*- coding: utf-8 -*-
 
from platform import platform
from django.shortcuts import render
from django.views.decorators import csrf
from GamesModel.models import Game
 
# 接收POST请求数据
def search_list(request):
    ctx ={}
    response="" 
    # list = Game.objects.all()


    if 'Platform' in request.POST:
        my_pla=request.POST['Platform']
        list = Game.objects.filter(Platform=my_pla).order_by("id")
        for var in list:
            response += var.Name + " "+f"{var.id}"+'<br>'
        ctx['Year'] = response


    if 'Year' in request.POST:
        my_year=request.POST['Year']
        list = Game.objects.filter(Year=my_year).order_by("id")
        for var in list:
            response += var.Name + " "+f"{var.id}"+'<br>'
        ctx['Year'] = response
    
    
    if 'Genre' in request.POST:
        G_list=["Sports","Platform","Racing","Role_Playing","Misc","Shooter","Simulation","Action","Puzzle","Fighting","Adventure","Stragegy"]
        my_Genre=request.POST['Genre']
        list = Game.objects.filter(Genre=my_Genre).order_by("id")
        for var in list:
            response += var.Name + " "+f"{var.id}"+'<br>'
        ctx['Year'] = response
    
    
    if 'Publisher' in request.POST:
        my_pub=request.POST['Publisher']
        list = Game.objects.filter(Publisher=my_pub).order_by("id")
        for var in list:
            response += var.Name + " "+f"{var.id}"+'<br>'
        ctx['Publisher'] = response



    if 'NA_Sales' in request.POST:
        list = Game.objects.all().order_by("-NA_Sales")
        for var in list:
            response += var.Name +" "+ f"{var.NA_Sales}"+" "+"<br>"
        ctx['NA_Sales'] = response


    if 'EU_Sales' in request.POST:
        list = Game.objects.order_by("-EU_Sales")
        for var in list:
            response += var.Name + f"{var.EU_Sales}"+" "+f"{var.id}"+'<br>'
        ctx['EU_Sales'] = response

    if 'JP_Sales' in request.POST:
        list = Game.objects.order_by("-JP_Sales")
        for var in list:
            response += var.Name + f"{var.JP_Sales}"+" "+f"{var.id}"+'<br>'
        ctx['JP_Sales'] = response
    
    
    if 'Other_Sales' in request.POST:
        list = Game.objects.order_by("-Other_Sales")
        for var in list:
            response += var.Name + f"{var.Other_Sales}"+" "+f"{var.id}"+'<br>'
        ctx['Other_Sales'] = response

    if 'Global_Sales' in request.POST:
        list = Game.objects.order_by("-Global_Sales")
        for var in list:
            response += var.Name + f"{var.Global_Sales}"+" "+f"{var.id}"+'<br>'
        ctx['Global_Sales'] = response
    
    return render(request, "list.html", ctx)
