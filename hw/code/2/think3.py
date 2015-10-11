#Do exercises 3.1, 3.2, 3.3, 3.4, 3.5 in think3.py
#Do 4.2 and 4.3 and add figures think4/_2.png and think4/_3.png
#Exercises 3.1 and 3.2
def repeat_lyrics():
    print_lyrics()
    print_lyrics()
    
def print_lyrics():
    print "I'm a lumberjack, and I'm okay."
    print "I sleep all night and I work all day."
    
repeat_lyrics()

#Exercise 3.3
def right_justify(s):
    total_spaces = 70
    leading_spaces = total_spaces - len(s)
    leading_spaces_string = ""
    for x in range(0,leading_spaces):
        leading_spaces_string += " "
    print leading_spaces_string + s
    
right_justify("allen")

#Exercise 3.4
def do_twice(f, n):
    f(n)
    f(n)
    
def do_four(f,n):
    do_twice(f,n)
    do_twice(f,n)
    
def print_twice(phrase):
    print phrase

do_twice(print_twice, 'spam')

#Exercise 3.5
def print_four(n):
    print n,
    print n,
    print n,
    print n,

def box_piece(c,s,n):
    print c,
    print_four(s)
    print c,
    print_four(s)
    if n == 4:
        print c,
        print_four(s)
        print c,
        print_four(s)
    print c
    
def box_side(n):
    box_piece("/"," ",n)
    box_piece("/"," ",n)
    box_piece("/"," ",n)
    box_piece("/"," ",n)
    
def box_top(n):
    box_piece("+","-",n)
    
def draw_grid(n):
    box_top(n)
    box_side(n)
    box_top(n)
    box_side(n)
    if n == 4:
        box_top(n)
        box_side(n)
        box_top(n)
        box_side(n)
    box_top(n)
    
draw_grid(2)
draw_grid(4)