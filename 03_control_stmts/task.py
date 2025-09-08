original_pin = 6670
entered_pin = 0


for attempts in range(4):
    user_entered_pin = int(input("enter pin"))
    if user_entered_pin != original_pin:
      print("Maximum Attempts Reached  -  Try after 24 Hours") 

    else:
      print("Transaction Success")
      break


