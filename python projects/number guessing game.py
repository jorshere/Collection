from random import randrange
def num_guess():
    lucky_num = randrange(0,100)
    count=1
    print("\t\t\t::WELCOME TO THE NUMBER GUESSING GAME::")
    num= int(input("\nGuess your lucky number between o to 100 :\t"))
    while num != lucky_num:
        if num > lucky_num:
            print("too high... try again:\t")
            num=int(input())
            count+=1
        else:
            print("too low... try again:\t")
            num=int(input())
            count+=1
    print(f"\n\t........Congratulations........ \nYou have Guessed the Lucky Number: {num}  in  {count} chances..")

num_guess()
