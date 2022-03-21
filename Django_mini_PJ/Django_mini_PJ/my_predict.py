# -*- coding: utf-8 -*-
 
# from http.client import HTTPResponse
from ast import Global
from django.http import HttpResponse
from platform import platform
from django.shortcuts import render
from django.views.decorators import csrf
from pymysql import NULL
from GamesModel.models import Game
import json
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
import matplotlib.pyplot as plt
from django.views.decorators.csrf import csrf_exempt 
# from django.template.defaulttags import csrf_token 
# 接收POST请求数据



#SKLEARN
def predict(x,y_all,area,degree_=1):


    x=np.reshape(x,(-1,1))
    y=y_all[area]
    y=np.reshape(y,(-1,1))

    #SKLEARN

    poly_reg=PolynomialFeatures(degree_)
    X_ploy=poly_reg.fit_transform(x)
    lin_reg=LinearRegression()
    lin_reg.fit(X_ploy,y)

    # y_pred=lin_reg.predict(X_ploy)
    yyy=np.array([[2019,2020,2021,2022,2023]])
    yyy=yyy.reshape(-1,1)
    X_new=poly_reg.fit_transform(yyy)
    final_pred=lin_reg.predict(X_new)
    final_pred=final_pred.reshape(final_pred.shape[0])
    ret_list=[]
    for i in final_pred:
        ret_list.append(float(i))
    return ret_list
    # plt.plot(x,y,c="red")
    # plt.plot(x,y_pred,c='blue')
    # plt.show()

# # @csrf_token
@csrf_exempt
def predict_list(request):
    ctx ={}
    ctx_list=[]
    response="" 
    my_pla="PS"
    my_area="Global_Sales"
    my_degree=1
    list = Game.objects.all()

    sales_all={"EU_Sales":np.zeros(34),"NA_Sales":np.zeros(34),"JP_Sales":np.zeros(34),"Other_Sales":np.zeros(34),"Global_Sales":np.zeros(34)}



    if 'Platform' in request.POST:
        my_pla=request.POST['Platform']
        if my_pla!="":
            list = list.filter(Platform=my_pla).order_by("Year")

    
    if 'Genre' in request.POST:
        my_Genre=request.POST['Genre']
        if my_Genre!="":
            list = list.filter(Genre=my_Genre).order_by("Year")
    
    
    if 'Publisher' in request.POST:
        my_pub=request.POST['Publisher']
        if my_pub!="":
            list = list.filter(Publisher=my_pub).order_by("Year")
    # if 'Area' in request.POST:
    #     my_area=request.POST['Area']
    if 'Degree' in request.POST:
        my_degree=request.POST['Degree']

    Year_x=a=np.linspace(1985,2018,34)
    
    Year_amount=np.zeros(34)
    # print(list)

    for var in list:
        for y in Year_x:
            if(int(var.Year)==int(y)):
                sales_all["EU_Sales"][int(y)-1985]+=var.EU_Sales
                sales_all["NA_Sales"][int(y)-1985]+=var.NA_Sales
                sales_all["JP_Sales"][int(y)-1985]+=var.JP_Sales
                sales_all["Other_Sales"][int(y)-1985]+=var.Other_Sales
                sales_all["Global_Sales"][int(y)-1985]+=var.Global_Sales
                Year_amount[int(y)-1985]+=1

    sales_all["EU_Sales"]/=Year_amount
    sales_all["NA_Sales"]/=Year_amount
    sales_all["JP_Sales"]/=Year_amount
    sales_all["Other_Sales"]/=Year_amount
    sales_all["Global_Sales"]/=Year_amount
    
    sales_all["EU_Sales"] [np.isnan(sales_all["EU_Sales"]) ]=0
    sales_all["NA_Sales"] [np.isnan( sales_all["NA_Sales"]) ]=0
    sales_all["JP_Sales"] [np.isnan(sales_all["JP_Sales"]) ]=0
    sales_all["Other_Sales"] [np.isnan(sales_all["Other_Sales"])]=0
    sales_all["Global_Sales"][np.isnan(sales_all["Global_Sales"])]=0

    pred_val={}
    area_list=["EU_Sales","NA_Sales","JP_Sales","Other_Sales","Global_Sales"] 
    ret_list={}

    # if my_area=="":
    #     my_area="Global_Sales"
    for i in area_list:
        pred_val[str(i)]=predict(Year_x,sales_all,str(i),int(my_degree));
        sales_all[str(i)]=sales_all[str(i)].tolist()
    ret_list["pred_val"]=pred_val
    

    ret_list["sale_list"]=sales_all
    
    # # for var in list:
    # #     loop_ctx={}
    # #     loop_ctx['Name'] = var.Name
    # #     loop_ctx['Platform']=var.Platform
    # #     loop_ctx['Year']=var.Year
    # #     loop_ctx['Genre']=var.Genre
    # #     loop_ctx['Publisher']=var.Publisher
    # # for i in area_list:
    # #     pred_val[str(i)]=predict(Year_x,sales_all,str(i),int(my_degree))
    # #     loop_ctx['Developer']=var.Developer
    # #     loop_ctx['Critic_Score']=var.Critic_Score
    # #     loop_ctx['User_Score']=var.User_Score
    # #     loop_ctx['NA_Sales']=var.NA_Sales
    # #     loop_ctx['EU_Sales']=var.EU_Sales
    # #     loop_ctx['JP_Sales']=var.JP_Sales
    # #     ctx_list.append(loop_ctx) 
    
    
    # # ctx_json=json.dumps(sales_all["EU_Sales"].tolist())
    # ctx_show={}

    # print(ret_list)
    ret_list_json=json.dumps(ret_list)
    # ctx_show['list']=ret_list_json
    # return HttpResponse(ctx_json_list)  
    return HttpResponse(ret_list_json)  
    # return render(request, "predict.html", ctx_show)

