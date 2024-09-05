import turtle

# Configurar a tela
turtle.setup(width=600, height=600)
turtle.bgcolor("white")

# Configurar a tartaruga
pen = turtle.Turtle()
pen.color("red")
pen.pensize(3)
pen.speed(1)

# Desenhar o coração
pen.begin_fill()
pen.left(50)
pen.forward(133)
pen.circle(50, 200)
pen.right(140)
pen.circle(50, 200)
pen.forward(133)
pen.end_fill()

# Esconder a tartaruga
pen.hideturtle()

# Manter a janela aberta
turtle.done()