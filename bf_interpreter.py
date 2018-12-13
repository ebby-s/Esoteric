global memory, pointer, in_memory, in_pointer
memory = [0]
pointer = 0
in_pointer = 0

def execute(program):        # Executes program
    #print(program)
    global memory, pointer, in_memory, in_pointer
    balance = 0
    loop = False
    for i,char in enumerate(program):
        #print(memory,char)
        if char == ">" and not loop: move_pointer(1)
        elif char == "<" and not loop: move_pointer(-1)
        elif char == "+" and not loop: memory[pointer] += 1
        elif char == "-" and not loop: memory[pointer] -= 1
        elif char == "[":
            if not loop:
                run_loop(program,i)
                loop = True
            balance += 1
        elif char == "]":
            balance -= 1
            if balance == 0: loop = False
        elif char == "," and not loop: take_input()
        elif char == "." and not loop: print(chr(memory[pointer]))
        elif char == "!" and not loop: print(memory,pointer)

def move_pointer(direction):   # Moves pointer to left or right
    global memory, pointer, in_memory, in_pointer
    pointer += direction
    while pointer < 0:
        memory.insert(0,0)
        pointer += 1
    while pointer > len(memory)-1:
        memory.append(0)

def run_loop(program,pos):    # Executes loop
    global memory, pointer, in_memory, in_pointer
    loop = ""
    pos += 1
    char = ""
    balance = 0
    while char != "]" or balance != 0:
        #print(program,pos)
        if char == "[": balance += 1
        elif char == "]": balance -= 1
        loop += char
        char = program[pos]
        pos += 1
    while memory[pointer] != 0:
        execute(loop)

def take_input():
    global memory, pointer, in_memory, in_pointer
    try:
        memory[pointer] = ord(in_memory[in_pointer])
        in_pointer += 1
    except: memory[pointer] = 0

if __name__ == "__main__":
    in_memory = [chr(3),chr(4)]
    program = open("happy birthday.bf").read().replace("\n","")
    execute(program)
