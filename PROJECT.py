name = input("Enter Your Name: ")
gaming_name = input("Enter your Cool aka Gaming Name: ")
print("Welcome", name,"aka", gaming_name,"to the Contest of Champions")

answer = input("Who will choose ..... Captain America/Iron Man/Black Widow/Hawkeye/Hulk/Thor ")
if answer == 'Captain America':
    opponent = input("Choose your opponent Iron Man/Thor/Hulk ")
    if opponent == 'Thor':
        print("Captain America Lose.... Game Over!!")
    elif opponent == 'Iron Man':
        print("Captain America Wins....", gaming_name,"win!!")
    else:
        print("Captain America Wins....", gaming_name,"You win!!")
elif answer == 'Thor':
    print("Thor Always Wins....Congrats Mighty Champion", gaming_name,"You Win!!")
elif answer == 'Hulk':
    opponent = input("Choose your opponent Iron Man/Black Widow/Hawkeye ")
    if opponent == 'Iron Man':
        print("Hulk Lose.... Game Over!!")
    elif opponent == 'Hawkeye':
        print("Hulk Wins....", gaming_name,"You win!!")
    else:
        print("Hulk Wins....", gaming_name,"You win!!")
elif answer == 'Iron Man':
    opponent = input("Choose your opponent Black Widow/Hulk/Captain America ")
    if opponent == 'Captain America':
        print("Iron Man Lose.... Game Over!!")
    elif opponent == 'Hulk':
        print("Iron Man Wins....", gaming_name,"You Win!!")
    else:
        print("Iron Man Wins....", gaming_name,"You Win!!")
elif answer == 'Hawkeye':
    opponent = input("Choose Your opponent Hulk/Black Widow/Thor ")
    if opponent == 'Thor':
        print("Hawkeye Lose.... Game Over!!")
    elif opponent == 'Black widow':
        print("Hawkeye Wins....", gaming_name,"You Win!!")
    else:
        print("Hawkeye Wins....", gaming_name,"You Win!!")
elif answer == 'Black Widow':
    print("Black Widow always Lose....She is only known for her looks.... not for power.... Better luck next time", gaming_name,"Game Over!!")
else:
    print("You could't write the characters name correct .... You can't be a Champion", gaming_name,"You are Cuttttttttt !!!!!!!!!!!!")


print("Had Fun", gaming_name, "Cause it's My Even Semester Project....")
print("Thank You")
print("Developer of this game ::: ")
print("YASHANK RAJVANSHI       yashankrajvanshi@gmail.com")

input("press any key to exit")
