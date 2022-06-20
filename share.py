
with open('G:\Among Us\Among Us - TOR 4.1.4 - Phil Hartman\BepInEx\config\me.eisbison.theotherroles.cfg') as f:
    contents = f.read()
#print(contents)

#Use this to Export to TXT:
import sys
sys.stdout = open('G:\Among Us\py-roles.txt', 'wt')

def find_nth(haystack, needle, n):
    start = haystack.find(needle)
    while start >= 0 and n > 1:
        start = haystack.find(needle, start+len(needle))
        n -= 1
    return start

#Janitor
name=""
chance=""
ROLE_10 = (find_nth(contents,"10 = ", 1))
if contents[ROLE_10+5] != "0":
    name = "Janitor"
if contents[ROLE_10+6] not in ["1","0"]:
    chance = "?"
if name != "":
    print(name,chance,sep="")


#Morphling
name=""
chance=""
ROLE_20 = (find_nth(contents,"20 = ", 1))
if contents[ROLE_20+5] != "0":
    name = "Morphling"
if contents[ROLE_20+6] not in ["1","0"]:
    chance = "?"
if name != "":
    print(name,chance,sep="")

#Camoflager
name=""
chance=""
ROLE_30 = (find_nth(contents,"30 = ", 1))
if contents[ROLE_30+5] != "0":
    name = "Camoflager"
if contents[ROLE_30+6] not in ["1","0"]:
    chance = "?"
if name != "":
    print(name,chance,sep="")

#Vampire
name=""
chance=""
ROLE_40 = (find_nth(contents,"40 = ", 1))
if contents[ROLE_40+5] != "0":
    name = "Vampire"
if contents[ROLE_40+6] not in ["1","0"]:
    chance = "?"
if name != "":
    print(name,chance,sep="")

#Eraser
name=""
chance=""
ROLE_230 = (find_nth(contents,"230 = ", 1))
if contents[ROLE_230+6] != "0":
    name = "Eraser"
if contents[ROLE_230 + 7] not in ["1","0"]:
    chance = "?"
if name != "":
    print(name,chance,sep="")

#Trickster
name=""
chance=""
ROLE_250 = (find_nth(contents,"250 = ", 1))
if contents[ROLE_250+6] != "0":
    name = "Trickster"
if contents[ROLE_250 + 7] not in ["1","0"]:
    chance = "?"
if name != "":
    print(name,chance,sep="")

#Cleaner
name=""
chance=""
ROLE_260 = (find_nth(contents,"260 = ", 1))
if contents[ROLE_260+6] != "0":
    name = "Cleaner"
if contents[ROLE_260 + 7] not in ["1","0"]:
    chance = "?"
if name != "":
    print(name,chance,sep="")

#Warlock
name=""
chance=""
ROLE_270 = (find_nth(contents,"270 = ", 1))
if contents[ROLE_270+6] != "0":
    name = "Warlock"
if contents[ROLE_270 + 7] not in ["1","0"]:
    chance = "?"
if name != "":
    print(name,chance,sep="")

#BountyHunter
name=""
chance=""
ROLE_320 = (find_nth(contents,"320 = ", 1))
if contents[ROLE_320+6] != "0":
    name = "BountyH"
if contents[ROLE_320 + 7] not in ["1","0"]:
    chance = "?"
if name != "":
    print(name,chance,sep="")

#Witch
name=""
chance=""
ROLE_370 = (find_nth(contents,"370 = ", 1))
if contents[ROLE_370+6] != "0":
    name = "Witch"
if contents[ROLE_370 + 7] not in ["1","0"]:
    chance = "?"
if name != "":
    print(name,chance,sep="")

#Ninja
name=""
chance=""
ROLE_380 = (find_nth(contents,"380 = ", 1))
if contents[ROLE_380+6] != "0":
    name = "Ninja"
if contents[ROLE_380 + 7] not in ["1","0"]:
    chance = "?"
if name != "":
    print(name,chance,sep="")

#Guesser - Bad
name=""
chance=""
ROLE_311 = (find_nth(contents,"311 = ", 1))
if contents[ROLE_311+6] != "0":
    name = "Guesser(B)"
if contents[ROLE_311 + 7] not in ["1","0"]:
    chance = "?"
if name != "":
    print(name,chance,sep="")

#-------------------------------Neutral Roles----------------------------------

#Jester
name=""
chance=""
ROLE_60 = (find_nth(contents,"60 = ", 2))
if contents[ROLE_60+5] != "0":
   name = "Jester"
if contents[ROLE_60+6] not in ["1","0"]:
    chance = "?"
if name != "":
    print(name,chance,sep="")

#Arsonist
name=""
chance=""
ROLE_290 = (find_nth(contents,"290 = ", 1))
if contents[ROLE_290+6] != "0":
    name = "Arsonist"
if contents[ROLE_290+7] not in ["1","0"]:
    chance = "?"
if name != "":
    print(name,chance,sep="")

#Jackal
name=""
chance=""
ROLE_220 = (find_nth(contents,"220 = ", 1))
if contents[ROLE_220+6] != "0":
    name = "Jackal"
