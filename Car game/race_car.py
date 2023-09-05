choices = ("start", "stop", "quit")

started = False
stopped = False

while True:
    button = input(">").lower()
    if button == ("start"):
        if started:
            print("The car is already started")
        else:
            started = True
            print("Car started...Ready to go!")
    elif button == ("stop"):
        if not started:
            print("The car is not started yet. You can't stop it")
        elif stopped:
            print("The car is already stopped")
        else:
            stopped = True
            print("Car stopped.")
    elif button == ("quit"):
        break
    elif button == "help":
        print("""
start - to start the car 
stop - to stop the car 
quit - to quit
              """)
    elif button != choices:
        print("I don't understand that.")
