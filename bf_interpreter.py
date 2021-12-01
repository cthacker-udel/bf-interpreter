def bf_interpreter(astr):

    ## starts at cell 0
    current_point = 0
    cells = [0]
    input_mode = False
    anchor_index = 0
    index = 0
    stack_ = []
    while index < len(astr):
        eachletter = astr[index]
        if input_mode:
            cells[current_point] = ord(eachletter)
            input_mode = False
        if eachletter == '+':
            cells[current_point] += 1
        elif eachletter == '-':
            cells[current_point] -= 1
        elif eachletter == '.':
            print(chr(cells[current_point]))
        elif eachletter == ',':
            input_mode = True
        elif eachletter == '[':
            if cells[current_point] == 0:
                ## jump past matching ]
                for i in range(index-1,len(astr)):
                    if astr[i] == ']' and len(stack_) == 0:
                        index = i+1
                        break
                    elif astr[i] == ']':
                        stack_.pop()
                    elif astr[i] == '[' and len(stack_) == 0:
                        stack_.append(astr[i])
                stack_ = []
        elif eachletter == ']':
            if cells[current_point] != 0:
                for i in range(index-1,-1,-1):
                    if astr[i] == '[' and len(stack_) == 0:
                        index = i
                        break
                    elif astr[i] == ']':
                        stack_.append(astr[i])
                    elif astr[i] == '[':
                        stack_.pop()
                stack_ = []
        elif eachletter == '>':
            if len(cells)-1 == current_point:
                cells.append(0)
                current_point += 1
            else:
                current_point += 1
        elif eachletter == '<':
            if current_point == 0:
                current_point = len(cells)-1
            else:
                current_point -= 1
        index += 1
