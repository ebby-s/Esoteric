global memory, pointer
memory = [0]
pointer = 0
program = open("program.txt").read().replace("\n","")

def execute(program):        
    global memory, pointer
    for i,char in enumerate(program):
        #print(memory,char)
        if char == ">": move_pointer(1)
        elif char == "<": move_pointer(-1)
        elif char == "+": memory[pointer] += 1
        elif char == "-": memory[pointer] -= 1
        elif char == "[": run_loop(program,i)
        elif char == "]": """nothing"""
        elif char == ",": """nothing"""
        elif char == ".": print(chr(memory[pointer]))
        else: print(memory,pointer)

def move_pointer(direction):
    global memory, pointer
    pointer += direction
    while pointer < 0:
        memory.insert(0,0)
    while pointer > len(memory)-1:
        memory.append(0)

def run_loop(program,pos):
    global memory, pointer
    loop = ""
    pos += 1
    char = ""
    while char != "]":
        loop += char
        char = program[pos]
        pos += 1
    while memory[pointer] > 1:
        execute(loop)

execute(program)
