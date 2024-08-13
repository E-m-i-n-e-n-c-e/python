list=[["2+2:\n","4"],["5*2:\n","10"],["3+3:\n","6"],["4*4:\n","16"],["5*5:\n","25"],["What is the capital of France:\n","Paris"]]
score=0
for i in list:
  print(i[0])
  ans=(input("Enter your answer: "))
  if ans==i[1]:
    print("\nCorrect")
    score=score+1
    print("You gain 1 point")
    print("Your score is:",score,"\n")
  else:
    print("\nIncorrect")
    score=score-1
    print("You lose one point")
    print("Your score is:",score,"\n")
print("\nyour total score is",score)
print("You win 10*"+str(score)+"="+str(10*score)+"$")
print("Thank you for playing")