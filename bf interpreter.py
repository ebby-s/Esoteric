global memory, pointer, in_memory, in_pointer
memory = [0]
pointer = 0
in_memory = [0]
in_pointer = 0
program = open("program.txt").read().replace("\n","")

def execute(program):        # Executes program
    global memory, pointer, in_memory, in_pointer
    for i,char in enumerate(program):
        #print(memory,char)
        if char == ">": move_pointer(1)
        elif char == "<": move_pointer(-1)
        elif char == "+": memory[pointer] += 1
        elif char == "-": memory[pointer] -= 1
        elif char == "[": run_loop(program,i)
        elif char == "]": """ends loop"""
        elif char == ",": """inputs a character"""
        elif char == ".": print(chr(memory[pointer]))
        else: print(memory,pointer)

def move_pointer(direction):   # Moves pointer to left or right
    global memory, pointer, in_memory, in_pointer
    pointer += direction
    while pointer < 0:
        memory.insert(0,0)
    while pointer > len(memory)-1:
        memory.append(0)

def run_loop(program,pos):    # Executes loop
    global memory, pointer, in_memory, in_pointer
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
