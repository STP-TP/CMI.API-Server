from django.db import models
from CMI_Define.sql_define import *


class attributetbl(models.Model):
    locals()[ATTRIBUTE_ID] = models.CharField(max_length=35)
    locals()[ATTRIBUTE_NAME] = models.CharField(max_length=20)
    locals()[ATTRIBUTE_EXPLAIN] = models.CharField(max_length=255)
    locals()[POSITION_NAME] = models.CharField(max_length=15)


class charactertbl(models.Model):
    locals()[CHARACTER_ID] = models.CharField(max_length=35)
    locals()[CHARACTER_NAME] = models.CharField(max_length=30)


class itemtbl(models.Model):
    locals()[ITEM_ID] = models.CharField(max_length=35)
    locals()[ITEM_NAME] = models.CharField(max_length=15)
    locals()[CHARACTER_ID] = models.CharField(max_length=35)
    locals()[SLOT_CODE] = models.SmallIntegerField(default=0)
    locals()[SLOT_NAME] = models.CharField(max_length=10)
    locals()[RARITY_CODE] = models.SmallIntegerField(default=0)
    locals()[RARITY_NAME] = models.CharField(max_length=4)
    locals()[SEASON_CODE] = models.CharField(max_length=10)
    locals()[SEASON_NAME] = models.CharField(max_length=20)
    locals()[ITEM_EXPLAIN] = models.CharField(max_length=255)
    locals()[ITEM_EXPLAIN_DETAIL] = models.CharField(max_length=255)


class matchtbl(models.Model):
    locals()[DATE] = models.DateTimeField()
    locals()[MATCH_ID] = models.CharField(max_length=70)
    locals()[MAP_ID] = models.CharField(max_length=3)
    locals()[MAP_NAME] = models.CharField(max_length=20)
    locals()[GAME_TYPE_ID] = models.CharField(max_length=8)


class match_detailtbl(models.Model):
    locals()[MAP_ID] = models.CharField(max_length=255)
    locals()[PLAYER_ID] = models.CharField(max_length=255)
    locals()[RESULT] = models.CharField(max_length=255)
    locals()[RANDOM] = models.BooleanField()
    locals()[PARTY_USER_COUNT] = models.BooleanField()
    locals()[CHARACTER_ID] = models.CharField(max_length=35)
    locals()[LEVEL] = models.SmallIntegerField(default=0)
    locals()[KILL_COUNT] = models.SmallIntegerField(default=0)
    locals()[DEATH_COUNT] = models.SmallIntegerField(default=0)
    locals()[ASSIST_COUNT] = models.SmallIntegerField(default=0)
    locals()[ATTACK_POINT] = models.IntegerField(default=0)
    locals()[DAMAGE_POINT] = models.IntegerField(default=0)
    locals()[BATTLE_POINT] = models.IntegerField(default=0)
    locals()[SIGHT_POINT] = models.IntegerField(default=0)
    locals()[PLAY_TIME] = models.SmallIntegerField(default=0)
    locals()[POSITION_NAME] = models.CharField(max_length=15)
    locals()[ATTRIBUTE_ID_LV1] = models.CharField(max_length=35)
    locals()[ATTRIBUTE_ID_LV2] = models.CharField(max_length=35)
    locals()[ATTRIBUTE_ID_LV3] = models.CharField(max_length=35)
    locals()[ITEM_101] = models.CharField(max_length=35)
    locals()[ITEM_102] = models.CharField(max_length=35)
    locals()[ITEM_103] = models.CharField(max_length=35)
    locals()[ITEM_104] = models.CharField(max_length=35)
    locals()[ITEM_105] = models.CharField(max_length=35)
    locals()[ITEM_106] = models.CharField(max_length=35)
    locals()[ITEM_107] = models.CharField(max_length=35)
    locals()[ITEM_202] = models.CharField(max_length=35)
    locals()[ITEM_203] = models.CharField(max_length=35)
    locals()[ITEM_204] = models.CharField(max_length=35)
    locals()[ITEM_205] = models.CharField(max_length=35)
    locals()[ITEM_301] = models.CharField(max_length=35)
    locals()[ITEM_302] = models.CharField(max_length=35)
    locals()[ITEM_303] = models.CharField(max_length=35)
    locals()[ITEM_304] = models.CharField(max_length=35)
    locals()[ITEM_305] = models.CharField(max_length=35)


class positiontbl(models.Model):
    locals()[POSITION_NAME] = models.CharField(max_length=15)
    locals()[POSITION_EXPLAIN] = models.CharField(max_length=50)


class search_datetbl(models.Model):
    locals()[TIER_NAME] = models.CharField(max_length=10)
    locals()[PAST_DATE] = models.DateTimeField()
    locals()[RECENT_DATE] = models.DateTimeField()


class usertbl(models.Model):
    locals()[PLAYER_ID] = models.CharField(max_length=35)
    locals()[NICKNAME] = models.CharField(max_length=20)
    locals()[GRADE] = models.SmallIntegerField(default=0)
    locals()[CLAN_NAME] = models.CharField(max_length=10)
    locals()[RATING_POINT] = models.SmallIntegerField(default=0)
    locals()[MAX_RATING_POINT] = models.SmallIntegerField(default=0)
    locals()[TIER_NAME] = models.CharField(max_length=10)
    locals()[RATING_WIN] = models.IntegerField(default=0)
    locals()[RATING_LOSE] = models.IntegerField(default=0)
    locals()[RATING_STOP] = models.IntegerField(default=0)
    locals()[NORMAL_WIN] = models.IntegerField(default=0)
    locals()[NORMAL_LOSE] = models.IntegerField(default=0)
    locals()[NORMAL_STOP] = models.IntegerField(default=0)
