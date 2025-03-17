# Calender Week 11 - 11 March 2025
# Slothbytes Newsletter Challenge - Hidden Calculater Words
# submit by Shadowdara
# written in Python
# 
# check out my Github Profile please
# https://github.com/shadowdara
#
# I am sure this would be possible a lot less complicated,
# but i like it to complicate simple things
#
# Yeah, you need to install Python to run this script!
#
# And to be honest, i am really sure what the challenge was,
# maybe it is although finding other words you can write with
# just numbers, that has nothing to do with coding,
# so I ended up with this idea.
#
# and i am not sure if 9 is not possible are used as "space",
# but 9 will work in this script and covert it to a "-"
#
# Python is btw my favourite prgramming language
#
# MIT LICENSE Shadowdara 2025
#
# to be honest i am not sure when i started, but i am defenetly
# sitting here a lot longer. (Now its 5:21 pm)
# i suck at coding lol
# i want to learn Java for Minecraft Mods
# but python is way easier so always end up with python
#
# D:
#
# I know my Version is a lot overkill and i wasted defenetly to
# much time for things nobody would ever care about, but at least
# i had a bit of fun thinking about thess problems!
# when you are not completly helpless, is programming mostly fun
#
# Sorry for all this comment spam, but i need this to not getting
# crazy lol!
#
# The next time i will do this in Java or Scala because i think
# this would be much harder!
#
# I am FINISHED and its now 6.05 pm
# this took so much time 
# D:
#
# I hope nobody reads this all lol

letters = "OIZEHSGLB-"

def updside_down():
    global msg_2
    msg_2 = list(msg.upper())
    for i in range(0, (length)):
        tmp = list(msg)
        for x in range(0, 10):
            if tmp[i] == letters[x]:
                msg_2[i] = x
                break
    msg_2 = "".join(map(str, msg_2))[::-1]
        

def right_side():
    global msg_2
    msg_2 = list(msg)
    for i in range(0, (length)):
        char = msg[i]
        if char.isdigit():
            tmp = int(msg[i])
            msg_2[i] = letters[tmp]
        else:
            break
    msg_2 = "".join(msg_2)[::-1]

def end():
    print()
    print(f"Your Message was:           {msg}")
    print(f"The converted Message is    {msg_2}")
    print()
    start()

def start():
    global msg, length
    msg = input("Your Message: ===>")
    length = len(msg)
    length -= 2
    if msg.startswith("1 "):
        msg = msg[2:]
        updside_down()
        end()
    elif msg.startswith("2 "):
        msg = msg[2:]
        right_side()
        end()
    elif msg.startswith("0") or msg.startswith("exit 0"):
        pass
    else:
        input("Invalid Input! Please try again!")
        start()

if __name__ == "__main__":
    print("""Upside Down Converter in Python

Only this Letters are working!

I, Z, E, H, S, G, L, B, -, 0
1, 2, 3, 4, 5, 6, 7, 8, 9, 0

Type in your Message!

start with "0 " - to exit
start with "1 " - to convert numbers to letters
start with "2 " - to convert letters to numbers

e.g:                     1 Hello
and the output would be: 07734
""")
    start()
