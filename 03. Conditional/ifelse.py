scissor = '가위'
rock = '바위'
paper = '보'

win = '이겼습니다!'
draw = '비겼습니다.'
lose = '졌습니다...'

mine = paper
yours = rock

result = ''

if (mine == rock and yours == scissor) or (mine == paper and yours == rock) or (mine == scissor and yours == paper):
    result = win
elif (mine == scissor and yours == rock) or (mine == rock and yours == paper) or (mine == paper and yours == scissor):
    result = lose
else:
    result = draw

print(result)
