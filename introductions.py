# write a function that takes 2 pieces of input (2 people), and introduces one to another
# prompt the user for 2 names
# Call your function, which should then print an introduction: introducing one person to another

def introduce(i,j):
    return("Hello " + i + " allow me to introduce you to " + j)
    
p1 = input("What is your name?: ")
p2 = input("And what is your name?: ")
print(introduce(p1,p2))
