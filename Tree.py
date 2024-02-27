from fileinput import close, filename
import sys
import time
import turtle
import pytest
def apply_rule_once(s, rule):
    s1 = ''  
    for i in s:
        if i == rule[0]:
            s1 += rule[1]
        elif i != rule[0]:
            s1 += i
    return s1
def apply_rules_n(s, rules, iter):    
    for i in range(iter):
        for rule in rules:
            s = apply_rule_once(s, rule)
    return s

def turtle_follows_instruction(t, instructions, d, a, colors):
    positions = []
    headings = []
    turtle_colors = []
    i = 0
    while i < len(instructions):
        instruction = instructions[i]
        if instruction == 'F':
            t.forward(d)
        elif instruction == '+':
            t.right(a)
        elif instruction == '-':
            t.left(a)
        elif instruction == 'C':
            color_index = int(instructions[i + 1])
            t.color(colors[color_index])
            i += 1 
        i += 1
        positions.append(t.pos())
        headings.append(t.heading())
        turtle_colors.append(t.color())
    return positions, headings, turtle_colors 
    

def turtle_follows_instruction2(t, instructions, d, a, colors):
    save = []  
    i = 0
    while i < len(instructions):
        instruction = instructions[i]
        if instruction == 'F':
            t.forward(d)
        elif instruction == '+':
            t.right(a)
        elif instruction == '-':
            t.left(a)
        elif instruction == 'C':
            color_index = int(instructions[i + 1])
            t.color(colors[color_index])
            i += 1  
        elif instruction == '[':
            save.append((t.pos(), t.heading(), t.color()[0]))
        elif instruction == ']':
            if save:
                pos, heading, color = save.pop()  
                t.penup()
                t.setpos(pos)
                t.setheading(heading)
                t.color(color)
                t.pendown()
        i += 1

def assert_turtle_states(t, locs, heads, cols, exp_locs, exp_heads):
    assert exp_locs[-1] == pytest.approx(t.position())
    assert exp_heads[-1] == pytest.approx(t.heading())
    assert len(heads) == len(exp_heads) and len(locs) == len(exp_locs)
    for i in range(len(exp_locs)):
        assert exp_heads[i] == pytest.approx(heads[i]) 
        assert exp_locs[i] == pytest.approx(locs[i])

def init_turtle():
    turtle.reset()
    turtle.clearscreen()
    turtle.setup(width=800, height=800)
    turtle.tracer(0)
    t = turtle.Turtle()
    t.left(90)
    return t

def cleanup_turtle():
    turtle.bye()
    turtle.Turtle._screen = None  
    turtle.TurtleScreen._RUNNING = True  

def test_q7_turtle_follows_instruction():
    t = init_turtle()
    locs, heads, cols = turtle_follows_instruction(t, 'F', 100, 0, [])

    locs, heads, cols = turtle_follows_instruction(t, 'F', 100, 0, [])

    locs, heads, cols = turtle_follows_instruction(t, '+', 100, 90, [])

    locs, heads, cols = turtle_follows_instruction(t, '+', 100, 90, [])

    locs, heads, cols = turtle_follows_instruction(t, '-', 100, 45, [])

    locs, heads, cols = turtle_follows_instruction(t, '-', 100, 45, [])

    locs, heads, cols = turtle_follows_instruction(t, 'FF', 100, 90, [])

    locs, heads, cols = turtle_follows_instruction(t, '++', 100, 45, [])

    locs, heads, cols = turtle_follows_instruction(t, 'F+F+F', 200, 90, [])
    cleanup_turtle()    


def test_q8_turtle_follows_instruction2():
    t = init_turtle()
    turtle_follows_instruction2(t, 'F[F]', 100, 90, [])
    turtle_follows_instruction2(t, 'F[F+F]', 100, 90, [])
    turtle_follows_instruction2(t, '[F[F[F]', 100, 90, [])
    turtle_follows_instruction2(t, '[F[F[F]]', 100, 90, [])
    turtle_follows_instruction2(t, '[F[F[F]]]', 100, 90, [])
    turtle_follows_instruction2(t, '[+[+[+', 100, 10, [])
    turtle_follows_instruction2(t, '[+[+[+]', 100, 10, [])
    turtle_follows_instruction2(t, '[+[+[+]]', 100, 10, [])
    turtle_follows_instruction2(t, '[+[+[+]]]', 100, 10, [])
    

def test_q9_turtle_following_rules():
    colors = [(140/255, 80/255, 60/255), (24/255, 180/255, 24/255), (48/255, 220/255, 48/255), (64/255, 255/255, 64/255)]
    start = 'F'
    rule = ['F', 'C0FF+[C1+F-F-F]-[C2-F+F+F]']
    rules = [rule]
    instructions = apply_rules_n(start, rules, 5)
    t = init_turtle()
    t.penup()
    t.setpos(0, -200)
    t.pendown()
    turtle_follows_instruction2(t, instructions, 4, 25, colors)
    turtle.getscreen().getcanvas().postscript(colormode='color', file='beautiful_rules1.ps')
    #turtle.mainloop()
    t.reset()
    t.penup()
    t.setpos(0, -200)
    t.left(90)
    t.pendown()
    start = 'FX'
    rule1 = ['F','C0FF-[C1-F+F]+[C2+F-F]']
    rule2 = ['X','C0FF+[C1+F]+[C3-F]']
    rules = [rule1, rule2]
    instructions = apply_rules_n(start, rules, 5)
    turtle_follows_instruction2(t, instructions, 4, 25, colors)
    turtle.getscreen().getcanvas().postscript(colormode='color', file='beautiful_rules2.ps')
    turtle.mainloop()

test_q9_turtle_following_rules()
