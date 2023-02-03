import speech_recognition as sr
import pyttsx3
import pyjokes

class AI():
  __name=""
  __skill=[]

  def __init__(self,name=None):
    self.engine = pyttsx3.init()
    self.r= sr.Recognizer()
    self.m = sr.Microphone()

    if name is not None:
      self.__name = name

    print("Listening")
    with self.m as source:
      self.r.adjust_for_ambient_noise(source)

  @property
  def name(self):
    return self.__name
    
  @name.setter
  def name(self,value):
    sentence= "Hellow, my name is" + self.__name
    self.__name=value
    self.engine.say(sentence)
    self.engine.runAndWait()
  
  def say(self,sentence):
    self.engine.say(sentence)
    self.engine.runAndWait()

  def listen(self):
    print("Say something")
    with self.m as source:
      audio=self.r.listen(source)
    print("got it")
    try:
      phrase= self.r.recognize_google(audio,show_all=False,language="eng-us")
      sentence="Got it, you said " + phrase
      self.engine.say(sentence)
      self.engine.runAndWait() 
      return phrase
    except sr.RequestError:  
      print("API was unreachable")
    except sr.UnknownValueError:
      print("sorry, didn't catch that")
      self.engine.say("Sorry didn't catch that")
      self.engine.runAndWait() 
    # print("You said",phrase)
    

