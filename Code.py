import Symbol_Table
def deal_with_A_instruction(line):
    # @value
    # here value is value is integer
    res = "0"
    num = line[1:]
    # num = (<integer>) base-10
    num = format(int(num), '015b')
    res = res+num
    return res

def deal_with_C_Instruction(dest, comp, jump):
    # clean c instruction dest=comp;jmp
    binary_ins = "111"
    # adding comp bits
    binary_ins +=Symbol_Table.find_Comp_bits_7(comp)
    # adding dest bits
    dest_bits = Symbol_Table.find_destination_bits(dest)
    binary_ins += dest_bits
    # adding jumpy bits
    jump_bits = Symbol_Table.find_jump_bits(jump)
    binary_ins += jump_bits
    return binary_ins

