
'''
pyching - a python version of the iching
'''


import random       # To generate the coin toss
import os           # To clear the screen
import time

# THE EIGHT TRIGRAMS / 3 LINES
CH_IEN = "---\n---\n---"
CHEN = "- -\n- -\n---"
K_AN = "- -\n---\n- -"
KEN = "---\n- -\n- -"
K_UN = "- -\n- -\n- -"
SUN = "---\n---\n- -"
LI = "---\n- -\n---"
TUI = "- -\n---\n---"


# THE SIXTY FOUR HEXAGRAMS / 6 LINES
HEXAGRAM1 = CH_IEN + CH_IEN # first value is the upper trigram and the second value the lower trigram
HEXAGRAM2 = K_UN + K_UN
HEXAGRAM3 = K_AN + CHEN
HEXAGRAM4 = KEN + K_AN
HEXAGRAM5 = K_AN + CH_IEN
HEXAGRAM6 = CH_IEN + K_AN 
HEXAGRAM7 = K_UN + K_AN
HEXAGRAM8 = K_AN + K_UN
HEXAGRAM9 = SUN + CH_IEN
HEXAGRAM10 = CH_IEN + TUI 
HEXAGRAM11 = K_UN + CH_IEN 
HEXAGRAM12 = CH_IEN + K_UN
HEXAGRAM13 = CH_IEN + LI
HEXAGRAM14 = LI + CH_IEN
HEXAGRAM15 = K_UN + KEN
HEXAGRAM16 = CHEN + K_UN
HEXAGRAM17 = TUI + CHEN
HEXAGRAM18 = KEN + SUN
HEXAGRAM19 = K_UN + TUI
HEXAGRAM20 = SUN + K_UN
HEXAGRAM21 = LI + CHEN
HEXAGRAM22 = KEN + LI
HEXAGRAM23 = KEN + K_UN
HEXAGRAM24 = K_UN + CHEN
HEXAGRAM25 = CH_IEN + CHEN
HEXAGRAM26 = KEN + CH_IEN
HEXAGRAM27 = KEN + CHEN
HEXAGRAM28 = TUI + SUN
HEXAGRAM29 = K_AN + K_AN
HEXAGRAM30 = LI + LI
HEXAGRAM31 = TUI + KEN
HEXAGRAM32 = CHEN + SUN
HEXAGRAM33 = CH_IEN + KEN
HEXAGRAM34 = CHEN + CH_IEN
HEXAGRAM35 = LI + K_UN
HEXAGRAM36 = K_UN + LI
HEXAGRAM37 = SUN + LI
HEXAGRAM38 = LI + TUI
HEXAGRAM39 = K_AN + KEN
HEXAGRAM40 = CHEN + K_AN
HEXAGRAM41 = KEN + TUI
HEXAGRAM42 = SUN + CHEN
HEXAGRAM43 = TUI + CH_IEN
HEXAGRAM44 = CH_IEN + SUN
HEXAGRAM45 = TUI + K_UN
HEXAGRAM46 = K_UN + SUN
HEXAGRAM47 = TUI + K_AN
HEXAGRAM48 = K_AN + SUN
HEXAGRAM49 = TUI + LI
HEXAGRAM50 = LI + SUN
HEXAGRAM51 = CHEN + CHEN
HEXAGRAM52 = KEN + KEN
HEXAGRAM53 = SUN + KEN
HEXAGRAM54 = CHEN + TUI
HEXAGRAM55 = CHEN + LI
HEXAGRAM56 = LI + KEN
HEXAGRAM57 = SUN + SUN
HEXAGRAM58 = TUI + TUI
HEXAGRAM59 = SUN + K_AN
HEXAGRAM60 = K_AN + TUI
HEXAGRAM61 = SUN + TUI
HEXAGRAM62 = CHEN + KEN
HEXAGRAM63 = K_AN + LI
HEXAGRAM64 = LI + K_AN


def title_screen():
  # A lot of terminal windows follows lol
  os.system('cls||clear')
  print()
  print("|<-------------------- Please E X P A N D your terminal window ------------------->|")
  print()
  print()
  print()
  print("---                                                                              - -")
  print("- -                                 * pyching *                                  ---")
  print("---                                                                              - -")
  print()
  print("This is a python version of the 'iching' (not an apple product lol)")
  print()

  print("The iching (or 'Book of Change') has been used for centuries to predict the future.")
  print("It is an oracle of sorts... You just need a good enough question to ask it!")
  print()
  input("Press [Enter/Return] to continue")
  print()

  os.system('cls||clear')
  print("Would you like to know how it works?")
  print()
  print("- Yeah, tell me about TRIGRAMS, HEXAGRAMS and a bit of background [Enter/Return]")
  print("- Don't care! I just wanna know my future! [skip]")
  print()


def learn_or_question():
  user_answer = input("Type 'skip' or press [Enter/Return] to learn more ")
  if user_answer == "":
      learn_about_iching()
  if user_answer == "skip" or "SKIP" or "Skip":
      user_question = question()
  return user_question


