'''
  Building the car game ::
  CAR GAME:
        > help
          start - to start the car
          stop - to stop the car
          quit - to exit
        > asd
          I don't understand this
        > start
          Car started... Ready to go!!
          >start
           Car had already started!!
        > stop
          Car stopped..
          >stop
           Car had already stopped!!
        > quit
'''
command = "  "
started = False
#while command != "quit"
while True:
    command = input("> ").lower()
    if command == "start":
        if started:
          print("Car has already started!!")
        else:
         started = True
         print("Car started...Ready to go!!")
    elif command == "stop":
        if not started:
            print("Car is already stopped!!")
        else:
            started = False
            print("Car stopped..")
    elif command == "help":
         print("""
start - to start the car
stop - to stop the car
quit - to exit
""")
    elif command == "quit":
      break

    else:
     print("I donot understand this")






