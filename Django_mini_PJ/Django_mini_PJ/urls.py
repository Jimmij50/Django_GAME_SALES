from django.urls import path
# from django.conf.urls import url

# from Django_mini_PJ. import my_predict
 
from . import mylist,search_list,search_name,my_predict,platform_select
 
urlpatterns = [
    # path('runoob/', views.runoob),
    path('mylist/', mylist.get_my_list),
    path('search_list/', search_list.my_search_list),
    path('search_name/', search_name.search_name),
    path('predict/', my_predict.predict_list),
    path('platform_select/', platform_select.platform_select),
    
]