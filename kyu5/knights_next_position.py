"""

kata_id: https://www.codewars.com/kata/6243819a58ad06b6c663d32b

The reason is why this code looks something strange is limited code length

"""
next_pos=lambda p:[f'{chr(x)}{y}' for s,d in zip((-2,-2,-1,-1,1,1,2,2),(-1,1,-2,2,-2,2,-1,1)) if 1<=(y:=int(p[1])+d)<=8 and 97<=(x:=ord(p[0])+s)<=104]
