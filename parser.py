from Code import deal_with_A_instruction, deal_with_C_Instruction
def parse(line):
    # now each line is a instruction
    binary_ins = None
    if(line[0]=='@'):
        binary_ins = deal_with_A_instruction(line)
    else:
        # preprocess c-instruction
        dest, comp, jmp = Preprocess_c_instruction(line)
        binary_ins = deal_with_C_Instruction(dest, comp, jmp)
    return binary_ins
        

def Preprocess_c_instruction(line):
    line = line.rstrip()
    line = line.lstrip()
    dest = comp = jump = ""
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
    # M=1 -> M=1;
    # D+1;JMP -> "=D+1;JMP"
    # "D;JMP" -> "=D;JMP"
    dest, p2 = line.split("=")
    comp, jump = p2.split(";")
    return [dest, comp, jump]
        