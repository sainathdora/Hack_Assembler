from parser import Parse, Preprocess
from Symbol_Table import ST
Preprocess("WhiteSpace")
# The preprocess step will remove white spaces and comments
with open("WhiteSpace.asm", "r") as f:
    lines = [(line if line[-1]!='\n' else line[0:-1]) for line in f]
    print(lines)
    #1st Pass: Find (XXX) then add them to symbol table
    cnt=0
    # cnt tracks how many Label declarations we have found so far
    for i, line in enumerate(lines):
        if line[0]=="(" and line[-1]==")":
            cnt +=1
            name_of_symbol = line[1:-1]
            ST[name_of_symbol] = (i-cnt)+1
         
# Parse("WhiteSpace") 