def learn_about_iching():
  os.system('cls||clear')
  print("The iching is a co-operative effort spanning many centuries,")
  print("formed from observation of the way things change.")
  print()
  print("In the same manner that there are patterns and cycles to nature,")
  print("so too there are patterns and cycles to human affairs.")
  print()
  input("Press [Enter/Return]")
  print()

  os.system('cls||clear')
  print("These patterns and repetitions of life are represented in the iching by 8 TRIGRAMS:")
  print()
  print("---      - -      - -      ---      - -      ---      ---      - -")
  print("---      - -      ---      - -      - -      ---      - -      ---")
  print("---      ---      - -      - -      - -      - -      ---      ---")
  print()
  print("Ch'ien   Chen     K'an     Ken      K'un     Sun      Li       Tui")
  print()
  input("Press [Enter/Return]")

  os.system('cls||clear')
  print("The eight TRIGRAMS, via an interconnected system of relations, combine to create sixty four unique HEXAGRAMS.")
  print("An example of a six line HEXAGRAM:")
  print()
  print("---\n- -   } Upper Trigram: Li \n---.")
  print("---\n---   } Lower Trigram: Ch'ien \n--- ")
  print()
  input("Press [Enter/Return]")

  os.system('cls||clear')
  print("These TRIGRAMS and resulting HEXAGRAMS are made with randomness!")
  print()
  print("Traditionally this was done with sticks but it can be done by flipping (python) coins")
  print()
  print("In the same manner we take a picture to capture a moment in time,")
  print("we use the random result of the coins to isolate your present mindset... and peer into your future!")
  print()
  input("Press [Enter/Return]")

  os.system('cls||clear')
  print("HOW TRIGRAMS / HEXAGRAMS ARE MADE:")
  print()
  print("---   =   2 heads, 1 tail")
  print("- -   =   2 tails, 1 head")
  print("---.  =   all tails")
  print("- -.  =   all heads")
  print()
  print("NOTE: Trigrams are created from the bottom up!")
  print()
  input("Press [Enter/Return]")

  os.system('cls||clear')
  print("One last thing to note, TRIGRAMS/HEXAGRAMS change!")
  print()
  print("If you generate a TRIGRAM/HEXAGRAM with a '.' a second 'opposite' will be created")
  print()
  print("- -.                                 ->                                     ---")
  print("---.                                 ->                                     - -")
  print("---                                  ->                                     ---")
  print("Tui                                                                          Li")
  print()
  input("Press [Enter/Return]")


def question():
  os.system('cls||clear')
  print("Ready with your question?")
  print()
  print("Seeking a yes or no answer will be unsatisfactory, ask open ended questions!")
  print("For example: 'In what way will learning to code impact my future quality of life?'")
  print("The more specific regarding the time, tense, people, place and the scope of what you want revealed, the better!")
  print()
  print("To approach the 'Book of Change' as though it were an intelligent, sensitive, living mind is not at all a mistake.")
  print("- From THE ICHING WORKBOOK by R. L. Wing")
  print()
  question = input("Type your question here then press [Enter/Return]: \n")
  os.system('cls||clear')
  while question == "":
      print("It can't be blank lol!")
      print()
      question = input("Type then press [Enter/Return]: ")
      os.system('cls||clear')
  return question


# This function is the bulk of the program, pretty much everything happens here:
def create_hexagrams(user_question):
  
  # Setting out all the variables that we're going to fill up
  
  answer = []

  # These are the original trigrams with dots (potentially) that we use for display purposes
  dotted_lower_trigram = ""
  dotted_upper_trigram = ""

  # If the trigram/hexagram has a dot then this will help signal the need to generate a second hexagram
  is_this_a_changing_hexagram = 0

  # These variables are stripped of the fullstops (from above variables) that we use to id in the HEXAGRAM directory
  lower_trigram = ""    
  upper_trigram = ""

  # These are stripped of the fullstops and used for identifying what the second hexagram is in the HEXAGRAM directory
  lower_trigram2 = ""
  upper_trigram2 = ""

  # These are for the final screen reveal, displaying the two hexagrams at once
  display_changing_hexagrams_low = ""
  display_changing_hexagrams_high = ""

  # we need to create two trigrams so we cycle around this function twice
  for x in range(2):
      heads_and_tails, n = create_trigram(x, answer)
      dotted_lower_trigram, dotted_upper_trigram = store_trigram(x, heads_and_tails, dotted_lower_trigram, dotted_upper_trigram)
      copy_of_heads_and_tails = copy_heads_and_tails(heads_and_tails)
      copy_of_heads_and_tails2 = copy_heads_and_tails2(heads_and_tails)
      lower_trigram2, upper_trigram2, is_this_a_changing_hexagram = store_second_hexagram(copy_of_heads_and_tails, x, is_this_a_changing_hexagram, lower_trigram2, upper_trigram2)
      display_changing_hexagrams_low, display_changing_hexagrams_high = display_hexagrams(copy_of_heads_and_tails2, x, display_changing_hexagrams_low, display_changing_hexagrams_high)
      lower_trigram, upper_trigram, is_this_a_changing_hexagram = remove_dots_to_compare(heads_and_tails, x, is_this_a_changing_hexagram, lower_trigram, upper_trigram)
      answer = id_the_trigram(lower_trigram, upper_trigram, x, answer)
      prompt(x)
  hexagrams(answer, is_this_a_changing_hexagram, lower_trigram, upper_trigram, dotted_lower_trigram, dotted_upper_trigram, user_question, lower_trigram2, upper_trigram2, display_changing_hexagrams_low, display_changing_hexagrams_high)


def flip_coins(heads_and_tails):

  line = []                               # Empty list that we temporarily fill

  for i in range(3):                      # Here we flip 3 coins at once
      line.append(random.randint(0,1))    # This adds the 3 coin flip result to 'line'
      if line[i] == 0:
          time.sleep(0.3)
          print("Heads")                  # It 'feels' right for the user to see the results
      elif line[i] == 1:
          time.sleep(0.3)
          print("Tails")
  heads_and_tails.append(line)            #keeps the coin toss result in memory

  line = []                               #wipes the heads and tails for another round of randomness
      
  return heads_and_tails


