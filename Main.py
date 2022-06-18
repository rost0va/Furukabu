import os
import math
import sys

from PlayerDict import PlayerDict
from MoveDict import MoveDict
from EquipDict import EquipDict

UserNameOffset = 0x4C0;
PrestigePointsOffset = 0x4D4;
FriendshipPointsOffset = 0x4D8;
TotalPlaytimeOffset = 0x4DC;
PlayerOffset = 0x11B0;
length = 0x6C;
PlayerPlace = 57;  ##←←Set the number of player place you want to get info
TotalMember = 90;  ##←←This value can read by reading .dat automatically

def byte2txt(a):
   x = a.decode('shift_jis')
   y = x.replace('\0', '')
   return y

def byte2int(a):
   x = bytes.fromhex(a)[::-1].hex()
   y = int(x,16)
   return y

def byte2hex(a):
   x = bytes.fromhex(a)[::-1].hex()
   y = hex(int(x,16))
   return y

def hex2int(a: str) -> int:
    if int(a[0], 16) < 8:  # plus
        x = int(a, 16)
    else:  # minus
        x = int(a, 16) - pow(16, len(a))
    return x

def movelv(a,b,c):
    if a == '真':
        if b == '早':
            if c <= 5:
                return ' '
            elif 6 <= c <= 20:
                return '改'
            elif 21 <= c:
                return '真'
        elif b == '普': 
            if c <= 8:
                return ' '
            elif 9 <= c <= 26:
                return '改'
            elif 27 <= c:
                return '真'
        elif b == '晩': 
            if c <= 14:
                return ' '
            elif 15 <= c <= 32:
                return '改'
            elif 33 <= c:
                return '真'
    elif a == 'V':
        if b == '早':
            if c <= 5:
                return ' '
            elif 6 <= c <= 20:
                return 'V2'
            elif 21 <= c:
                return 'V3'
        elif b == '普': 
            if c <= 8:
                return ''
            elif 9 <= c <= 26:
                return 'V2'
            elif 27 <= c:
                return 'V3'
        elif b == '晩': 
            if c <= 14:
                return ' '
            elif 15 <= c <= 32:
                return 'V2'
            elif 33 <= c:
                return 'V3'
    elif a == 'G':
        if b == '早':
            if c <= 14:
                return ''
            elif 15 <= c <= 34:
                return 'G2'
            elif 35 <= c <= 54:
                return 'G3'
            elif 55 <= c <= 79:
                return 'G4'
            elif 80 <= c:
                return 'G5'
        elif b == '普': 
            if c <= 19:
                return ''
            elif 20 <= c <= 39:
                return 'G2'
            elif 40 <= c <= 59:
                return 'G3'
            elif 59 <= c <= 89:
                return 'G4'
            elif 90 <= c:
                return 'G5'
        elif b == '晩': 
            if c <= 19:
                return ' '
            elif 20 <= c <= 44:
                return 'G2'
            elif 45 <= c <= 69:
                return 'G3'
            elif 70 <= c <= 99:
                return 'G4'
            elif 100 <= c:
                return 'G5'
    else:
        return ' '
                
