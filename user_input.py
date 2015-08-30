text=''
while text != "quit":
  text = input("Enter a number (or quit to exit): ")
  if text == "quit":
    print ("exiting program")
  elif text == "H20":
    print("Water")
  elif text == "CH4":
    print("Methane")
  else:
    print("Unknown compound")
