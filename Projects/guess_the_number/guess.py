import random
HowManyGusses = 0
print('Hello! what is your name ?')
myName = raw_input()

rand_num = random.randint(1,33)
print("well," +myName+ ",I am thinking of a number between 1 and 33.")


while HowManyGusses < 10:
    print("Take a Guess ", myName )
    guess = raw_input()
    guess = int(guess)

    HowManyGusses = HowManyGusses + 1
    if HowManyGusses == 5:
        print ("Last chance left to guess", myName)

    if guess < rand_num:
        print ("Your Guess is Too Low", myName)
    if guess > rand_num:
        print ("Your Guess is Too High", myName)
    if guess > 33:
        print ("Please Enter a number in between 1 and 33", myName)
    if guess == rand_num:
        break

if guess == rand_num:
    HowManyGusses = str(HowManyGusses)
    print ("Good Job, "+myName+ "! You Guessed my number in "+HowManyGusses+",guesses")
if guess != rand_num:
    rand_num = str(rand_num)
    print("Nope. The Number i was Thinking of was " +rand_num)
