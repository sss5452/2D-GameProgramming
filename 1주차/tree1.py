import turtle as t

angle = 20
min_length = 100
reduce_rate =0.7

def tree(length):
    t.forward(length)
    if length> min_length:
        sub = length * reduce_rate
        t.left(angle)
        tree(sub)
        t.right(2*angle)
        tree(sub)
        t.left(angle)
    t.backword(length)
    
t.speed(0)
t.penup()
