# Python program for Plotting Fibonacci
# spiral fractal using Turtle
import turtle
import math

  
def fibonacci_plot(number_of_interactions):

        
    first_variable = 0
    second_variable = 1
    square_a = first_variable
    square_b = second_variable
 
    # Setting the colour of the plotting pen to blue
    x.pencolor("blue")
 
    # Drawing the first square
    x.forward(second_variable * factor)
    x.left(90)
    x.forward(second_variable * factor)
    x.left(90)
    x.forward(second_variable * factor)
    x.left(90)
    x.forward(second_variable * factor)
 
    # Proceeding in the Fibonacci Series
    temporary = square_b
    square_b = square_b + square_a
    square_a = temporary
     
    # Drawing the rest of the squares
    
    for i in range(1, number_of_interactions):
        
        x.backward(square_a * factor)
        x.right(90)
        x.forward(square_b * factor)
        x.left(90)
        x.forward(square_b * factor)
        x.left(90)
        x.forward(square_b * factor)
 
        # Proceeding in the Fibonacci Series
        temporary = square_b
        square_b = square_b + square_a
        square_a = temporary
 
    # Bringing the pen to starting point of the spiral plot
    x.penup()
    x.setposition(factor, 0)
    x.seth(0)
    x.pendown()
 
    # Setting the colour of the plotting pen to red
    x.pencolor("red")
 
    # Fibonacci Spiral Plot
    x.left(90)
    
    for i in range(number_of_interactions):
        
        print(second_variable)
        fdwd = math.pi * second_variable * factor / 2
        fdwd /= 90
        
        for j in range(90):
            
            x.forward(fdwd)
            x.left(1)
        temporary = first_variable
        first_variable = second_variable
        second_variable = temporary + second_variable
 
 
# Here 'factor' signifies the multiplicative
# factor which expands or shrinks the scale
# of the plot by a certain factor.
factor = 1
 
# Taking Input for the number of
# Iterations our Algorithm will run
number_of_interactions = 15
 
# Plotting the Fibonacci Spiral Fractal
# and printing the corresponding Fibonacci Number

if number_of_interactions > 0:
    
    print("Fibonacci series for", number_of_interactions, "elements :")
    x = turtle.Turtle()
    x.speed(100)
    fibonacci_plot(number_of_interactions)
    turtle.done()
    
else:
    
    print("Number of iterations must be > 0")