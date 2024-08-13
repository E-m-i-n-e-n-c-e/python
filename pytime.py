import time as t
hour=int(t.strftime("%H"))

if(hour<7):
    print("Why are you up?\nGo to fucking sleep")
elif(hour<12):
     print("Good morning \nig you managed to get up before its afternoon if you're seeing this")
elif(hour<17):
     print("Good afternoon\nig you just woke up a while back so its more like good morning to you")
elif(hour<20):
     print("Good evening\n Your head is probably starting to hurt by now.Better go out and take a break ")
else:
     print("Goodnight\nYeah we both know you aren't going to sleep anytime soon")
