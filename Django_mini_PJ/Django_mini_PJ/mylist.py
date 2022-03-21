# -*- coding: utf-8 -*-
# Sort the games by sale number in specific genre, platform 
from telnetlib import GA
from django.http import HttpResponse
 
from GamesModel.models import Game
 
# 数据库操作
def get_my_list(request):
    # 初始化
    response = ""
    response1 = ""
    
    
    
    # 通过objects这个模型管理器的all()获得所有数据行，相当于SQL中的SELECT * FROM
    list = Game.objects.all()
        
    # filter相当于SQL中的WHERE，可设置条件过滤结果
    response2 = Game.objects.filter(id=1) 
    
    # 获取单个对象
    response3 = Game.objects.get(id=1) 
    
    # 限制返回的数据 相当于 SQL 中的 OFFSET 0 LIMIT 2;
    # Test.objects.order_by('name')[0:2]
    
    #数据排序
    Game.objects.order_by("id")
    
    # 上面的方法可以连锁使用
    list = Game.objects.filter(Year=2008).order_by("id")
    
    # 输出所有数据
    for var in list[0:10000]:
        response1 += var.Name + " "f"{var.id}"+"<br>"
    response = response1
    #return HttpResponse("<p>" + response + "</p>")
    return HttpResponse("hello")