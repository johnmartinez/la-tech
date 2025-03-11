# How Command Injection works

- The goal is to inject or append arbitrary commands at the end of another command or URL
- A vulnerable web site will execute the command using its local operating system privileges
- Vulnerable web sites / apps will see this as a normal URL or command
- If an application is running as a privileged user, more damage can be done

![Command Injection Flowchart by MITRE](https://cwe.mitre.org/data/images/CWE-77-Diagram.png)

> [!WARNING]
> FIRST, DO NO HARM...TO YOURSELF AND OTHERS. Be careful that you only run this on lab equipment and be ethical about where/when you run this newfound power!

# How to run this code

1. Use a Linux or macOS system as an unprivileged user
2. Make sure you have `python3` installed
3. Clone [this repo](https://github.com/johnmartinez/la-tech.git) 
4. Open a terminal session
5. To run the web server, use the following command:
```
python3 ./vuln_server.py
```
6. Open a web browser, enter the url `http://localhost:8080/?cmd=` and insert linux commands (the browser will escape spaces and other characters)
7. You can use `pwnd.sh` in the repo as an example for remote code execution, or use the [gist link](https://gist.githubusercontent.com/johnmartinez/4db0733de870f0ee2ec98eda03a05148/raw/aa598f5ee9bb546d4f27baf1172bb0a1afd8d33b/pwnd.sh)
8. CTRL-C in the terminal window that you're running `vuln_server,py` to terminate the process

Above all...have fun!
