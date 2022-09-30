code = list('+++++[>++<-]>[<++++++++++>-]<.>---->>>>')
tape = [0 for x in range(2)]
postion = 0

#very simple brainfuck I made in ~20 min

def loop_interp(pos, code):
  global tape, postion
  end = pos
  while code[end] != ']':
    end += 1
  code = code[pos+1:end+1]
  i = 0
  while True:
    if code[i] == ']':
      if tape[postion]-1 < 1:
        break
      else:
        i = -1
    elif code[i] == '+':
      tape[postion] += 1
    elif code[i] == '-':
      if tape[postion] > 0:
        tape[postion] -= 1
    elif code[i] == '<':
      if postion > 0:
        postion -= 1
    elif code[i] == '>':
      if postion > len(tape) - 2:
        tape.append(0)
      postion += 1
    elif code[i] == '.':
      print(tape[postion])
    elif code[i] == ',':
      tape[postion] = int(input(f'{postion}: '))
    i += 1

def main():
  for i in range(len(code)):
    if code[i] == '+':
      tape[postion] += 1
    elif code[i] == '-':
      if tape[postion] > 0:
        tape[postion] -= 1
    elif code[i] == '<':
      if postion > 0:
        postion -= 1
    elif code[i] == '>':
      if postion > len(tape) - 2:
        tape.append(0)
      postion += 1
    elif code[i] == '.':
      print(tape[postion])
    elif code[i] == ',':
      tape[postion] = int(input(f'{postion}: '))
    elif code[i] == '[':
      loop_interp(i, code)

if __name__ == "__main__":
    main()