if contents[ROLE_220+7] not in ["1","0"]:
    chance = "?"
if name != "":
    print(name,chance,sep="")

#Jackal Sidekick
name=""
chance=""
ROLE_224 = (find_nth(contents,"224 = ", 1))
if contents[ROLE_224+6] != "0":
    name = "-Sidekick"
#if contents[ROLE_224+7] not in ["1","0"]:
#    chance = "?"
if name != "":
    print(name,chance,sep="")

#Vulture
name=""
chance=""
ROLE_340 = (find_nth(contents,"340 = ", 1))
if contents[ROLE_340+6] != "0":
    name = "Vulture"
if contents[ROLE_340+7] not in ["1","0"]:
    chance = "?"
if name != "":
    print(name,chance,sep="")

#Lawyer
name=""
chance=""
ROLE_350 = (find_nth(contents,"350 = ", 1))
if contents[ROLE_350+6] != "0":
    name = "Lawyer"
if contents[ROLE_350+7] not in ["1","0"]:
    chance = "?"
if name != "":
    print(name,chance,sep="")


#-------------------------------Crewmate Roles----------------------------------



#Guesser - Good
name=""
chance=""
ROLE_317 = (find_nth(contents,"317 = ", 1))
if contents[ROLE_317+6] != "0":
    name = "Guesser(G)"
if contents[ROLE_317 + 7] not in ["1","0"]:
    chance = "?"
if name != "":
    print(name,chance,sep="")

#Shifter
name=""
chance=""
ROLE_70 = (find_nth(contents,"70 = ", 3))
if contents[ROLE_70+5] != "0":
    name = "Shifter"
if contents[ROLE_70 + 6] not in ["1","0"]:
    chance = "?"
if name != "":
    print(name,chance,sep="")

#Mayor
name=""
chance=""
ROLE_80 = (find_nth(contents,"80 = ", 2))
if contents[ROLE_80+5] != "0":
    name = "Mayor"
if contents[ROLE_80 + 6] not in ["1","0"]:
    chance = "?"
if name != "":
    print(name,chance,sep="")

#Engineer
name=""
chance=""
ROLE_90 = (find_nth(contents,"90 = ", 2))
if contents[ROLE_90+5] != "0":
    name = "Engineer"
if contents[ROLE_90 + 6] not in ["1","0"]:
    chance = "?"
if name != "":
    print(name,chance,sep="")

#Sheriff
name=""
chance=""
ROLE_100 = (find_nth(contents,"100 = ", 1))
if contents[ROLE_100+6] != "0":
    name = "Sheriff"
if contents[ROLE_100 + 7] not in ["1","0"]:
    chance = "?"
if name != "":
    print(name,chance,sep="")

#Sheriff's Deputy
name=""
chance=""
ROLE_103 = (find_nth(contents,"103 = ", 1))
if contents[ROLE_103+6] != "0":
    name = "-Deputy"
if contents[ROLE_103 + 7] not in ["1","0"]:
    chance = "?"
if name != "":
    print(name,chance,sep="")

#Lighter
name=""
chance=""
ROLE_110 = (find_nth(contents,"110 = ", 1))
if contents[ROLE_110+6] != "0":
    name = "Lighter"
if contents[ROLE_110 + 7] not in ["1","0"]:
    chance = "?"
if name != "":
    print(name,chance,sep="")

#Detective
name=""
chance=""
ROLE_120 = (find_nth(contents,"120 = ", 1))
if contents[ROLE_120+6] != "0":
    name = "Detective"
if contents[ROLE_120 + 7] not in ["1","0"]:
    chance = "?"
if name != "":
    print(name,chance,sep="")

#TimeMaster
name=""
chance=""
ROLE_130 = (find_nth(contents,"130 = ", 1))
if contents[ROLE_130+6] != "0":
    name = "TimeMast"
if contents[ROLE_130 + 7] not in ["1","0"]:
    chance = "?"
if name != "":
    print(name,chance,sep="")

#Medic
name=""
chance=""
ROLE_140 = (find_nth(contents,"140 = ", 1))
if contents[ROLE_140+6] != "0":
    name = "Medic"
if contents[ROLE_140 + 7] not in ["1","0"]:
    chance = "?"
if name != "":
    print(name,chance,sep="")

#Swapper
name=""
chance=""
ROLE_150 = (find_nth(contents,"150 = ", 1))
if contents[ROLE_150+6] != "0":
    name = "Swapper"
if contents[ROLE_150 + 7] not in ["1","0"]:
    chance = "?"
if name != "":
    print(name,chance,sep="")

#Seer
name=""
chance=""
ROLE_160 = (find_nth(contents,"160 = ", 1))
if contents[ROLE_160+6] != "0":
    name = "Seer"
if contents[ROLE_160 + 7] not in ["1","0"]:
    chance = "?"
if name != "":
    print(name,chance,sep="")

#Hacker
name=""
chance=""
ROLE_170 = (find_nth(contents,"170 = ", 1))
if contents[ROLE_170+6] != "0":
    name = "Hacker"
