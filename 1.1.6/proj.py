answer=input("How are you feeling today: good, bad, or a bit of both?")
if(answer =="good"):
  print("That's great, hope you have a great day!")

elif(answer == "bad"):
  print("Oh that's bad, hope it gets better though!")

elif(answer == "a bit of both"):
  print("I guess that is kind of good, hope you are ok.")

else:
  print("Ok.")

print("you are feeling",answer, "maybe it is because of the amount of time you have been in school.")

time=int(input("How much time have you been in school for today?: much, a_little, or none"))
if(time >= 8):
  print("That is a lot of time, you still have", 24-time,"hours of the day to do something.")

elif(time >= 4):
  print("That is not that much time, you still have", 24-time, "hours left to do something today.")

elif(time == 0):
  print("You have not done anything")