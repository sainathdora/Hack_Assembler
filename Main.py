import Symbol_Table as ST
import parser
fn = "dummy"
lines_lst = []
with open(f"{fn}.asm", 'r') as f:
    lines = f.readlines()
    # ignore the comments, empty spaces
    for i, line in enumerate(lines):
        line = line.rstrip()
        line = line.lstrip()
        if line[0:2]=="//":
            continue
        elif len(line)==0:
            continue
        lines_lst.append(line)
# now we have raw lines
# pass-1, add (XXX) into the symbol table
no_of_labels_encountered=0
for i, line in enumerate(lines_lst):
    if(line[0]=='(' and line[-1]==')'):
        no_of_labels_encountered +=1
        label_name = line[1:-1]
        # ('Loop', '2')
        ST.ST[label_name] = ((i+1)-no_of_labels_encountered)
# pass-2, for variables
n=16
lines_lst2 = []
for i, line in enumerate(lines_lst):
    # if @<value>
    if(line[0]=='@'):
        if(ST.ST.get(line[1:])):
            lines_lst2.append(f'@{ST.ST.get(line[1:])}')
            continue
        else:
            # check if @<number>
            if line[1:].isdigit():
                lines_lst2.append(line)
                continue
            else:
            # @<some variable>
                ST.ST[f'{line[1:]}']=n
                n+=1
                lines_lst2.append(f'@{ST.ST.get(line[1:])}')
                continue
    if(line[0]=='(' and line[-1]==')'):
        continue 
    lines_lst2.append(line)
print(ST.ST)
print("\n")
print(lines_lst, end="\n\n")
print(lines_lst2)
# Now worry about translation of instruction
binary_instructions=[]
for line in lines_lst2:
    binary_instructions.append(parser.parse(line))
with open('dummy.hack', 'w') as f:
    f.write("\n".join(binary_instructions))