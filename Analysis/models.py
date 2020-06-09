from django.db import models


# Create your models here.
class Analysis(models.Model):
    name = models.CharField(max_length=200)
    mail = models.CharField(max_length=200)
    age = models.IntegerField(default=0)

class attributetbl(models.Model):
    attributeID = models.CharField(max_length=35)
    attributeName = models.CharField(max_length=20)
    attributeExplain = models.CharField(max_length=255)
    positionName = models.CharField(max_length=15)

class charactertbl(models.Model):
    characterID = models.CharField(max_length=35)
    characterName = models.CharField(max_length=30)

class itemtbl(models.Model):
    itemID = models.CharField(max_length=35)
    itemName = models.CharField(max_length=15)
    characterId = models.CharField(max_length=35)
    slotCode = models.SmallIntegerField(default=0)
    slotName = models.CharField(max_length=10)
    rarityCode = models.SmallIntegerField(default=0)
    rarityName = models.CharField(max_length=4)
    seasonCode = models.CharField(max_length=10)
    seasonName = models.CharField(max_length=20)
    explain = models.CharField(max_length=255)
    explainDetail = models.CharField(max_length=255)

class matchtbl(models.Model):
    date = models.DateTimeField()
    matchID = models.CharField(max_length=70)
    mapID = models.CharField(max_length=3)
    mapName = models.CharField(max_length=20)
    gametypeID = models.CharField(max_length=8)

class match_detailtbl(models.Model):
    matchID = models.CharField(max_length=255)
    playerID = models.CharField(max_length=255)
    result = models.CharField(max_length=255)
    random = models.BooleanField()
    partyUserCount = models.BooleanField()
    characterID = models.CharField(max_length=35)
    level = models.SmallIntegerField(default=0)
    killCount = models.SmallIntegerField(default=0)
    deathCount = models.SmallIntegerField(default=0)
    assistCount = models.SmallIntegerField(default=0)
    attackPoint = models.IntegerField(default=0)
    damagePoint = models.IntegerField(default=0)
    battlePoint = models.IntegerField(default=0)
    sightPoint = models.IntegerField(default=0)
    playTime = models.SmallIntegerField(default=0)
    positionName = models.CharField(max_length=15)
    attributeID_lv1 = models.CharField(max_length=35)
    attributeID_lv2 = models.CharField(max_length=35)
    attributeID_lv3 = models.CharField(max_length=35)
    item_101 = models.CharField(max_length=35)
    item_102 = models.CharField(max_length=35)
    item_103 = models.CharField(max_length=35)
    item_104 = models.CharField(max_length=35)
    item_105 = models.CharField(max_length=35)
    item_106 = models.CharField(max_length=35)
    item_107 = models.CharField(max_length=35)
    item_202 = models.CharField(max_length=35)
    item_203 = models.CharField(max_length=35)
    item_204 = models.CharField(max_length=35)
    item_205 = models.CharField(max_length=35)
    item_301 = models.CharField(max_length=35)
    item_302 = models.CharField(max_length=35)
    item_303 = models.CharField(max_length=35)
    item_304 = models.CharField(max_length=35)
    item_305 = models.CharField(max_length=35)

class positiontbl(models.Model):
    positionName = models.CharField(max_length=15)
    positionExplain = models.CharField(max_length=50)

class search_datetbl(models.Model):
    tierName = models.CharField(max_length=10)
    past_date = models.DateTimeField()
    recent_date = models.DateTimeField()

class usertbl(models.Model):
    playerID = models.CharField(max_length=35)
    nickname = models.CharField(max_length=20)
    grade = models.SmallIntegerField(default=0)
    clanName = models.CharField(max_length=10)
    ratingPoint = models.SmallIntegerField(default=0)
    maxRatingPoint = models.SmallIntegerField(default=0)
    tierName = models.CharField(max_length=10)
    ratingWin = models.IntegerField(default=0)
    ratingLose = models.IntegerField(default=0)
    ratingStop = models.IntegerField(default=0)
    normalWin = models.IntegerField(default=0)
    normalLose = models.IntegerField(default=0)
    normalStop = models.IntegerField(default=0)
