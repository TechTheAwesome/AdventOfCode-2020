#Import input as raw string array
inputs = open('../raw_input/input.txt',).read().split('\n')

#Make it a grid
i = 0
while i < len(inputs):
    inputs[i] = list(inputs[i])
    i += 1

#Solve
tree = '#'
open = '.'
height = len(inputs) 
width = len(inputs[0]) 
answer = 0
x = 0
y = 1
while y < height:
    if x+3 > width - 1:
        x -= width
    x += 3
    #print(x,y,width, height)
    if inputs[y][x] == tree:
        answer += 1
    y +=1


print(answer)