def get_player():
	with open('ina3O_save.dat','rb') as f:
	   PlayerInfo = []
   
	   f.seek(PlayerOffset+length*PlayerPlace, os.SEEK_SET)
	   exp_h = f.read(4).hex()
	   exp = byte2int(exp_h)
	   chara_h = f.read(2).hex()
	   charaID = byte2hex(chara_h)
	   charaName = PlayerDict[charaID][1]
	   goals_h = f.read(2).hex()
	   goals = byte2int(goals_h)
   
	   f.seek(0x2, os.SEEK_CUR)
	   played_h = f.read(2).hex()
	   playedGame = byte2int(played_h)
   
	   f.seek(0x4, os.SEEK_CUR)
	   eqp1_h = f.read(2).hex()
	   eqp1ID = byte2hex(eqp1_h)
	   eqp1Name = EquipDict[eqp1ID][0]
	   eqp2_h = f.read(2).hex()
	   eqp2ID = byte2hex(eqp2_h)
	   eqp2Name = EquipDict[eqp2ID][0]
	   eqp3_h = f.read(2).hex()
	   eqp3ID = byte2hex(eqp3_h)
	   eqp3Name = EquipDict[eqp3ID][0]
   
	   f.seek(0x2, os.SEEK_CUR)
	   GP_h = f.read(2).hex()
	   GPpoint = byte2int(GP_h)
	   GP = GPpoint+PlayerDict[charaID][2]
	   TP_h = f.read(2).hex()
	   TPpoint = byte2int(TP_h)
	   TP = TPpoint+PlayerDict[charaID][3]+EquipDict[eqp2ID][3]+EquipDict[eqp3ID][3]
   
	   f.seek(0x1C, os.SEEK_CUR)
	   move1 = f.read(2).hex()
	   move1ID = byte2hex(move1)
	   move1Name = MoveDict[move1ID][0]
	   move2 = f.read(2).hex()
	   move2ID = byte2hex(move2)
	   move2Name = MoveDict[move2ID][0]
	   move3 = f.read(2).hex()
	   move3ID = byte2hex(move3)
	   move3Name = MoveDict[move3ID][0]
	   move4 = f.read(2).hex()
	   move4ID = byte2hex(move4)
	   move4Name = MoveDict[move4ID][0]
	   move5 = f.read(2).hex()
	   move5ID = byte2hex(move5)
	   move5Name = MoveDict[move5ID][0]
	   move6 = f.read(2).hex()
	   move6ID = byte2hex(move6)
	   move6Name = MoveDict[move6ID][0]   
	   m1Times_h = f.read(1).hex()
	   m1TimesUsed = int(m1Times_h,16)
	   move1Lv = movelv(MoveDict[move1ID][6], MoveDict[move1ID][7], m1TimesUsed)
	   m2Times_h = f.read(1).hex()
	   m2TimesUsed = int(m2Times_h,16)
	   move2Lv = movelv(MoveDict[move2ID][6], MoveDict[move2ID][7], m2TimesUsed)
	   m3Times_h = f.read(1).hex()
	   m3TimesUsed = int(m3Times_h,16)
	   move3Lv = movelv(MoveDict[move3ID][6], MoveDict[move3ID][7], m3TimesUsed)
	   m4Times_h = f.read(1).hex()
	   m4TimesUsed = int(m4Times_h,16)
	   move4Lv = movelv(MoveDict[move4ID][6], MoveDict[move4ID][7], m4TimesUsed)	   
	   m5Times_h = f.read(1).hex()
	   m5TimesUsed = int(m5Times_h,16)
	   move5Lv = movelv(MoveDict[move5ID][6], MoveDict[move5ID][7], m5TimesUsed)	   
	   m6Times_h = f.read(1).hex()
	   m6TimesUsed = int(m6Times_h,16)
	   move6Lv = movelv(MoveDict[move6ID][6], MoveDict[move6ID][7], m6TimesUsed)
   
	   level_h = f.read(1).hex()
	   level = int(level_h,16)
	   
	   f.seek(0x4, os.SEEK_CUR)
	   kick_h = f.read(1).hex()
	   kickPoint = hex2int(kick_h)
	   kick = kickPoint+PlayerDict[charaID][4]+EquipDict[eqp1ID][4]
	   body_h = f.read(1).hex()
	   bodyPoint = hex2int(body_h)
	   body = bodyPoint+PlayerDict[charaID][5]+EquipDict[eqp2ID][5]+EquipDict[eqp3ID][5]
	   guard_h = f.read(1).hex()
	   guardPoint = hex2int(guard_h)
	   guard = guardPoint+PlayerDict[charaID][7]
	   control_h = f.read(1).hex()
	   controlPoint = hex2int(control_h)
	   control = controlPoint+PlayerDict[charaID][6]+EquipDict[eqp2ID][6]+EquipDict[eqp3ID][6]
	   speed_h = f.read(1).hex()
	   speedPoint = hex2int(speed_h)
	   speed = speedPoint+PlayerDict[charaID][8]+EquipDict[eqp1ID][8]
	   guts_h = f.read(1).hex()
	   gutsPoint = hex2int(guts_h)
	   guts = gutsPoint+PlayerDict[charaID][10]+EquipDict[eqp2ID][10]+EquipDict[eqp3ID][10]
	   stamina_h = f.read(1).hex()
	   staminaPoint = hex2int(stamina_h)
	   stamina = staminaPoint+PlayerDict[charaID][9]+EquipDict[eqp2ID][9]+EquipDict[eqp3ID][9]
	   
	   PlayerInfo.append(charaName)
	   PlayerInfo.append(goals)
	   PlayerInfo.append(playedGame)
	   PlayerInfo.append(exp)
	   PlayerInfo.append(level)
	   PlayerInfo.append(GP)
	   PlayerInfo.append(TP)
	   PlayerInfo.append(kick)
	   PlayerInfo.append(body)
	   PlayerInfo.append(control)
	   PlayerInfo.append(guard)
	   PlayerInfo.append(speed)
	   PlayerInfo.append(stamina)
	   PlayerInfo.append(guts)
	   PlayerInfo.append(move1Name)
	   PlayerInfo.append(move2Name)
	   PlayerInfo.append(move3Name)
	   PlayerInfo.append(move4Name)
	   PlayerInfo.append(move5Name)
	   PlayerInfo.append(move6Name)
	   PlayerInfo.append(move1Lv)
	   PlayerInfo.append(move2Lv)
	   PlayerInfo.append(move3Lv)
	   PlayerInfo.append(move4Lv)
	   PlayerInfo.append(move5Lv)
	   PlayerInfo.append(move6Lv)
	   PlayerInfo.append(eqp1Name)
	   PlayerInfo.append(eqp2Name)
	   PlayerInfo.append(eqp3Name)
	return PlayerInfo

