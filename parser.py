import re

def Preprocess(filename): #filename.asm
    with open(f'{filename}.asm') as f:
        lines = [line.rstrip() for line in f]
        lines = [line.lstrip() for line in lines]
        lines = list(filter(lambda x:x!='', lines))
        # this list contains no white space, all we have to do now is worry about comments
        # <content-1> // <content-2>
        # select only content-1
        l2=[]
        for indx, ele in enumerate(lines):
            if(ele=="\n"):
                continue
            if(len(ele.split("//"))==1):
                l2.append(ele)
                continue
            left, right = ele.split("//")
            if(left!=""):
                left = left.rstrip()
                l2.append(left)
        lines=l2
        writetofile(lines, filename, 'asm')
    
    
def writetofile(lines, output, extension):
    # lines is list of line, output is where to write this parsed output generally .asm
    with open(f"{output}.{extension}", "w") as f:
        for indx, line in enumerate(lines):
            line = line.rstrip()
            line = line.lstrip()
            if(indx==len(lines)-1):
                f.write(line)
            else:
                f.write(line + "\n")

def Deal_A_Instruction(line):
    #assume A-Instruction
    res = "0"
    num = line[1:]
    # num = (<integer>) base-10
    num = format(int(num), '015b')
    res = res+num
    return res
    # num is now in binary

def Parse(filename):
    Preprocess(filename)
    lines=[]
    with open(f'{filename}.asm', 'r') as f:
        lines = [line for line in f]
        for ind, line in enumerate(lines):
            if(line[0]=='@'):
                BinaryOp = Deal_A_Instruction(line)
                lines[ind]=BinaryOp
            else:
                BinaryOp = Deal_with_C_instruction(line)
                lines[ind]=BinaryOp
    writetofile(lines, f'{filename}', 'hack')


def Preprocess_c_instruction(line):
    line = line.rstrip()
    line = line.lstrip()
    p2=line
    try:
        dest, p2 = line.split("=")
    except ValueError as e:
        line = "="+line
        dest, p2 = line.split("=")
    try:
        comp, jump = p2.split(";")
    except ValueError as e:
        line = line+";"
    
    return line
        

def Deal_with_C_instruction(line):
    line = Preprocess_c_instruction(line)
    dest, p2 = line.split("=")
    comp, jump = p2.split(";")
    
    # jump is string of length 0, if p2 = "D+1;"(eg)
    # identify the destination eg: dest -> (binary)
    dest_bits = find_destination_bits(dest)
    # identify the comp bits
    # "=<comp>;"
    comp_bits, a = find_Comp_bits(comp)
    jump_bits = find_jump_bits(jump)
    return f"111{a}{comp_bits}{dest_bits}{jump_bits}"


def find_destination_bits(dest):
    d = {
        "":"000",
        "M":"001",
        "D":"010",
        "MD":"011",
        "A":"100",
        "AM":"101",
        "AD":"110",
        "AMD":"111"
    }
    return d[dest]

def find_Comp_bits(comp):
    d = {
        "0":["101010", 0],
        "1":["111111", 0],
        "-1":["111010", 0],
        "D":["001100", 0],

        "A":["110000", 0],
        "M":["110000", 1],
        
        "!D":["001101", 0],
        
        "!A":["110001", 0],
        "!M":["110001", 1],
        
        "-D":["001111", 0],
        
        "-A":["110011", 0],
        "-M":["110011", 1],

        "D+1":["011111", 0],
        
        "A+1":["110111", 0],
        "M+1":["110111", 1],

        "D-1":["001110", 0],

        "A-1":["110010", 0],
        "M-1":["110010", 1],

        "D+A":["000010", 0],
        "D+M":["000010", 1],

        "D-A":["010011", 0],
        "D-M":["010011", 1],
        
        "A-D":['000111', 0],
        "M-D":['000111', 1],

        "D&A":["000000", 0],
        "D&M":["000000", 1],

        "D|A":["010101", 0],
        "D|M":["010101", 1],
    }
    return d[comp]

def find_jump_bits(jump):
    d = {
        "":"000",
        "JGT":"001",
        "JEQ":"010",
        "JGE":"011",
        "JLT":"100",
        "JNE":"101",
        "JLE":"110",
        "JMP":"111"
    }
    return d[jump]