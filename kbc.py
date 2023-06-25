#kbc game by neeraj deshmukh
print("Namashkaar bahiyo aur behno , swagat hai apka is khel mein , mai hu Neeraj Deshmukh, chaliye shuru karte hai 'Kaun Banega Crorepati'")
print("Let's play!!")
a=(input(" Please Enter your good name: "))
print("Toh humare contestant ka naam hai",a)
print(a,"Aapka bohut bohut swagat hai Kaun Banega Crorepati mein")
print("Toh jaise ki aap jaante hai",a,"ki is game mein 3 padaaw hai")
print("Pehla padaaw hai 10,000 rupayo pe")
print("Dusra padaaw hai 3,20,000 rupayo pe")
print("Aur teesra padaaw hai 1,00,00,000 rupayo pe")
print("Chaliye bina kisi deri ke shuru karte hai Kaun Banega Crorepati")
print("let's play!!")
questions = [
  [
    "The International Literacy Day is observed on?", "Nov 28", "May 2", "Sep 22",
    "Sep 8", "", 4
  ],
  [
    "The language of Lakshadweep. a Union Territory of India, is?", "Tamil", "Hindi", "Telugu","Malayalam","", 4
  ],
  [
    "In which group of places the Kumbha Mela is held every twelve years?", "Ujjain. Purl; Prayag. Haridwar", "Rameshwaram. Purl, Badrinath. Dwarika", "Chittakoot, Ujjain, Prayag,'Haridwar",
    "Prayag. Haridwar, Ujjain,. Nasik", "", 4
  ],
  [
    "Bahubali festival is related to?", "Islam", "Hinduism", "Buddhism",
    "Jainism", "", 4
  ],
  [
    "Which day is observed as the World Standards  Day?", "June 26", "Nov 15", "Dec 2",
    "Oct 14", "", 4
  ],
  [
    " Which of the following was the theme of the World Red Cross and Red Crescent Day?", "Dignity for all - focus on women", "Focus on health for all", "Nourishment for all-focus on children",
    "Dignity for all - focus on Children", "", 4
  ],
  [
    "September 27 is celebrated every year as?", "Teachers' Day", "National Integration Day", "International Literacy Day",
    "World Tourism Day", "", 4
  ],
  [
    "Who is the author of 'Manas Ka-Hans'?", "Khushwant Singh", "Prem Chand", "Jayashankar Prasad",
    "Amrit Lal Nagar", "", 4
  ],
  [
    " The death anniversary of which of the following leaders is observed as Martyrs' Day?", "Smt. Indira Gandhi", "PI. Jawaharlal Nehru", "Lal Bahadur Shastri",
    "Mahatma Gandhi", "", 4
  ],
  [
    " Who is the author of the epic 'Meghdoot'?", "Vishakadatta", "Valmiki", "Banabhatta",
    "Kalidas", "", 4
  ],
  [
    "'Good Friday' is observed to commemorate the event of?", "birth of Jesus Christ", "birth of' St. Peter", "rebirth of Jesus Christ",
    "crucification 'of Jesus Christ", "", 4
  ],
  [
    " Who is the author of the book 'Amrit Ki Ore?", "Mukesh Kumar", "Upendra Nath", "Nirad C. Choudhary",
    "Narendra Mohan", "", 4
  ],
  [
    "Which of the following is observed as Sports Day every year?", "22nd April", "26th  july", "2nd October",
    "29th August", "", 4
  ],
  [
    "World Health Day is observed on?", "Apr 28", "Mar 6 ", "May 15",
    "Apr 7", "", 4
  ],
  [
    "Pongal is a popular festival of which state?", "Karnataka", "Kerala", "Andhra Pradesh",
    "Tamil Nadu", "", 4
  ],
    
 
]

levels = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000,640000,1250000,2500000,5000000,10000000]
money = 0
for i in range(0, len(questions)):
  
  question = questions[i]
  print(f"\n\nQuestion for Rs. {levels[i]}")
  print(f"a. {question[1]}          b. {question[2]} ")
  print(f"c. {question[3]}          d. {question[4]} ")
  reply = int(input("Enter your answer (1-4) or  0 to quit:\n" ))
  if (reply == 0):
    money = levels[i-1]
    break
  if(reply == question[-1]):
    print(f"\n\nCorrect answer, you have won Rs. {levels[i]}")
    if(i == 4):
      money = 10000
    elif(i == 9):
      money = 320000
    elif(i == 14):
      money = 10000000
  else:
    print("\nWrong answer!")
    break 

print(f"total money won is {money}")
    
    
