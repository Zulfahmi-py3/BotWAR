from linepy import *
from akad.ttypes import *
from multiprocessing import Pool, Process
from datetime import datetime
import time,random,sys,json,codecs,threading,glob,re,os,subprocess,asyncio
from datetime import datetime, timedelta
from time import sleep
from humanfriendly import format_timespan, format_size, format_number, format_length
import time, random, sys, json, codecs, threading, glob, re, string, os, requests, subprocess, six, ast, urllib, urllib.parse
_session = requests.session()
botStart = time.time()
settings = {
    "line": "TOKEN SB",
    "kb1": "TOKEN KICKER 1",
    "kb2": "TOKEN KICKER 2",
    "kb3": "TOKEN KICKER 3",
    "kunci": False,
    "kata": "prank",
    "blacklist": {}
}
line = LINE(settings["line"])
line.log("Auth Token : " + str(line.authToken))
channelToken = line.getChannelResult()
kb1 = LINE(settings["kb1"])
kb1.log("Auth Token : " + str(kb1.authToken))
kb2 = LINE(settings["kb2"])
kb2.log("Auth Token : " + str(kb2.authToken))
kb3 = LINE(settings["kb3"])
kb3.log("Auth Token : " + str(kb3.authToken))
oepoll = OEPoll(line)
lineProfile = line.getProfile()
lineSettings = line.getSettings()
myBOG = line.profile.mid
kb1BOG = kb1.getProfile().mid
kb2BOG = kb2.getProfile().mid
kb3BOG = kb3.getProfile().mid
mid = line.getProfile().mid
Bots = [myBOG,kb1BOG,kb2BOG,kb3BOG]
settings = {
    "kunci": False,
    "kata": "prank",
    "blacklist": {}
}
Drop_Xv = "u5818cb4404411c2e2e6e6937d172cca8" #ID_DROPING_BOTS
Xv_WIN = "udfaf52176415b46cb445ae2757ec85f3" #ID_WINDOWS_XP
Xv_LAN = "u17a086ccff618e754588a1108335867f" #ID_SERVER_LAN
Xv_Servic = "ub0842532a31b9d99856cf2590b17d33f" #ID_PROV_SERVICE
Xv_DxD = "uc8dc5352066b6a344bde3c07b0fe04ea" #ID_SYSTEM_BOTS
Line_Import = [Drop_Xv,Xv_WIN,Xv_LAN,Xv_Servic,Xv_DxD] #ALL_IMPORTING
def restartBot():
    print ("[ INFO ] BOT RESETTED")
    backupData()
    time.sleep(5)
    python = sys.executable
    os.execl(python, python, *sys.argv)
def logError(text):
    line.log("[ ERROR ] " + str(text))
    tz = pytz.timezone("Asia/Jakarta")
    timeNow = datetime.now(tz=tz)
    timeHours = datetime.strftime(timeNow,"(%H:%M)")
    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
    hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
    inihari = datetime.now(tz=tz)
    hr = inihari.strftime('%A')
    bln = inihari.strftime('%m')
    for i in range(len(day)):
        if hr == day[i]: hasil = hari[i]
    for k in range(0, len(bulan)):
        if bln == str(k): bln = bulan[k-1]
    time = hasil + ", " + inihari.strftime('%d') + " - " + bln + " - " + inihari.strftime('%Y') + " | " + inihari.strftime('%H:%M:%S')
    with open("PrankBots.txt","a") as error:
        error.write("\n[%s] %s" % (str(time), text))
def command(text):
    pesan = text.lower()
    if settings["kunci"] == True:
        if pesan.startswith(settings["kata"]):
            prankbot = pesan.replace(settings["kata"],"")
        else:
            prankbot = "Undefined command"
    else:
        prankbot = text.lower()
    return prankbot
