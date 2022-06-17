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
PlayerPlace = 57;
TotalMember = 80;

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
                
              

with open('.dat','rb') as f:
   f.seek(0x74, os.SEEK_SET)
   team_h = f.read(16)
   team = byte2txt(team_h)
   print(team)
   
with open('.dat','rb') as f:
   UserSaveInfo = []
   
   f.seek(UserNameOffset, os.SEEK_SET)
   name_h = f.read(16)
   name = byte2txt(name_h)
   UserSaveInfo.append(name)
   
   f.seek(PrestigePointsOffset, os.SEEK_SET)
   
   pp_h = f.read(4).hex()
   PrestigePoints = byte2int(pp_h)
   UserSaveInfo.append(PrestigePoints)
   
   fp_h = f.read(4).hex()
   FriendshipPoints = byte2int(fp_h)
   UserSaveInfo.append(FriendshipPoints)
   
   pt_h = f.read(4).hex()
   pt = byte2int(pt_h)
   m,h = math.modf(pt/216000)
   Hours = int(h)
   Minutes = int(m*60)
   UserSaveInfo.append(Hours)
   UserSaveInfo.append(Minutes)
   
   print(UserSaveInfo)

   PlayerInfo = []
   
   f.seek(PlayerOffset+length*PlayerPlace, os.SEEK_SET)
   
   exp_h = f.read(4).hex()
   exp = byte2int(exp_h)
   PlayerInfo.append(exp)
   
   chara_h = f.read(2).hex()
   charaID = byte2hex(chara_h)
   PlayerInfo.append(charaID)
   
   goals_h = f.read(2).hex()
   goals = byte2int(goals_h)
   PlayerInfo.append(goals)
   
   f.seek(0x2, os.SEEK_CUR)
   
   played_h = f.read(2).hex()
   playedGame = byte2int(played_h)
   PlayerInfo.append(playedGame)
   
   f.seek(0x4, os.SEEK_CUR)
   
   eqp1_h = f.read(2).hex()
   eqp1ID = byte2hex(eqp1_h)
   PlayerInfo.append(eqp1ID)
   eqp2_h = f.read(2).hex()
   eqp2ID = byte2hex(eqp2_h)
   PlayerInfo.append(eqp2ID)
   eqp3_h = f.read(2).hex()
   eqp3ID = byte2hex(eqp3_h)
   PlayerInfo.append(eqp3ID)
   
   f.seek(0x2, os.SEEK_CUR)
   
   GP_h = f.read(2).hex()
   GPpoint = byte2int(GP_h)
   TP_h = f.read(2).hex()
   TPpoint = byte2int(TP_h)
   
   f.seek(0x1C, os.SEEK_CUR)
   
   move1 = f.read(2).hex()
   move1ID = byte2hex(move1)
   PlayerInfo.append(move1ID)
   move2 = f.read(2).hex()
   move2ID = byte2hex(move2)
   PlayerInfo.append(move2ID)
   move3 = f.read(2).hex()
   move3ID = byte2hex(move3)
   PlayerInfo.append(move3ID)
   move4 = f.read(2).hex()
   move4ID = byte2hex(move4)
   PlayerInfo.append(move4ID)
   move5 = f.read(2).hex()
   move5ID = byte2hex(move5)
   PlayerInfo.append(move5ID)
   move6 = f.read(2).hex()
   move6ID = byte2hex(move6)
   PlayerInfo.append(move6ID)
   
   m1Times_h = f.read(1).hex()
   m1TimesUsed = int(m1Times_h,16)
   PlayerInfo.append(m1TimesUsed)
   m2Times_h = f.read(1).hex()
   m2TimesUsed = int(m2Times_h,16)
   PlayerInfo.append(m2TimesUsed)
   m3Times_h = f.read(1).hex()
   m3TimesUsed = int(m3Times_h,16)
   PlayerInfo.append(m3TimesUsed)
   m4Times_h = f.read(1).hex()
   m4TimesUsed = int(m4Times_h,16)
   PlayerInfo.append(m4TimesUsed)
   m5Times_h = f.read(1).hex()
   m5TimesUsed = int(m5Times_h,16)
   PlayerInfo.append(m5TimesUsed)
   m6Times_h = f.read(1).hex()
   m6TimesUsed = int(m6Times_h,16)
   PlayerInfo.append(m6TimesUsed)
   
   level_h = f.read(1).hex()
   level = int(level_h,16)
   PlayerInfo.append(level)
   
   f.seek(0x4, os.SEEK_CUR)
   
   kick_h = f.read(1).hex()
   kickPoint = hex2int(kick_h)
   body_h = f.read(1).hex()
   bodyPoint = hex2int(body_h)
   guard_h = f.read(1).hex()
   guardPoint = hex2int(guard_h)
   control_h = f.read(1).hex()
   controlPoint = hex2int(control_h)
   speed_h = f.read(1).hex()
   speedPoint = hex2int(speed_h)
   guts_h = f.read(1).hex()
   gutsPoint = hex2int(guts_h)
   stamina_h = f.read(1).hex()
   staminaPoint = hex2int(stamina_h)
   
   PlayerInfo.append(GPpoint)
   PlayerInfo.append(TPpoint)
   PlayerInfo.append(kickPoint)
   PlayerInfo.append(bodyPoint)
   PlayerInfo.append(controlPoint)
   PlayerInfo.append(guardPoint)
   PlayerInfo.append(speedPoint)
   PlayerInfo.append(staminaPoint)
   PlayerInfo.append(gutsPoint)
   
   print(PlayerInfo)
   
