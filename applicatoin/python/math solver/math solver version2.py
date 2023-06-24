import random
import time

charectrs = ["abdullah","salah","ali","sofia","mahmoud","your mom","your dad","your ant","your naibor"]
numbers =  [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]
correct_answers = 0
incorrect_answers = 0

print("there are a lot of peapole that need your help only you know math I am deppending on you save the world\n")
time.sleep(1)
player = input("what is your name king of math? ")
print("\n")
time.sleep(1)
print(f"hello {player} lets see how well you know math answer thise problem")

while True:
    problem =random.choice(numbers)
    problem1 = random.choice(numbers)
    problem2 = random.choice(charectrs)
    print(f"{problem2} needs you very quickly to solve thise problem")
    time.sleep(1)
    n = int( input(f" {problem} x {problem1} = "))
    if problem * problem1 == n:
        time.sleep(1)
        print("that seems like the correct answer\n")
        correct_answers += 1
    else:
        time.sleep(1)
        print("oops wrong answer\n")
        incorrect_answers -= 1

    print(f"correct answers => {correct_answers}")
    print(f"incorrect anserwes => {incorrect_answers}\n")
    del problem, problem1
    problem = random.choice(numbers)
    problem1 = random.choice(numbers)

    if correct_answers == 10:
        print("great job you won the game")
    elif incorrect_answers == 10:
        print("you are terribale at math")

    
    


