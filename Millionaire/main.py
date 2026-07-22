questions = [
    ["who is shah Rukh Khan?", "Wresler", "Actor", "Astronaut", "Plumber", 2],
    ["What is capital of France?", "Delhi", "Paris", "Landon", "Berlin", 2],
    ["Largest planet ?", "Jupiter", "Saturn", "Uranus", "Earth", 1],
    ["Largest River ?", "Nile", "Amazon", "Chile", "yamuna", 2],
    ["Square root of 64?", "2", "4", "8", "64", 3],
    ["countrry called land of rising sun", "china", "North Korea", "South Korea", "Japan", 4],
    ["Who painted monalisa ?", "VVG", "Pablo picasso" , "Leonardo ", "Claude", 2],

    ]

for question in questions:
    print(question[0])
    print("a",question[1])
    print("b",question[2])
    print("c",question[3])
    print("d",question[4])
    a= int(input("enter 1 for a, 2 for b , 3 for c, 4 for d"))

    count = 0
    if question[5] == a:
        print("Correct answer")
        count = count + 1
    else:
        print("Wrong answer")
        break