with open('.dat','rb') as f:
   f.seek(PlayerOffset+4, os.SEEK_SET)
   Memberlist = []
   for i in range(TotalMember):
      chara_h = f.read(2).hex()
      charaID = byte2hex(chara_h)
      Memberlist.append(charaID)
      f.seek(0x6C-2, os.SEEK_CUR)
   print(Memberlist)
   
print(PlayerDict[PlayerInfo[1]][1])
GP = GPpoint+PlayerDict[PlayerInfo[1]][2]
TP = TPpoint+PlayerDict[PlayerInfo[1]][3]+EquipDict[PlayerInfo[5]][3]+EquipDict[PlayerInfo[6]][3]
Kick = kickPoint+PlayerDict[PlayerInfo[1]][4]+EquipDict[PlayerInfo[4]][4]
Body = bodyPoint+PlayerDict[PlayerInfo[1]][5]+EquipDict[PlayerInfo[5]][5]+EquipDict[PlayerInfo[6]][5]
Control = controlPoint+PlayerDict[PlayerInfo[1]][6]+EquipDict[PlayerInfo[5]][6]+EquipDict[PlayerInfo[6]][6]
Guard = guardPoint+PlayerDict[PlayerInfo[1]][7]
Speed = speedPoint+PlayerDict[PlayerInfo[1]][8]+EquipDict[PlayerInfo[4]][8]
Stamina = staminaPoint+PlayerDict[PlayerInfo[1]][9]+EquipDict[PlayerInfo[5]][9]+EquipDict[PlayerInfo[6]][9]
Guts = gutsPoint+PlayerDict[PlayerInfo[1]][10]+EquipDict[PlayerInfo[5]][10]+EquipDict[PlayerInfo[6]][10]
Move1 = MoveDict[PlayerInfo[7]][0]
Move2 = MoveDict[PlayerInfo[8]][0]
Move3 = MoveDict[PlayerInfo[9]][0]
Move4 = MoveDict[PlayerInfo[10]][0]
Move5 = MoveDict[PlayerInfo[11]][0]
Move6 = MoveDict[PlayerInfo[12]][0]
Move1Lv = movelv(MoveDict[PlayerInfo[7]][6], MoveDict[PlayerInfo[7]][7], m1TimesUsed)
Move2Lv = movelv(MoveDict[PlayerInfo[8]][6], MoveDict[PlayerInfo[8]][7], m2TimesUsed)
Move3Lv = movelv(MoveDict[PlayerInfo[9]][6], MoveDict[PlayerInfo[9]][7], m3TimesUsed)
Move4Lv = movelv(MoveDict[PlayerInfo[10]][6], MoveDict[PlayerInfo[10]][7], m4TimesUsed)
Move5Lv = movelv(MoveDict[PlayerInfo[11]][6], MoveDict[PlayerInfo[11]][7], m5TimesUsed)
Move6Lv = movelv(MoveDict[PlayerInfo[12]][6], MoveDict[PlayerInfo[12]][7], m6TimesUsed)
Equipment1 = EquipDict[PlayerInfo[4]][0]
Equipment2 = EquipDict[PlayerInfo[5]][0]
Equipment3 = EquipDict[PlayerInfo[6]][0]

print(GP, TP, Kick, Body, Control, Guard, Speed, Stamina, Guts)
print(Move1+Move1Lv, Move2+Move2Lv, Move3+Move3Lv, Move4+Move4Lv, Move5+Move5Lv, Move6+Move6Lv)
print(Equipment1, Equipment2, Equipment3)