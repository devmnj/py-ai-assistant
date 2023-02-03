from ai import AI
import pyjokes

alf = AI();

def joke():
  funny = pyjokes.get_joke()
  print(funny)
  alf.say(funny)

command = ""
while True and command!="goodbye": 
  command = alf.listen()
  print("command was:", command)

  if command == "tell me a joke":
    joke()

alf.say("Goodbye, I'am to sleep")