if contents[ROLE_170 + 7] not in ["1","0"]:
    chance = "?"
if name != "":
    print(name,chance,sep="")

#Tracker
name=""
chance=""
ROLE_200 = (find_nth(contents,"200 = ", 1))
if contents[ROLE_200+6] != "0":
    name = "Tracker"
if contents[ROLE_200 + 7] not in ["1","0"]:
    chance = "?"
if name != "":
    print(name,chance,sep="")

#Snitch
name=""
chance=""
ROLE_210 = (find_nth(contents,"210 = ", 1))
if contents[ROLE_210+6] != "0":
    name = "Tracker"
if contents[ROLE_210 + 7] not in ["1","0"]:
    chance = "?"
if name != "":
    print(name,chance,sep="")

#Spy
name=""
chance=""
ROLE_240 = (find_nth(contents,"240 = ", 1))
if contents[ROLE_240+6] != "0":
    name = "Spy"
if contents[ROLE_240 + 7] not in ["1","0"]:
    chance = "?"
if name != "":
    print(name,chance,sep="")

#PortalMaker
name=""
chance=""
ROLE_390 = (find_nth(contents,"390 = ", 1))
if contents[ROLE_390+6] != "0":
    name = "PortalMkr"
if contents[ROLE_390 + 7] not in ["1","0"]:
    chance = "?"
if name != "":
    print(name,chance,sep="")

#Security Guard
name=""
chance=""
ROLE_280 = (find_nth(contents,"280 = ", 1))
if contents[ROLE_280+6] != "0":
    name = "SecGuard"
if contents[ROLE_280 + 7] not in ["1","0"]:
    chance = "?"
if name != "":
    print(name,chance,sep="")

#Medium
name=""
chance=""
ROLE_360 = (find_nth(contents,"360 = ", 1))
if contents[ROLE_360+6] != "0":
    name = "Medium"
if contents[ROLE_360 + 7] not in ["1","0"]:
    chance = "?"
if name != "":
    print(name,chance,sep="")



#-------------------------------Modifiers ----------------------------------
#Bloody
name=""
chance=""
ROLE_1000 = (find_nth(contents,"1000 = ", 1))
if contents[ROLE_1000+7] != "0":
    name = "(Bloody)"
if contents[ROLE_1000 + 8] not in ["1","0"]:
    chance = "?"
if name != "":
    print(name,chance,sep="")

# AntiTeleporter
name = ""
chance = ""
ROLE_1010 = (find_nth(contents, "1010 = ", 1))
if contents[ROLE_1010 + 7] != "0":
    name = "(AntiTele)"
if contents[ROLE_1010 + 8] not in ["1", "0"]:
    chance = "?"
if name != "":
    print(name,chance,sep="")

# Tie Breaker
name = ""
chance = ""
ROLE_1020 = (find_nth(contents, "1020 = ", 1))
if contents[ROLE_1020 + 7] != "0":
    name = "(TieB)"
if contents[ROLE_1020 + 8] not in ["1", "0"]:
    chance = "?"
if name != "":
    print(name,chance,sep="")

# Bait
name = ""
chance = ""
ROLE_1030 = (find_nth(contents, "1030 = ", 1))
if contents[ROLE_1030 + 7] != "0":
    name = "(Bait)"
if contents[ROLE_1030 + 8] not in ["1", "0"]:
    chance = "?"
if name != "":
    print(name,chance,sep="")

# Lovers
name = ""
chance = ""
ROLE_1040 = (find_nth(contents, "1040 = ", 1))
if contents[ROLE_1040 + 7] != "0":
    name = "(Lovers)"
if contents[ROLE_1040 + 8] not in ["1", "0"]:
    chance = "?"
if name != "":
    print(name,chance,sep="")

# Sunglasses
name = ""
chance = ""
ROLE_1050 = (find_nth(contents, "1050 = ", 1))
if contents[ROLE_1050 + 7] != "0":
    name = "(⌐■_■)"
if contents[ROLE_1050 + 8] not in ["1", "0"]:
    chance = "?"
if name != "":
    print(name,chance,sep="")

# Mini
name = ""
chance = ""
ROLE_1061 = (find_nth(contents, "1061 = ", 1))
if contents[ROLE_1061 + 7] != "0":
    name = "(Mini)"
if contents[ROLE_1061 + 8] not in ["1", "0"]:
    chance = "?"
if name != "":
    print(name,chance,sep="")

# VIP
name = ""
chance = ""
ROLE_1070 = (find_nth(contents, "1070 = ", 1))
if contents[ROLE_1070 + 7] != "0":
    name = "(VIP)"
if contents[ROLE_1070 + 8] not in ["1", "0"]:
    chance = "?"
if name != "":
    print(name,chance,sep="")

# Invert
name = ""
chance = ""
ROLE_1080 = (find_nth(contents, "1080 = ", 1))
if contents[ROLE_1080 + 7] != "0":
    name = "(Invert)"
if contents[ROLE_1080 + 8] not in ["1", "0"]:
    chance = "?"
if name != "":
    print(name,chance,sep="")


