import random
import hangman_art
import hangman_words
from replit import clear

lives = 6
chosen_word = random.choice(hangman_words.word_list)
display = []

for letter in chosen_word:
  display += "_"

end_of_game = False

#print inicial screen
from hangman_art import logo, stages
print(logo)
print(stages[lives])
print(display)

while not end_of_game:
  #guess a letter
  guess = input("Guess a letter: ").lower()
  clear()
  if guess in display:
    print(f"You've already gessed this letter: {guess}")
  
  for position in range(len(chosen_word)):
    #print(position)
    letter = chosen_word[position]
    if letter == guess:
      #print('match')
      display[position] = letter
  
  if guess not in chosen_word:
    print(f"You gessed {guess}, that's not in the word. You loose a live.")
    lives -= 1
    
    if lives == 0:
      end_of_game = True
      print("You die")

  if "_" not in display:
    end_of_game = True
    print("You win")

  print(stages[lives])
  if lives > 0:
    print(display)
  
    
#print(f"Chosen: {chosen_word}")