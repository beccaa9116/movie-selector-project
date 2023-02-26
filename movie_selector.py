import random

#For a bit of context, this is a selector I saw and I decided that I want to take this to another level 
#so I'm gonna try to make a program that's gonna choose what I should watch on Disney+
#  friends = ['Olek','Carmela','Laura','Megan','Keith','Anna','Skyler','Amy','Nadya']
#  random.randint(1, 5) --> random number between 1 and 5
#  random.choice(array) --> random item in this array
#  selected = random.choice(friends) # randomly choose a friend
#  print('Who should I facetime today?')
#  print(selected)

#little program header:
print("\nLet the program decide what you should watch on Disney+\n")

import csv

#spent a quality amount of time trying to figure out the right directory for this 
# and the right way to import it into the list but I think we got it!
file = open("/data/animated_movies.csv", "r")
animated_movies = list(csv.reader(file))
file.close()

#now let's import all the lists we have, I'm thinking about dividing it into tv series and movies (just so we have a bunch of more data, exciting!)
#all these lists are just data I downloaded from web rn so the lists might differ in the future, but it's still fun this way so let's go

file = open("/data/animated_series.csv", "r")
animated_series = list(csv.reader(file))
file.close()

file = open("/data/disney_exclusive_series.csv", "r")
exclusive_series = list(csv.reader(file))
file.close()

file = open("/data/disney_exclusive_movies.csv", "r")
exclusive_movies = list(csv.reader(file))
file.close()

file = open("/data/documentaries.csv", "r")
documentaries = list(csv.reader(file))
file.close()

file = open("/data/liveaction_series.csv", "r")
liveaction_series = list(csv.reader(file))
file.close()

file = open("/data/liveaction_movies.csv", "r")
liveaction_movies = list(csv.reader(file))
file.close()

file = open("/data/marvel.csv", "r")
marvel = list(csv.reader(file))
file.close()

file = open("/data/pixar.csv", "r")
pixar = list(csv.reader(file))
file.close()

file = open("/data/star_wars.csv", "r")
star_wars = list(csv.reader(file))
file.close()

#everything successfully imported... phew
#I'm just gonna list out our first options:
print("These are the categories you can choose from: \n1. movies \n2. series \n3. documentaries \n4. special collections \n")

#let the user choose:
choice = input("Which category sounds the best? (1, 2, 3, 4): ")
if choice in ('1','2','3','4'):

 if choice == '1':
  print("\nGreat, you chose a movie. Your options now are: \n1. animated \n2. disney exclusive \n3. live action \n")
  choice2 = input("Make a choice (1, 2, 3): ")
  if choice2 in ('1', '2', '3'):
   if choice2 == '1':
    selected = random.choice(animated_movies)
    print(f"The animated movie you should watch is: {selected}")
   elif choice2 == '2':
    selected = random.choice(exclusive_movies)
    print(f"The disney exclusive movie you should watch is: {selected}")
   elif choice2 == '3':
    selected = random.choice(liveaction_movies)
    print(f"The live action movie you should watch is: {selected}")
  else:
   print("We don't have such movie, sorry.")

 elif choice == '2':
  print("\nGreat, you chose series. Your options now are: \n1. animated \n2. disney exclusive \n3. live action \n")
  choice2 = input("Make a choice (1, 2, 3): ")
  if choice2 in ('1', '2', '3'):
   if choice2 == '1':
    selected = random.choice(animated_series)
    print(f"The animated series you should watch is: {selected}")
   elif choice2 == '2':
    selected = random.choice(exclusive_series)
    print(f"The disney exclusive series you should watch is: {selected}")
   elif choice2 == '3':
    selected = random.choice(liveaction_series)
    print(f"The live action series you should watch is: {selected}")
  else:
   print("We don't have such series, sorry.")
  
 elif choice == '3':
  selected = random.choice(documentaries)
  print(f"The documentary you should watch is: {selected}")

 elif choice == '4':
  print("\nGreat, we have these special collections: \n1. marvel \n2. pixar \n3. star wars \n")
  choice2 = input("Make a choice (1, 2, 3): ")
  if choice2 in ('1', '2', '3'):
   if choice2 == '1':
    selected = random.choice(marvel)
    print(f"The piece from marvel you should watch is: {selected}")
   elif choice2 == '2':
    selected = random.choice(pixar)
    print(f"The piece from pixar you should watch is: {selected}")
   elif choice2 == '3':
    selected = random.choice(star_wars)
    print(f"The piece from star wars you should watch is: {selected}")
  else:
   print("We don't have such collection, sorry.")

else:
 print("That category is not on our list, sorry.")

#after quite a bit of time we have all the choices here and now we can let the program decide what we should watch
#I don't know if this is the best way to do this, but honestly this is the frist thing I programmed all by myself in Python and I can't be happier even if it is a bit messy.