def create_trigram(x, answer):

      heads_and_tails = []

      for n in range(3): #we need to do the following three times 
          input("Press [Enter/Return] to flip 3 coins: ")
          os.system('cls||clear')
          heads_and_tails = flip_coins(heads_and_tails)                   # the coin flips are stored
          heads_and_tails, n = convert_to_string(heads_and_tails, n)      # and then converted into strings
          display_lines(heads_and_tails, n, x)                            # these strings are then displayed in the terminal
      return heads_and_tails, n


# This converts the 0s and 1s into our visual strings
def convert_to_string(heads_and_tails, n):

      # Turns 1 Tails into "---"
      if heads_and_tails[n] == [1, 0, 0]:
          heads_and_tails.remove([1, 0, 0])
          heads_and_tails.insert(n, "---")

      if heads_and_tails[n] == [0, 1, 0]:
          heads_and_tails.remove([0, 1, 0])
          heads_and_tails.insert(n, "---")

      if heads_and_tails[n] == [0, 0, 1]:
          heads_and_tails.remove([0, 0, 1])
          heads_and_tails.insert(n, "---")

      # Turn 2 Tails into "- -"
      if heads_and_tails[n] == [1, 1, 0]:
          heads_and_tails.remove([1, 1, 0])
          heads_and_tails.insert(n, "- -")

      if heads_and_tails[n] == [0, 1, 1]:
          heads_and_tails.remove([0, 1, 1])
          heads_and_tails.insert(n, "- -")

      if heads_and_tails[n] == [1, 0, 1]:
          heads_and_tails.remove([1, 0, 1])
          heads_and_tails.insert(n, "- -")

      # Turn 3 Heads into "- -."
      if heads_and_tails[n] == [0, 0, 0]:
          heads_and_tails.remove([0, 0, 0])
          heads_and_tails.insert(n, "- -.")

      # Turn 3 Tails into "---."
      if heads_and_tails[n] == [1, 1, 1]:
          heads_and_tails.remove([1, 1, 1])
          heads_and_tails.insert(n, "---.")
      print()

      return heads_and_tails, n

# This function essentially draws the trigram lines for the user to see
def display_lines(heads_and_tails, n, x):

  if x == 0:
      time.sleep(0.3)
      print(f"Line {n+1} of your Trigram = {heads_and_tails[n]}")
      if n == 1:
          print(f"Line 1 of your Trigram = {heads_and_tails[0]}")
      if n == 2:
          print(f"Line 2 of your Trigram = {heads_and_tails[1]}")
          print(f"Line 1 of your Trigram = {heads_and_tails[0]}")

  if x == 1:
      time.sleep(0.3)
      print(f"Line {n+4} of your Trigram = {heads_and_tails[n]}")
      if n == 1:
          print(f"Line 4 of your Trigram = {heads_and_tails[0]}")
      if n == 2:
          print(f"Line 5 of your Trigram = {heads_and_tails[1]}")
          print(f"Line 4 of your Trigram = {heads_and_tails[0]}")
  print()


def store_trigram(x, heads_and_tails, dotted_lower_trigram, dotted_upper_trigram):
  # For visual purposes we will save and display the dotted trigrams

  if x == 0:
      #The trigrams are created and displayed from the bottom line up
      dotted_lower_trigram = heads_and_tails[2] + "\n" + heads_and_tails[1] + "\n" + heads_and_tails[0]
  
  if x == 1:
      dotted_upper_trigram = heads_and_tails[2] + "\n" + heads_and_tails[1] + "\n" + heads_and_tails[0]
      
  return dotted_lower_trigram, dotted_upper_trigram


# The dotted trigrams are useful for display purposes but for ID purposes we need to strip them of the dots
def copy_heads_and_tails(heads_and_tails):
      # Below makes a copy of 'heads_and_tails' (before we alter it)
      heads_and_tails_copy = []
      for i in range(3):
          heads_and_tails_copy.append(heads_and_tails[i])
      return heads_and_tails_copy                             # we are going to use this copy and strip away the dots for the hexagram directory

# unoriginal name here lol 
def copy_heads_and_tails2(heads_and_tails):
      # Below makes a copy of 'heads_and_tails' (before we alter it)
      heads_and_tails_copy = []
      for i in range(3):
          heads_and_tails_copy.append(heads_and_tails[i])
      return heads_and_tails_copy                         # we are going to use this copy and strip away the dots for the final display


# Because Trigrams/Hexagrams can change, we need to create a (potential) 2nd hexagram 
def store_second_hexagram(copy_of_heads_and_tails, x, is_this_a_changing_hexagram, lower_trigram2, upper_trigram2):

  # The idea is that if a '.' is present in the first hexagram, we will create the second hexagram to display later.
  # This goes through the results and creates any opposite values trigged by the '.'.
  # We will then use the output to ID the second hexagram  
  for n in range(3):
      if copy_of_heads_and_tails[n] == "- -.":
          copy_of_heads_and_tails.remove("- -.")
          copy_of_heads_and_tails.insert(n, "---")
          is_this_a_changing_hexagram += 1

      if copy_of_heads_and_tails[n] == "---.":
          copy_of_heads_and_tails.remove("---.")
          copy_of_heads_and_tails.insert(n, "- -")
          is_this_a_changing_hexagram += 1

  if x == 0:
      lower_trigram2 = copy_of_heads_and_tails[2] + "\n" + copy_of_heads_and_tails[1] + "\n" + copy_of_heads_and_tails[0] 
  if x == 1:
      upper_trigram2 = copy_of_heads_and_tails[2] + "\n" + copy_of_heads_and_tails[1] + "\n" + copy_of_heads_and_tails[0] 

  return lower_trigram2, upper_trigram2, is_this_a_changing_hexagram


