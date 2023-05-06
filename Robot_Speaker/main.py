# import pyttsx3
# if __name__ == '__main__':
#    command = pyttsx3.init()
#    print("This is a AI based Speaker created by Subhendu Goutam")
#    while(True):
#       x=input("Enter what you want me to speak: ")
#       if x=="end":
#          command.say("Sayonara Sir")
#          command.runAndWait()
#          break
#       command.say(x)
#       command.runAndWait()
#OR
import win32com.client as wincom
if __name__=='__main__':
   speak = wincom.Dispatch("SAPI.SpVoice")
   print("This is an AI based speaker which convert your texts to speach and it is created by Subhendu Goutam")
   while(True):
      command=input("Enter what you want me to speak: ")
      if command=="quit":
         speak.Speak("Sayonara")
         break
      speak.Speak(command)