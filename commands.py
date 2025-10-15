import os
import subprocess 
history=[]
aliases={}

def isBuiltin(s):
    if s.startswith("exit"):
        exit()
        return True
    elif s.startswith("history"):
        print(history)
        return True
    elif  s.startswith("alias"):
        alias_str = s[6:].strip()
        name, command = alias_str.split("=", 1)
        command = command.strip().strip("'\"")
        aliases[name.strip()]=command
        return True
    elif s.startswith("pwd"):
         print(os.getcwd())
         return True
    elif s.startswith("clear"):
         print(os.system("cls" if os.name=="nt" else "clear"))
         return True
    elif s.startswith("cd"):
         os.chdir(s[3:])
         return True

    return False   
   


windows_builtins = ["dir", "echo", "cls","mkdir"]
while True:
    s=input()
    history.append(s)
    cmd_parts = s.split()

    if cmd_parts[0] in aliases:
        s = aliases[cmd_parts[0]]
        cmd_parts = s.split()
    
    if isBuiltin(s):
        continue      
    elif "|" in s:
        cmds = [cmd.strip() for cmd in s.split('|')]
        p1=subprocess.Popen(cmds[0],stdout=subprocess.PIPE,shell=True)
        p2=subprocess.Popen(cmds[1],stdin=p1.stdout,stdout=subprocess.PIPE,shell=True)
        p1.stdout.close()
        output = p2.communicate()[0]
        print(output.decode())
        
    elif s.split()[0].lower() in windows_builtins:
        result=subprocess.run(s,shell=True)
        print(result)
    else:
        mylist = s.split(" ")
        result=subprocess.run(mylist,shell=True,capture_output=True, text=True)
        print(result)
        





        
       


    


