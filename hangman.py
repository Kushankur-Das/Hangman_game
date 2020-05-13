def main():
  import random
  name=input("Enter your name buddy?")
  print(f"well {name}, Let's play the game!")
  level=str(input("Select the level for which you want to play this game. (Enter 'e' for Easy Level 'm' for medium level 'h' for high level"))
  if(level=='e'):
    turns=20
  elif(level=='m'):
    turns=15
  else:
    turns=10
  wordlist = ['rainbow' ,'computer', 'science', 'programming', 'python', 'mathematics', 'player', 'condition', 'reverse', 'water', 'board', 'chess']
  hidden_word=random.choice(wordlist)
  print("Guess the charecters")
  guesses=''
  while turns>0:
    failed=0
    for char in hidden_word:
      if char in guesses:
        print(char)
      else:
        print("_")
        failed+=1
    if failed==0:
      print("YOU WIN")
      break
    guess=input("guess a charecter:")
    guesses+=guess
    if guess not in hidden_word:
      turns -= 1
      print("Wrong")
      print("You have", +turns,'more guesses')
      if turns == 0:
        print("You lose")
main()