def get_member():   
	with open('ina3O_save.dat','rb') as f:
	   Memberlist = []
	   
	   f.seek(PlayerOffset+4, os.SEEK_SET)
	   for i in range(TotalMember):
	   	  chara_h = f.read(2).hex()
	   	  charaID = byte2hex(chara_h)
	   	  name = PlayerDict[charaID][1]
	   	  Memberlist.append(name)
	   	  f.seek(0x6C-2, os.SEEK_CUR)
	   return Memberlist

def get_userdata():	
	with open('ina3O_save.dat','rb') as f:
	   UserSaveInfo = []
	   
	   f.seek(0x74, os.SEEK_SET)
	   team_h = f.read(16)
	   team = byte2txt(team_h)
   
	   f.seek(UserNameOffset, os.SEEK_SET)
	   name_h = f.read(16)
	   name = byte2txt(name_h)
   
	   f.seek(PrestigePointsOffset, os.SEEK_SET)
	   pp_h = f.read(4).hex()
	   PrestigePoints = byte2int(pp_h)
	   fp_h = f.read(4).hex()
	   FriendshipPoints = byte2int(fp_h)
	   pt_h = f.read(4).hex()
	   pt = byte2int(pt_h)
	   m,h = math.modf(pt/216000)
	   Hours = int(h)
	   Minutes = int(m*60)
	   
	   UserSaveInfo.append(name)
	   UserSaveInfo.append(PrestigePoints)
	   UserSaveInfo.append(FriendshipPoints)
	   UserSaveInfo.append(Hours)
	   UserSaveInfo.append(Minutes)
	   UserSaveInfo.append(team)
	   
	   return UserSaveInfo

a = get_player()
b = get_member()
c = get_userdata()
print(a)
print(b)
print(c)