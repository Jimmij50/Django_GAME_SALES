from django.db import models

# Create your models here.
from django.db import models
 
class Game(models.Model):
    # id=models.IntegerField()
    Name=models.CharField(max_length=200)
    Platform=models.CharField(max_length=200)
    Year=models.IntegerField()
    Genre=models.CharField(max_length=200)
    Publisher=models.CharField(max_length=200)
    Developer=models.CharField(max_length=200)
    Critic_Score=models.FloatField()
    User_Score=models.FloatField()
    NA_Sales=models.FloatField()
    EU_Sales=models.FloatField()
    JP_Sales=models.FloatField()
    Other_Sales=models.FloatField()
    Global_Sales=models.FloatField()
    Card_image=models.CharField(max_length=200)
    Full_image=models.CharField(max_length=200)
    class Meta:
        db_table = "games1"