# How Command Injection works

- The goal is to inject or append arbitrary commands at the end of another command or URL
- A vulnerable web site will execute the command using its local operating system privileges
- Vulnerable web sites / apps will see this as a normal URL or command
- If an application is running as a privileged user, more damage can be done

![Command Injection Flowchart by MITRE](https://cwe.mitre.org/data/images/CWE-77-Diagram.png)
