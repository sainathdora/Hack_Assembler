from parser import Parse, Preprocess, writetofile
from Symbol_Table import ST
fn = "WhiteSpace"
Preprocess(fn)
# The preprocess step will remove white spaces and comments
lines=[]
with open(f"{fn}.asm", "r") as f:
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
    
    # second pass: set n=16, if instruction is a symbol then look up ST
    # if ST[symbol] found then use it for translation
    n=16
    print(f"running Pass 2")
    for i, line in enumerate(lines):
        # print(f"line = {line}")
        if(line[0]=='@'):
            # @<value>
            if ST.get(line[1:]):
                # already known value
                print(f"known = {ST.get(line[1:])}")
                lines[i] = "@"+str(ST.get(line[1:]))
            else:
                # add this value to ST and replace it with known value
                ST[line[1:]]=n
                lines[i] = "@"+str(ST.get(line[1:]))
                n+=1
    for i in ST:
        print(f"{i} : {ST[i]}")
    print(lines)


writetofile(lines, fn, 'asm')
Preprocess(fn)
Parse(fn) 