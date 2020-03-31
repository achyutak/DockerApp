import glob
import os
import socket
import sys
import re
og_stdout = sys.stdout
path = 'home/data/'
res_path = 'home/output/result.txt'
length_of_words = []
myfiles = glob.glob(path + '*.txt')
for f in myfiles:
    myfiles[myfiles.index(f)] = re.sub(path,'',f)
out = open(res_path,"w+")
sys.stdout = out
print("This is a New File made by Aravinda Karthik\n\n")
print("The input files are in:",path,"directory\n")
print("The output files are in:",res_path,"directory\n")
print("There are",len(myfiles),"files in the " + path + " directory, they are:")
for f in myfiles: print(f)

for f in myfiles:
    file = open(path + f)
    n = len(file.read().split())
    print("In file " + f + ": There are",n,"words.")
    length_of_words.append(n)

print("\nThe grand total is :",sum(length_of_words))
print("\nThe file containing maximum number of words is:",myfiles[length_of_words.index(max(length_of_words))])
import socket
def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # doesn't even have to be reachable
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
    except:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP
print("\nThe IP address of the machine is:",get_ip())
sys.stdout = og_stdout
out.close()
view = open(res_path,"r")
print(view.read())