def display_hexagrams(copy_of_heads_and_tails2, x, display_changing_hexagrams_low, display_changing_hexagrams_high):

  # Whilst the previous function above is used to ID the second hexagram behind the scene, this function is for display purposes
  # At the end, if there are two hexagrams, the user gets to see directly how they change.

  for n in range(3):
      if copy_of_heads_and_tails2[n] == "- -.":
          copy_of_heads_and_tails2.remove("- -.")
          copy_of_heads_and_tails2.insert(n, "- -.             ->           ---")
      if copy_of_heads_and_tails2[n] == "---.":
          copy_of_heads_and_tails2.remove("---.")
          copy_of_heads_and_tails2.insert(n, "---.             ->           - -")
      if copy_of_heads_and_tails2[n] == "---":
          copy_of_heads_and_tails2.remove("---")
          copy_of_heads_and_tails2.insert(n, "---                           ---")
      if copy_of_heads_and_tails2[n] == "- -":
          copy_of_heads_and_tails2.remove("- -")
          copy_of_heads_and_tails2.insert(n, "- -                           - -")
      
      if x == 0:
          display_changing_hexagrams_low = copy_of_heads_and_tails2[2] + "\n" + copy_of_heads_and_tails2[1] + "\n" + copy_of_heads_and_tails2[0] 
      if x == 1:
          display_changing_hexagrams_high = copy_of_heads_and_tails2[2] + "\n" + copy_of_heads_and_tails2[1] + "\n" + copy_of_heads_and_tails2[0] 

  return display_changing_hexagrams_low, display_changing_hexagrams_high


def remove_dots_to_compare(heads_and_tails, x, is_this_a_changing_hexagram, lower_trigram, upper_trigram):

  # This function looks similar to previous ones but its made speicifcally to id the first hexagram.
  # We strip the full stops from the trigrams to help ID them against the database of TRIGRAMS
  # We have to process the heads_and_tails copies first because they alter the results in different ways

  for n in range(3):
      if heads_and_tails[n] == "- -.":
          heads_and_tails.remove("- -.")
          heads_and_tails.insert(n, "- -")
          is_this_a_changing_hexagram += 1

      if heads_and_tails[n] == "---.":
          heads_and_tails.remove("---.")
          heads_and_tails.insert(n, "---")
          is_this_a_changing_hexagram += 1

  if x == 0:
      lower_trigram = heads_and_tails[2] + "\n" + heads_and_tails[1] + "\n" + heads_and_tails[0]
  if x == 1:
      upper_trigram = heads_and_tails[2] + "\n" + heads_and_tails[1] + "\n" + heads_and_tails[0]

  return lower_trigram, upper_trigram, is_this_a_changing_hexagram


# This function IDs the trigram by referencing the eight trigram CONSTANTS
def id_the_trigram(lower_trigram, upper_trigram, x, answer):
  
  lower_upper = "Lower", "Upper" #alternating text

  if lower_trigram == CH_IEN or upper_trigram == CH_IEN:
      answer.append("Ch'ien")
      print(f"Your {lower_upper[x]} Trigram is: {answer[x]}")

  elif lower_trigram == CHEN or upper_trigram == CHEN:
      answer.append("Chen")
      print(f"Your {lower_upper[x]} Trigram is: {answer[x]}")

  elif lower_trigram == K_AN or upper_trigram == K_AN:
      answer.append("K'an")
      print(f"Your {lower_upper[x]} Trigram is: {answer[x]}")

  elif lower_trigram == KEN or upper_trigram == KEN:
      answer.append("Ken")
      print(f"Your {lower_upper[x]} Trigram is: {answer[x]}")

  elif lower_trigram == K_UN or upper_trigram == K_UN:
      answer.append("K'un")
      print(f"Your {lower_upper[x]} Trigram is: {answer[x]}")

  elif lower_trigram == SUN or upper_trigram == SUN:
      answer.append("Sun")
      print(f"Your {lower_upper[x]} Trigram is: {answer[x]}")

  elif lower_trigram == LI or upper_trigram == LI:
      answer.append("Li")
      print(f"Your {lower_upper[x]} Trigram is: {answer[x]}")

  elif lower_trigram == TUI or upper_trigram == TUI:
      answer.append("Tui")
      print(f"Your {lower_upper[x]} Trigram is: {answer[x]}")

  print()
  return answer


# At the end of the coin toss we have a bridge, we either go back around or continue depending if we've made the six lines or not
def prompt(x):

  if x == 0:
      print("You're half way through, now lets make your Upper Trigram")
      print()
  if x == 1:
      input("Press [Enter/Return] to reveal your HEXAGRAM")
      os.system('cls||clear')


def hexagrams(answer, is_this_a_changing_hexagram, lower_trigram, upper_trigram, dotted_lower_trigram, dotted_upper_trigram, user_question, lower_trigram2, upper_trigram2, display_changing_hexagrams_low, display_changing_hexagrams_high):

  # If there are no dots then its a static hexagram
  if is_this_a_changing_hexagram == 0:        
      print("YOUR HEXAGRAM:")
      print() 
      time.sleep(0.5)
      print(f"{dotted_upper_trigram}")                    # notice that 'dotted' is for display...
      time.sleep(0.5)
      print(f"{dotted_lower_trigram}")
      print() 
      time.sleep(0.5)
      print(f"YOUR QUESTION: {user_question}")
      print()
      time.sleep(0.5)
      hexagram_directory(upper_trigram, lower_trigram)    # ... but for id purposes its the undotted version. This dives deep into the 64 different hexagrams and matches the trigrams.
      print() 

  # This runs when dots are present!
  if is_this_a_changing_hexagram > 0:
      print("YOUR HEXAGRAMS:")
      print() 
      time.sleep(0.5)
      print(f"{display_changing_hexagrams_high}")         # this neatly displays to the user how the hexagrams have changed  
      time.sleep(0.5)
      print(f"{display_changing_hexagrams_low}")
      print() 
      time.sleep(0.5)
      print(f"YOUR QUESTION: {user_question}")
      print()
      time.sleep(0.5)
      hexagram_directory(upper_trigram, lower_trigram)
      print() 
      time.sleep(0.5)
      print("Changing to:")
      print() 
      time.sleep(0.5)
      hexagram2(lower_trigram2, upper_trigram2)           # again, note how these trigrams are their own unique variable that we created earlier.


