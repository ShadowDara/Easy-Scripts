# Week 12

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
