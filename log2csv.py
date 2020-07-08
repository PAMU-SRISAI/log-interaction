

#!/usr/bin/env python3
import re
import operator

error={}
user={}
user1={}
f=open("syslog.log","r")
for line in f:
  n=re.search(r"ticky: ERROR ([\w ]*) ", line)
  if n is None:
    new=re.search(r" \(([\w]*)\)", line)
    if new is not None:
        if new.groups()[0] in user.keys():
            user[new.groups()[0]]= user[new.groups()[0]]+1
        else:
            user[new.groups()[0]]=1
  else:
    if n.groups()[0] in error.keys():
        error[n.groups()[0]]= error[n.groups()[0]]+1
    else:
        error[n.groups()[0]]=1
    new=re.search(r" \(([\w]*)\)", line)
    if new is not None:
        if new.groups()[0] in user1.keys():
            user1[new.groups()[0]]= user1[new.groups()[0]]+1
        else:
            user1[new.groups()[0]]=1
error=sorted(error.items(), key = operator.itemgetter(1), reverse=True)
user=sorted(user.items())

#print(user)
#print(user1)
f.close()
f=open("error_message.csv", "w")
f.write("Error,Count\n")
for x in error:
    f.write(x[0]+","+str(x[1])+"\n")
f.close()
f=open("user_statistics.csv", "w")
f.write("Username,INFO,ERROR\n")
for x in user:
    if x[0] in user1.keys():
        f.write(x[0]+","+str(x[1])+","+str(user1[x[0]])+"\n")
    else:
        f.write(x[0]+","+str(x[1]) + ",0" + "\n")
f.close()
