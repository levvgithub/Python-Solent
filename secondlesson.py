print ("How many cables should I remove?")
cable1 = int(input())
i = 0
cablemsg = "Remove cable."
while i < cable1:
  print(cablemsg)
  i += 1

print ("Enter an activity")
activity = str(input())
if activity == "calculate":
  print("Performing calculations...")
  print("Activity completed!")
else:
  print("Performing activity...")
  print("Activity completed!")

print("How far are we from the cave?")
distance = int(input())
for x in range (0, distance+1):
  print(f"{7-x} steps remaining")
print("We have reached the cave!")