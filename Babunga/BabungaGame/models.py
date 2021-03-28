from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.
class profession(models.Model):
    name = models.CharField(max_length=20)
    baseHp = models.IntegerField()
    baseAttack = models.IntegerField()
    baseArmor = models.IntegerField()
    Attack_per_lvl = models.IntegerField()
    HP_per_lvl = models.IntegerField()
    Armor_per_lvl = models.IntegerField()
    image = models.ImageField(upload_to="media/images/profession")
class itemType(models.Model):
    name = models.CharField(max_length=32)

class itemClass(models.Model):
    name = models.CharField(max_length=32)

class item(models.Model):
    name = models.CharField(max_length=126)
    type = models.ForeignKey(itemType,on_delete=models.CASCADE)
    it_class = models.ForeignKey(itemClass,on_delete=models.CASCADE)
    image = models.ImageField(upload_to="media/images/items")
    Attack = models.IntegerField()
    Armor = models.IntegerField()
    HP = models.IntegerField()

class in_game_item(models.Model):
    new_item = models.ForeignKey(item,on_delete=models.CASCADE)
    drop_date = models.DateTimeField(auto_now_add=True)

class player(models.Model):
    login = models.ForeignKey(User, on_delete=models.CASCADE)
    profession = models.ForeignKey(profession,on_delete=models.CASCADE)
    image = models.ForeignKey(item,on_delete=models.CASCADE)
    Money = models.IntegerField()
    Lvl = models.IntegerField()
    HP = models.IntegerField()
    Attack = models.IntegerField()
    Weapon = models.IntegerField()
    Armour = models.IntegerField()
    Boots = models.IntegerField()
    Necklace = models.IntegerField()
    Ring = models.IntegerField()
    Shield = models.IntegerField()
    Energy = models.IntegerField()


class bag(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    slot_1 = models.ForeignKey(in_game_item, on_delete=models.CASCADE,null=True, blank=True,related_name='slot_1')
    slot_2 = models.ForeignKey(in_game_item, on_delete=models.CASCADE, null=True, blank=True,related_name='slot_2')
    slot_3 = models.ForeignKey(in_game_item, on_delete=models.CASCADE, null=True, blank=True,related_name='slot_3')
    slot_4 = models.ForeignKey(in_game_item, on_delete=models.CASCADE, null=True, blank=True,related_name='slot_4')
    slot_5 = models.ForeignKey(in_game_item, on_delete=models.CASCADE, null=True, blank=True,related_name='slot_5')
    slot_6 = models.ForeignKey(in_game_item, on_delete=models.CASCADE, null=True, blank=True,related_name='slot_6')
    slot_7 = models.ForeignKey(in_game_item, on_delete=models.CASCADE, null=True, blank=True,related_name='slot_7')
    slot_8 = models.ForeignKey(in_game_item, on_delete=models.CASCADE, null=True, blank=True,related_name='slot_8')
    slot_9 = models.ForeignKey(in_game_item, on_delete=models.CASCADE, null=True, blank=True,related_name='slot_9')
    slot_10 = models.ForeignKey(in_game_item, on_delete=models.CASCADE, null=True, blank=True,related_name='slot_10')
    slot_11 = models.ForeignKey(in_game_item, on_delete=models.CASCADE, null=True, blank=True,related_name='slot_11')
    slot_12 = models.ForeignKey(in_game_item, on_delete=models.CASCADE, null=True, blank=True,related_name='slot_12')
    slot_13 = models.ForeignKey(in_game_item, on_delete=models.CASCADE, null=True, blank=True,related_name='slot_13')
    slot_14 = models.ForeignKey(in_game_item, on_delete=models.CASCADE, null=True, blank=True,related_name='slot_14')
    slot_15 = models.ForeignKey(in_game_item, on_delete=models.CASCADE, null=True, blank=True,related_name='slot_15')
    slot_16 = models.ForeignKey(in_game_item, on_delete=models.CASCADE, null=True, blank=True,related_name='slot_16')
    slot_17 = models.ForeignKey(in_game_item, on_delete=models.CASCADE, null=True, blank=True,related_name='slot_17')
    slot_18 = models.ForeignKey(in_game_item, on_delete=models.CASCADE, null=True, blank=True,related_name='slot_18')
    slot_19 = models.ForeignKey(in_game_item, on_delete=models.CASCADE, null=True, blank=True,related_name='slot_19')
    slot_20 = models.ForeignKey(in_game_item, on_delete=models.CASCADE, null=True, blank=True,related_name='slot_20')
    slot_21 = models.ForeignKey(in_game_item, on_delete=models.CASCADE, null=True, blank=True,related_name='slot_21')
    slot_22 = models.ForeignKey(in_game_item, on_delete=models.CASCADE, null=True, blank=True,related_name='slot_22')
    slot_23 = models.ForeignKey(in_game_item, on_delete=models.CASCADE, null=True, blank=True,related_name='slot_23')
    slot_24 = models.ForeignKey(in_game_item, on_delete=models.CASCADE, null=True, blank=True,related_name='slot_24')
    slot_25 = models.ForeignKey(in_game_item, on_delete=models.CASCADE, null=True, blank=True,related_name='slot_25')
    slot_26 = models.ForeignKey(in_game_item, on_delete=models.CASCADE, null=True, blank=True,related_name='slot_26')
    slot_27 = models.ForeignKey(in_game_item, on_delete=models.CASCADE, null=True, blank=True,related_name='slot_27')
    slot_28 = models.ForeignKey(in_game_item, on_delete=models.CASCADE, null=True, blank=True,related_name='slot_28')
    slot_29 = models.ForeignKey(in_game_item, on_delete=models.CASCADE, null=True, blank=True,related_name='slot_29')
    slot_30 = models.ForeignKey(in_game_item, on_delete=models.CASCADE, null=True, blank=True,related_name='slot_30')

class monster(models.Model):
    Name = models.CharField(max_length=35)
    HP = models.IntegerField()
    Armour = models.IntegerField()
    Attack = models.IntegerField()
    Image = models.ImageField(upload_to="media/images/monsters")

class aukcje(models.Model):
    item = models.ForeignKey(in_game_item,on_delete=models.CASCADE)
    price = models.IntegerField()

class loot(models.Model):
    monster = models.ForeignKey(monster, on_delete=models.CASCADE)
    min_value = models.IntegerField()
    max_value = models.IntegerField()
    item = models.ForeignKey(item,on_delete=models.CASCADE)











