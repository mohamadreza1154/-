import random
def  Hangman(counter ):
  if counter == 1:
       print(""" 

      _______
     |/      |
     |      (_)
     |      
     |       
     |      
     |
    _|___""") 
  elif  counter == 2:
       print(""" 

       _______
     |/      |
     |      (_)
     |      \|/
     |       
     |      
     |
    _|___""")
  elif counter == 3:
       print(""" 

           _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |      
     |
    _|___""")
  elif  counter ==4:
      print("""
   |_______________``\
    [/]           [  ]
    [\]           | ||
    [/]           |  |
    [\]           |  |
    [/]           || |
   [---]          |  |
   [---]          |@ |
   [---]          |  |
  oOOOOOo         |  |
 oOO___OOo        | @|
oO/|||||\Oo       |  |
OO/|||||\OOo      |  |
*O\ x x /OO*      |  |
/*|  c  |O*\      |  |
   \_O_/    \     |  |
    \#/     |     |  |
 |       |  |     | ||
 |       |  |_____| ||__
_/_______\__|  \  ||||  \
/         \_|\  _ | ||\  \
|    V    |\  \//\  \  \  \
|    |    | __//  \  \  \  \
|    |    |\|//|\  \  \  \  \
------------\--- \  \  \  \  \
\  \  \  \  \  \  \  \  \  \  \
_\__\__\__\__\__\__\__\__\__\__\
__|__|__|__|__|__|__|__|__|__|__|
|___| |___|
|###/ \###|
\##/   \##/
 ``     `` """)  
hang =0           
word_list = ["mouse", "banana", "letter"];
word = random.choice(word_list)
count_word =len(word)
array = ["_"] * len(word)
for i in range(1,count_word+4):
    answer =input("please gass the answer\n ")
    if  answer in word:
        for j in range(1 , count_word+1):
                if answer==word[j-1] :
                   array[j-1]=word[j-1]
        for ch in array:
             print( ch, end = "")
        print("\n")
        if  "_"  not in array :
             print("you win")
             break   
    else:
            hang+=1
            Hangman(hang)
            if hang ==4:
                print ("game over ")
                