def hexagram2(lower_trigram2, upper_trigram2):

      upper_trigram = upper_trigram2                      # they have already have their dots stripped, so we can simply rename them to names the directory will read
      lower_trigram = lower_trigram2

      hexagram_directory(upper_trigram, lower_trigram)    # and now the second hexagram is id'd


def hexagram_directory(upper_trigram, lower_trigram):

  # Moment of truth, we combine the two TRIGRAMS to find our HEXAGRAM
  if upper_trigram + lower_trigram == HEXAGRAM1:
      print("HEXAGRAM #1: Creative Power / The Creative")
      print("Simple translation: https://divination.com/iching/lookup/1-2/")
      print("In-depth translation: http://www2.unipr.it/~deyoung/I_Ching_Wilhelm_Translation.html#1")

  elif upper_trigram + lower_trigram == HEXAGRAM2:
      print("HEXAGRAM #2: Natural Response / The Receptive")
      print("Simple translation: https://divination.com/iching/lookup/2-2/")
      print("In-depth translation: http://www2.unipr.it/~deyoung/I_Ching_Wilhelm_Translation.html#2")

  elif upper_trigram + lower_trigram == HEXAGRAM3:
      print("HEXAGRAM #3: Difficult Beginnings")
      print("Simple translation: https://divination.com/iching/lookup/3-2/")
      print("In-depth translation: http://www2.unipr.it/~deyoung/I_Ching_Wilhelm_Translation.html#3")

  elif upper_trigram + lower_trigram == HEXAGRAM4:
      print("HEXAGRAM #4: Inexperience / Youthful Folly")
      print("Simple translation: https://divination.com/iching/lookup/4-2/")
      print("In-depth translation: http://www2.unipr.it/~deyoung/I_Ching_Wilhelm_Translation.html#4")

  elif upper_trigram + lower_trigram == HEXAGRAM5:
      print("HEXAGRAM #5: Calculated Waiting")
      print("Simple translation: https://divination.com/iching/lookup/5-2/")
      print("In-depth translation: http://www2.unipr.it/~deyoung/I_Ching_Wilhelm_Translation.html#5")

  elif upper_trigram + lower_trigram == HEXAGRAM6:
      print("HEXAGRAM #6: Conflict")
      print("Simple translation: https://divination.com/iching/lookup/6-2/")
      print("In-depth translation: http://www2.unipr.it/~deyoung/I_Ching_Wilhelm_Translation.html#6")

  elif upper_trigram + lower_trigram == HEXAGRAM7:
      print("HEXAGRAM #7: Collective Force / The Army")
      print("Simple translation: https://divination.com/iching/lookup/7-2/")
      print("In-depth translation: http://www2.unipr.it/~deyoung/I_Ching_Wilhelm_Translation.html#7")

  elif upper_trigram + lower_trigram == HEXAGRAM8:
      print("HEXAGRAM #8: Unity / Holding Together")
      print("Simple translation: https://divination.com/iching/lookup/8-2/")
      print("In-depth translation: http://www2.unipr.it/~deyoung/I_Ching_Wilhelm_Translation.html#8")

  elif upper_trigram + lower_trigram == HEXAGRAM9:
      print("HEXAGRAM #9: Restrained / The Taming Power of the Small")
      print("Simple translation: https://divination.com/iching/lookup/9-2/")
      print("In-depth translation: http://www2.unipr.it/~deyoung/I_Ching_Wilhelm_Translation.html#9")

  elif upper_trigram + lower_trigram == HEXAGRAM10:
      print("HEXAGRAM #10: Conduct")
      print("Simple translation: https://divination.com/iching/lookup/10-2/")
      print("In-depth translation: http://www2.unipr.it/~deyoung/I_Ching_Wilhelm_Translation.html#10")

  elif upper_trigram + lower_trigram == HEXAGRAM11:
      print("HEXAGRAM #11: Prospering / Peace")
      print("Simple translation: https://divination.com/iching/lookup/11-2/")
      print("In-depth translation: http://www2.unipr.it/~deyoung/I_Ching_Wilhelm_Translation.html#11")

  elif upper_trigram + lower_trigram == HEXAGRAM12:
      print("HEXAGRAM #12: Stagnation")
      print("Simple translation: https://divination.com/iching/lookup/12-2/")
      print("In-depth translation: http://www2.unipr.it/~deyoung/I_Ching_Wilhelm_Translation.html#12")

  elif upper_trigram + lower_trigram == HEXAGRAM13:
      print("HEXAGRAM #13: Community / Fellowship With Men")
      print("Simple translation: https://divination.com/iching/lookup/13-2/")
      print("In-depth translation: http://www2.unipr.it/~deyoung/I_Ching_Wilhelm_Translation.html#13")

  elif upper_trigram + lower_trigram == HEXAGRAM14:
      print("HEXAGRAM #14: Sovereignty / Possession in Great Measure")
      print("Simple translation: https://divination.com/iching/lookup/14-2/")
      print("In-depth translation: http://www2.unipr.it/~deyoung/I_Ching_Wilhelm_Translation.html#14")

  elif upper_trigram + lower_trigram == HEXAGRAM15:
      print("HEXAGRAM #15: Moderation / Modesty")
      print("Simple translation: https://divination.com/iching/lookup/15-2/")
      print("In-depth translation: http://www2.unipr.it/~deyoung/I_Ching_Wilhelm_Translation.html#15")

  elif upper_trigram + lower_trigram == HEXAGRAM16:
      print("HEXAGRAM #16: Harmonize / Enthusiasm")
      print("Simple translation: https://divination.com/iching/lookup/16-2/")
      print("In-depth translation: http://www2.unipr.it/~deyoung/I_Ching_Wilhelm_Translation.html#16")

  elif upper_trigram + lower_trigram == HEXAGRAM17:
      print("HEXAGRAM #17: Adapting / Following")
      print("Simple translation: https://divination.com/iching/lookup/17-2/")
      print("In-depth translation: http://www2.unipr.it/~deyoung/I_Ching_Wilhelm_Translation.html#17")

  elif upper_trigram + lower_trigram == HEXAGRAM18:
      print("HEXAGRAM #18: Repair / Decay")
      print("Simple translation: https://divination.com/iching/lookup/18-2/")
      print("In-depth translation: http://www2.unipr.it/~deyoung/I_Ching_Wilhelm_Translation.html#18")

  elif upper_trigram + lower_trigram == HEXAGRAM19:
      print("HEXAGRAM #19: Promotion / Approach")
      print("Simple translation: https://divination.com/iching/lookup/19-2/")
      print("In-depth translation: http://www2.unipr.it/~deyoung/I_Ching_Wilhelm_Translation.html#19")

  elif upper_trigram + lower_trigram == HEXAGRAM20:
      print("HEXAGRAM #20: Contemplating")
      print("Simple translation: https://divination.com/iching/lookup/20-2/")
      print("In-depth translation: http://www2.unipr.it/~deyoung/I_Ching_Wilhelm_Translation.html#20")

  elif upper_trigram + lower_trigram == HEXAGRAM21:
      print("HEXAGRAM #21: Reform / Biting Through")
      print("Simple translation: https://divination.com/iching/lookup/21-2/")
      print("In-depth translation: http://www2.unipr.it/~deyoung/I_Ching_Wilhelm_Translation.html#21")

  elif upper_trigram + lower_trigram == HEXAGRAM22:
      print("HEXAGRAM #22: Grace")
      print("Simple translation: https://divination.com/iching/lookup/22-2/")
      print("In-depth translation: http://www2.unipr.it/~deyoung/I_Ching_Wilhelm_Translation.html#22")

  elif upper_trigram + lower_trigram == HEXAGRAM23:
      print("HEXAGRAM #23: Deterioration / Splitting Apart")
      print("Simple translation: https://divination.com/iching/lookup/23-2/")
      print("In-depth translation: http://www2.unipr.it/~deyoung/I_Ching_Wilhelm_Translation.html#23")

  elif upper_trigram + lower_trigram == HEXAGRAM24:
      print("HEXAGRAM #24: Returning")
      print("Simple translation: https://divination.com/iching/lookup/24-2/")
      print("In-depth translation: http://www2.unipr.it/~deyoung/I_Ching_Wilhelm_Translation.html#24")

  elif upper_trigram + lower_trigram == HEXAGRAM25:
      print("HEXAGRAM #25: Innocence")
      print("Simple translation: https://divination.com/iching/lookup/25-2/")
      print("In-depth translation: http://www2.unipr.it/~deyoung/I_Ching_Wilhelm_Translation.html#25")

  elif upper_trigram + lower_trigram == HEXAGRAM26:
      print("HEXAGRAM #26: Potential Energy / The Taming of the Great")
      print("Simple translation: https://divination.com/iching/lookup/26-2/")
      print("In-depth translation: http://www2.unipr.it/~deyoung/I_Ching_Wilhelm_Translation.html#26")

  elif upper_trigram + lower_trigram == HEXAGRAM27:
      print("HEXAGRAM #27: Nourishing")
      print("Simple translation: https://divination.com/iching/lookup/27-2/")
      print("In-depth translation: http://www2.unipr.it/~deyoung/I_Ching_Wilhelm_Translation.html#27")

  elif upper_trigram + lower_trigram == HEXAGRAM28:
      print("HEXAGRAM #28: Critical Mass / Preponderance of the Great")
      print("Simple translation: https://divination.com/iching/lookup/28-2/")
      print("In-depth translation: http://www2.unipr.it/~deyoung/I_Ching_Wilhelm_Translation.html#28")

  elif upper_trigram + lower_trigram == HEXAGRAM29:
      print("HEXAGRAM #29: Danger")
      print("Simple translation: https://divination.com/iching/lookup/29-2/")
      print("In-depth translation: http://www2.unipr.it/~deyoung/I_Ching_Wilhelm_Translation.html#29")

  elif upper_trigram + lower_trigram == HEXAGRAM30:
      print("HEXAGRAM #30: Synergy / The Clinging")
      print("Simple translation: https://divination.com/iching/lookup/30-2/")
      print("In-depth translation: http://www2.unipr.it/~deyoung/I_Ching_Wilhelm_Translation.html#30")

  elif upper_trigram + lower_trigram == HEXAGRAM31:
      print("HEXAGRAM #31: Attraction")
      print("Simple translation: https://divination.com/iching/lookup/31-2/")
      print("In-depth translation: http://www2.unipr.it/~deyoung/I_Ching_Wilhelm_Translation.html#31")

  elif upper_trigram + lower_trigram == HEXAGRAM32:
      print("HEXAGRAM #32: Continuing / Enduring")
      print("Simple translation: https://divination.com/iching/lookup/32-2/")
      print("In-depth translation: http://www2.unipr.it/~deyoung/I_Ching_Wilhelm_Translation.html#32")

  elif upper_trigram + lower_trigram == HEXAGRAM33:
      print("HEXAGRAM #33: Retreat")
      print("Simple translation: https://divination.com/iching/lookup/33-2/")
      print("In-depth translation: http://www2.unipr.it/~deyoung/I_Ching_Wilhelm_Translation.html#33")

  elif upper_trigram + lower_trigram == HEXAGRAM34:
      print("HEXAGRAM #34: Great Power")
      print("Simple translation: https://divination.com/iching/lookup/34-2/")
      print("In-depth translation: http://www2.unipr.it/~deyoung/I_Ching_Wilhelm_Translation.html#34")

  elif upper_trigram + lower_trigram == HEXAGRAM35:
      print("HEXAGRAM #35: Progress")
      print("Simple translation: https://divination.com/iching/lookup/35-2/")
      print("In-depth translation: http://www2.unipr.it/~deyoung/I_Ching_Wilhelm_Translation.html#35")

  elif upper_trigram + lower_trigram == HEXAGRAM36:
      print("HEXAGRAM #36: Censorship / Darkening of the Light")
      print("Simple translation: https://divination.com/iching/lookup/36-2/")
      print("In-depth translation: http://www2.unipr.it/~deyoung/I_Ching_Wilhelm_Translation.html#36")

  elif upper_trigram + lower_trigram == HEXAGRAM37:
      print("HEXAGRAM #37: Family")
      print("Simple translation: https://divination.com/iching/lookup/37-2/")
      print("In-depth translation: http://www2.unipr.it/~deyoung/I_Ching_Wilhelm_Translation.html#37")

  elif upper_trigram + lower_trigram == HEXAGRAM38:
      print("HEXAGRAM #38: Contradiction / Opposition")
      print("Simple translation: https://divination.com/iching/lookup/38-2/")
      print("In-depth translation: http://www2.unipr.it/~deyoung/I_Ching_Wilhelm_Translation.html#38")

  elif upper_trigram + lower_trigram == HEXAGRAM39:
      print("HEXAGRAM #39: Obstacles")
      print("Simple translation: https://divination.com/iching/lookup/39-2/")
      print("In-depth translation: http://www2.unipr.it/~deyoung/I_Ching_Wilhelm_Translation.html#39")

  elif upper_trigram + lower_trigram == HEXAGRAM40:
      print("HEXAGRAM #40: Liberation / Deliverance")
      print("Simple translation: https://divination.com/iching/lookup/40-2/")
      print("In-depth translation: http://www2.unipr.it/~deyoung/I_Ching_Wilhelm_Translation.html#40")

  elif upper_trigram + lower_trigram == HEXAGRAM41:
      print("HEXAGRAM #41: Decline / Decrease")
      print("Simple translation: https://divination.com/iching/lookup/41-2/")
      print("In-depth translation: http://www2.unipr.it/~deyoung/I_Ching_Wilhelm_Translation.html#41")

  elif upper_trigram + lower_trigram == HEXAGRAM42:
      print("HEXAGRAM #42: Benefit / Increase")
      print("Simple translation: https://divination.com/iching/lookup/42-2/")
      print("In-depth translation: http://www2.unipr.it/~deyoung/I_Ching_Wilhelm_Translation.html#42")

  elif upper_trigram + lower_trigram == HEXAGRAM43:
      print("HEXAGRAM #43: Resolution")
      print("Simple translation: https://divination.com/iching/lookup/43-2/")
      print("In-depth translation: http://www2.unipr.it/~deyoung/I_Ching_Wilhelm_Translation.html#43")

  elif upper_trigram + lower_trigram == HEXAGRAM44:
      print("HEXAGRAM #44: Temptation / Coming to Meet")
      print("Simple translation: https://divination.com/iching/lookup/44-2/")
      print("In-depth translation: http://www2.unipr.it/~deyoung/I_Ching_Wilhelm_Translation.html#44")

  elif upper_trigram + lower_trigram == HEXAGRAM45:
      print("HEXAGRAM #45: Assembling")
      print("Simple translation: https://divination.com/iching/lookup/45-2/")
      print("In-depth translation: http://www2.unipr.it/~deyoung/I_Ching_Wilhelm_Translation.html#45")

  elif upper_trigram + lower_trigram == HEXAGRAM46:
      print("HEXAGRAM #46: Advancement / Pushing Upward")
      print("Simple translation: https://divination.com/iching/lookup/46-2/")
      print("In-depth translation: http://www2.unipr.it/~deyoung/I_Ching_Wilhelm_Translation.html#46")

  elif upper_trigram + lower_trigram == HEXAGRAM47:
      print("HEXAGRAM #47: Adversity")
      print("Simple translation: https://divination.com/iching/lookup/47-2/")
      print("In-depth translation: http://www2.unipr.it/~deyoung/I_Ching_Wilhelm_Translation.html#47")

  elif upper_trigram + lower_trigram == HEXAGRAM48:
      print("HEXAGRAM #48: The Source / The Well")
      print("Simple translation: https://divination.com/iching/lookup/48-2/")
      print("In-depth translation: http://www2.unipr.it/~deyoung/I_Ching_Wilhelm_Translation.html#48")

  elif upper_trigram + lower_trigram == HEXAGRAM49:
      print("HEXAGRAM #49: Changing / Revolution")
      print("Simple translation: https://divination.com/iching/lookup/49-2/")
      print("In-depth translation: http://www2.unipr.it/~deyoung/I_Ching_Wilhelm_Translation.html#49")

  elif upper_trigram + lower_trigram == HEXAGRAM50:
      print("HEXAGRAM #50: Cosmic Order / The Cauldron")
      print("Simple translation: https://divination.com/iching/lookup/50-2/")
      print("In-depth translation: http://www2.unipr.it/~deyoung/I_Ching_Wilhelm_Translation.html#50")

  elif upper_trigram + lower_trigram == HEXAGRAM51:
      print("HEXAGRAM #51: Shocking")
      print("Simple translation: https://divination.com/iching/lookup/51-2/")
      print("In-depth translation: http://www2.unipr.it/~deyoung/I_Ching_Wilhelm_Translation.html#51")

  elif upper_trigram + lower_trigram == HEXAGRAM52:
      print("HEXAGRAM #52: Meditation / Keeping still")
      print("Simple translation: https://divination.com/iching/lookup/52-2/")
      print("In-depth translation: http://www2.unipr.it/~deyoung/I_Ching_Wilhelm_Translation.html#52")

  elif upper_trigram + lower_trigram == HEXAGRAM53:
      print("HEXAGRAM #53: Developing")
      print("Simple translation: https://divination.com/iching/lookup/53-2/")
      print("In-depth translation: http://www2.unipr.it/~deyoung/I_Ching_Wilhelm_Translation.html#53")

  elif upper_trigram + lower_trigram == HEXAGRAM54:
      print("HEXAGRAM #54: Subordinate / The Marrying Maiden")
      print("Simple translation: https://divination.com/iching/lookup/54-2/")
      print("In-depth translation: http://www2.unipr.it/~deyoung/I_Ching_Wilhelm_Translation.html#54")

  elif upper_trigram + lower_trigram == HEXAGRAM55:
      print("HEXAGRAM #55: Zenith / Abundance")
      print("Simple translation: https://divination.com/iching/lookup/55-2/")
      print("In-depth translation: http://www2.unipr.it/~deyoung/I_Ching_Wilhelm_Translation.html#55")

  elif upper_trigram + lower_trigram == HEXAGRAM56:
      print("HEXAGRAM #56: Traveling")
      print("Simple translation: https://divination.com/iching/lookup/56-2/")
      print("In-depth translation: http://www2.unipr.it/~deyoung/I_Ching_Wilhelm_Translation.html#56")

  elif upper_trigram + lower_trigram == HEXAGRAM57:
      print("HEXAGRAM #57: Penetrating Influence / The Gentle")
      print("Simple translation: https://divination.com/iching/lookup/57-2/")
      print("In-depth translation: http://www2.unipr.it/~deyoung/I_Ching_Wilhelm_Translation.html#57")

  elif upper_trigram + lower_trigram == HEXAGRAM58:
      print("HEXAGRAM #58: Encouraging / Joy")
      print("Simple translation: https://divination.com/iching/lookup/58-2/")
      print("In-depth translation: http://www2.unipr.it/~deyoung/I_Ching_Wilhelm_Translation.html#58")

  elif upper_trigram + lower_trigram == HEXAGRAM59:
      print("HEXAGRAM #59: Reuniting / Dispersion")
      print("Simple translation: https://divination.com/iching/lookup/59-2/")
      print("In-depth translation: http://www2.unipr.it/~deyoung/I_Ching_Wilhelm_Translation.html#59")

  elif upper_trigram + lower_trigram == HEXAGRAM60:
      print("HEXAGRAM #60: Limitations")
      print("Simple translation: https://divination.com/iching/lookup/60-2/")
      print("In-depth translation: http://www2.unipr.it/~deyoung/I_Ching_Wilhelm_Translation.html#60")

  elif upper_trigram + lower_trigram == HEXAGRAM61:
      print("HEXAGRAM #61: Insight / Inner Truth")
      print("Simple translation: https://divination.com/iching/lookup/61-2/")
      print("In-depth translation: http://www2.unipr.it/~deyoung/I_Ching_Wilhelm_Translation.html#61")

  elif upper_trigram + lower_trigram == HEXAGRAM62:
      print("HEXAGRAM #62: Conscientiousness / Preponderance of the Small")
      print("Simple translation: https://divination.com/iching/lookup/62-2/")
      print("In-depth translation: http://www2.unipr.it/~deyoung/I_Ching_Wilhelm_Translation.html#62")

  elif upper_trigram + lower_trigram == HEXAGRAM63:
      print("HEXAGRAM #63: After the End")
      print("Simple translation: https://divination.com/iching/lookup/63-2/")
      print("In-depth translation: http://www2.unipr.it/~deyoung/I_Ching_Wilhelm_Translation.html#63")

  elif upper_trigram + lower_trigram == HEXAGRAM64:
      print("HEXAGRAM #64: Before the End")
      print("Simple translation: https://divination.com/iching/lookup/64-2/")
      print("In-depth translation: http://www2.unipr.it/~deyoung/I_Ching_Wilhelm_Translation.html#64")

def final_message():
  print()
  print("Further resources:")
  print("The I Ching Workbook by R.L.Wing:")
  print("https://www.amazon.co.uk/I-Ching-Workbook-Wing/dp/038512838X")


#MAIN PROGRAM
title_screen()
user_question = learn_or_question()
create_hexagrams(user_question)
final_message()

