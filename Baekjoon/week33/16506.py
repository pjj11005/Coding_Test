import sys

input = sys.stdin.readline


def solution():
  opcode = {
      'ADD': 0, 'ADDC': 1,
      'SUB': 2, 'SUBC': 3,
      'MOV': 4, 'MOVC': 5,
      'AND': 6, 'ANDC': 7,
      'OR': 8, 'ORC': 9,
      'NOT': 10,
      'MULT': 12, 'MULTC': 13,
      'LSFTL': 14, 'LSFTLC': 15,
      'LSFTR': 16, 'LSFTRC': 17,
      'ASFTR': 18, 'ASFTRC': 19,
      'RL': 20, 'RLC': 21,
      'RR': 22, 'RRC': 23
  }

  for _ in range(int(input())):
    op, rd, ra, rb = input().split()
    
    # ra 사용 안함
    if op in {'MOV', 'MOVC', 'NOT'}:
      ra = 0
      
    rd, ra, rb = int(rd), int(ra), int(rb)
    
    result = bin(opcode[op])[2:].zfill(5) # 0 ~ 4
    result += '0' # 5
    result += bin(rd)[2:].zfill(3) # 6 ~ 8
    result += bin(ra)[2:].zfill(3) # 9 ~ 11
    # 12 ~ 15
    # rb
    if result[4] == '0':
      result += bin(rb)[2:].zfill(3) + '0'
    # C#
    else:
      result += bin(rb)[2:].zfill(4)

    print(result)

if __name__ == '__main__':
  solution()