def bot(op):
    global time
    global ast
    global groupParam
    try:
        if op.type == 0:
            return
        if op.type == 25:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            setKey = settings["kata"].title()
            if settings["kunci"] == False:
                 setKey = ''
            if msg.toType == 0 or msg.toType == 1 or msg.toType == 2:
                if msg.toType == 0:
                    if sender != line.profile.mid:
                        to = sender
                    else:
                        to = receiver
                elif msg.toType == 1:
                    to = receiver
                elif msg.toType == 2:
                    to = receiver
                if msg.contentType == 0:
                    if text is None:
                        return
                    else:
                        prankbot = command(text)
                        if prankbot == "abouts":
                            line.sendMessage(to,"|abouts Bot|\n|R _for respon\n|kikil _for kickall\n|kick @mention _for kick target\n|in _for bot join group\n|out _ for bot leave group\n|bye _for self leave group\n|banlist _for check blacklist user\n|clearban _for delete all blacklist\n|mybot _for send contact bot\n|backup _for backup bot")
                        if prankbot == "backup":
                            try:
                                line.findAndAddContactsByMid(kb1BOG)
                                line.findAndAddContactsByMid(kb2BOG)
                                line.findAndAddContactsByMid(kb3BOG)
                                line.findAndAddContactsByMid(Drop_Xv)
                                line.findAndAddContactsByMid(Xv_WIN)
                                line.findAndAddContactsByMid(Xv_LAN)
                                line.findAndAddContactsByMid(Xv_Servic)
                                line.findAndAddContactsByMid(Xv_DxD)
                                kb1.findAndAddContactsByMid(myBOG)
                                kb1.findAndAddContactsByMid(kb2BOG)
                                kb1.findAndAddContactsByMid(kb3BOG)
                                kb1.findAndAddContactsByMid(Drop_Xv)
                                kb1.findAndAddContactsByMid(Xv_WIN)
                                kb1.findAndAddContactsByMid(Xv_LAN)
                                kb1.findAndAddContactsByMid(Xv_Servic)
                                kb1.findAndAddContactsByMid(Xv_DxD)
                                kb2.findAndAddContactsByMid(myBOG)
                                kb2.findAndAddContactsByMid(kb1BOG)
                                kb2.findAndAddContactsByMid(Drop_Xv)
                                kb2.findAndAddContactsByMid(Xv_WIN)
                                kb2.findAndAddContactsByMid(Xv_LAN)
                                kb2.findAndAddContactsByMid(Xv_Servic)
                                kb2.findAndAddContactsByMid(Xv_DxD)
                                kb3.findAndAddContactsByMid(myBOG)
                                kb3.findAndAddContactsByMid(kb1BOG)
                                kb3.findAndAddContactsByMid(kb2BOG)
                                kb3.findAndAddContactsByMid(Drop_Xv)
                                kb3.findAndAddContactsByMid(Xv_WIN)
                                kb3.findAndAddContactsByMid(Xv_LAN)
                                kb3.findAndAddContactsByMid(Xv_Servic)
                                kb3.findAndAddContactsByMid(Xv_DxD)
                                line.sendMessage(to,"succes.!!.\nready..")
                            except:
                                line.sendMessage(to,"ready..")
                        if prankbot == "in":
                            anggota = [kb1BOG,kb2BOG,kb3BOG]
                            line.inviteIntoGroup(msg.to, anggota)
                            kb1.acceptGroupInvitation(msg.to)
                            kb2.acceptGroupInvitation(msg.to)
                            kb3.acceptGroupInvitation(msg.to)
                        elif prankbot.startswith("kick "):
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                lists = []
                                for mention in mentionees:
                                    if mention["M"] not in lists:
                                        lists.append(mention["M"])
                                for ls in lists:
                                    try:
                                        kb1.kickoutFromGroup(to,[ls])
                                        print (to,[ls])
                                    except:
                                        kb2.kickoutFromGroup(to,[ls])
                                        print (to,[ls])
                        elif prankbot == "banlist":
                                if settings["blacklist"] == {}:
                                    line.sendMessage(to,"Tidak Ada kontak blacklist")
                                else:
                                    line.sendMessage(to,"═══════List blacklist═══════")
                                    h = ""
                                    for i in settings["blacklist"]:
                                        h = line.getContact(i)
                                        line.sendContact(to,i)
                        elif prankbot == "clearban":
                            settings["blacklist"] = {}
                            line.sendMessage(to,"success.!!")
                        elif prankbot == "mybots" or prankbot == "mybot":
                            line.sendContact(to, myBOG)
                            line.sendContact(to, kb1BOG)
                            line.sendContact(to, kb2BOG)
                            line.sendContact(to, kb3BOG)
                        elif prankbot == "r":
                            profile = kb1.getProfile()
                            text = profile.displayName + "􀜁􀅔􏿿"
                            kb1.sendMessage(to, text)
                            profile = kb2.getProfile()
                            text = profile.displayName + "􀜁􀅔􏿿"
                            kb2.sendMessage(to, text)
                            profile = kb3.getProfile()
                            text = profile.displayName + "􀜁􀅔􏿿"
                            kb3.sendMessage(to, text)
                        elif prankbot == "bye":
                            kb1.leaveGroup(msg.to)
                            kb2.leaveGroup(msg.to)
                            kb3.leaveGroup(msg.to)
                            line.sendMessage(to,"====owner creator=====")
                            line.sendContact(to, 'u0ac948397fbc732bd3bc5ca273faa698')
                            line.leaveGroup(msg.to)
                        elif prankbot == "out":
                            kb1.leaveGroup(msg.to)
                            kb2.leaveGroup(msg.to)
                            kb3.leaveGroup(msg.to)
                        elif prankbot == "kikil":
                            if msg.toType == 2:
                                gs = line.getGroup(msg.to)
                                gs = kb1.getGroup(msg.to)
                                gs = kb2.getGroup(msg.to)
                                gs = kb3.getGroup(msg.to)
                                time.sleep(0.0002)
                                targets = []
                                for g in gs.members:
                                    if _name in g.displayName:
                                        targets.append(g.mid)
                                if targets == []:
                                    line.sendMessage(to,"LIMIT.!!!")
                                else:
                                     for target in targets:
                                         if not target in Bots:
                                             try:
                                                 klist=[kb1,kb2,kb3line]
                                                 kicker=random.choice(klist)
                                                 kicker.kickoutFromGroup(to,[target])
                                                 print (to,[g.mid])
                                             except:
                                                 pass
        if op.type == 19 or op.type == 32:
            if myBOG in op.param3:
                if op.param2 in Bots:
                    kb1.inviteIntoGroup(op.param1,[op.param3])
                    line.acceptGroupInvitation(op.param1)
                else:
                    settings["blacklist"][op.param2] = True
                    try:
                        kb1.inviteIntoGroup(op.param1,[op.param3])
                        kb2.kickoutFromGroup(op.param1,[op.param2])
                        kb3.kickoutFromGroup(op.param1,[op.param2])
                        line.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            kb1.kickoutFromGroup(op.param1,[op.param2])
                            kb2.inviteIntoGroup(op.param1,[op.param3])
                            kb3.inviteIntoGroup(op.param1,[op.param3])
                            line.acceptGroupInvitation(op.param1)
                        except:
                            pass
            if kb1BOG in op.param3: #BAGIAN BACKUP LEWAT QR
                if op.param2 in Bots:
                    kb1.inviteIntoGroup(op.param1,[op.param3])
                    line.acceptGroupInvitation(op.param1)
                else:
                    settings["blacklist"][op.param2] = True
                    try:
                        G = line.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        line.updateGroup(G)
                        Ticket = line.reissueGroupTicket(op.param1)
                        kb1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kb2.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        G = kb2.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        kb2.updateGroup(G)
                        Ticket = kb2.reissueGroupTicket(op.param1)
                        kb1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kb1.kickoutFromGroup(op.param1,[op.param2])
            if kb2BOG in op.param3:
                if op.param2 in Bots:
                    kb1.inviteIntoGroup(op.param1,[op.param3])
                    line.acceptGroupInvitation(op.param1)
                else:
                    settings["blacklist"][op.param2] = True
                    try:
                        line.inviteIntoGroup(op.param1,[op.param3])
                        kb1.kickoutFromGroup(op.param1,[op.param2])
                        kb2.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            line.kickoutFromGroup(op.param1,[op.param2])
                            kb1.inviteIntoGroup(op.param1,[op.param3])
                            kb2.acceptGroupInvitation(op.param1)
                        except:
                            pass
            if kb3BOG in op.param3:
                if op.param2 in Bots:
                    kb2.inviteIntoGroup(op.param1,[op.param3])
                    line.acceptGroupInvitation(op.param1)
                else:
                    settings["blacklist"][op.param2] = True
                    try:
                        line.inviteIntoGroup(op.param1,[op.param3])
                        kb2.kickoutFromGroup(op.param1,[op.param2])
                        kb3.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            line.kickoutFromGroup(op.param1,[op.param2])
                            kb2.inviteIntoGroup(op.param1,[op.param3])
                            kb3.acceptGroupInvitation(op.param1)
                        except:
                            pass
        if op.type == 17:
            if op.param2 in settings["blacklist"]:
                try:
                    kb1.kickoutFromGroup(op.param1,[op.param2])
                except:
                    try:
                        kb2.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            kb3.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            line.kickoutFromGroup(op.param1,[op.param2])
        except Exception as error:
            logError(error)
        if op.type == 59:
            print (op)
while True:
    try:
      ops=oepoll.singleTrace(count=50)
      if ops != None:
        for op in ops: 
          bot(op)
          oepoll.setRevision(op.revision)
    except Exception as e:
        line.log("[SINGLE_TRACE] ERROR : " + str(e))
