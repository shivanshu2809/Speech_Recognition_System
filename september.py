import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import cv2
import random
from twilio.rest import Client
from selenium import webdriver 
from time import sleep




engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)




#def engine.say(audio):
 #   engine.say(audio)
 #   engine.runAndWait()

#engine.say('please first scan your face....')
#face_cascade=cv2.CascadeClassifier("C:\\Users\\DELL\\Desktop\\Excelr Hyd\\Facial-Expression-Detection-master\\haarcascade_frontalface_alt.xml")
#cap= cv2.VideoCapture(0)

#while True:
#    ret, frame=cap.read()
#    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
 #   faces=face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)
  #  for (x,y,w,h) in faces:
   #     print(x,y,w,h)

 #   cv2.imshow('Frame',frame)
#
  #  if cv2.waitKey(5) & 0xFF ==ord('q'):
   #     break

#cap.release()
#cv2.destroyAllWindows()


account_sid = 'ACe6abd18a0969e644b86508f151af093c'
auth_token = '7bdeb8630512b84fb854a2b16753d240'
client = Client(account_sid, auth_token)

from_whatsapp_number='whatsapp:+14155238886'
to_whatsapp_number='whatsapp:+918109422973'
otprandom=random.randint(1000,9999)
message = client.messages.create(
                     body="Your Login OTP is : "+str(otprandom),
                     from_=from_whatsapp_number,
                     to=to_whatsapp_number
                 )
print(otprandom)
#print(message.sid)

engine.say('please first enter the login otp')
engine.runAndWait()
otpinp=int(input("Enter Login OTP : "))
if otpinp==otprandom:

    def wishMe():
        hour=int(datetime.datetime.now().hour)
        if hour>=0 and hour<12:
            engine.say('Good Morning Sir')
            engine.runAndWait()
            engine.stop()
        elif hour>=12 and hour<17:
            engine.say('Good Afternoon Sir')
            engine.runAndWait()
            engine.stop()

        else:
            engine.say('Good Evening Sir')
        engine.say('Please tell me how may I help you?')
        engine.runAndWait()
        engine.stop()
        return


    def takeCommand():
    
    
        r=sr.Recognizer()
        with sr.Microphone() as source:
            print('Listening...')
            r.pause_threshold=1
            r.energy_threshold=5000
            audio=r.listen(source)
        try:
            print('Recognizing...')
            query=r.recognize_google(audio)
            print(f'User Said : {query}\n')
        
        except Exception as e:
            #print('Say that again please...')
            #engine.say('Say that again please...')
            return "none"
        return query

    #listen=takeCommand().lower()

    if __name__ == "__main__":

    #if "hello september" in listen:
        
        while True:
            query=takeCommand().lower()
            br1="www."
            br2=".com"
            exp1='"'
            exp2='explorer "c:\\'
            exp3='explorer "d:\\'
            exp4='explorer "e:\\'
            exp5='explorer "g:\\'
            if "hello september" in query:
                wishMe()

        ## NORMAL FUNCTIONS
        #  

        
            elif 'wikipedia' in query:
                engine.say('Searching Wikipedia...')
                engine.runAndWait()
                query=query.replace('wikipedia',"")
                results=wikipedia.summary(query,sentences=2)
                print(results)
                engine.say('According to wikipedia...')
                engine.say(results)
                engine.runAndWait()

            

            elif 'open my pc' in query:
                engine.say('opening sir!')
                os.system('cd..')
                os.system('cd..')
                os.system('explorer')

            elif 'open c drive' in query:
                engine.say('opening sir!')
                engine.runAndWait()
                os.system('cd..')
                os.system('cd..')
                os.system('explorer "c:"')

            elif 'open d drive' in query:
                engine.say('opening sir!')
                os.system('cd..')
                os.system('cd..')
                os.system('explorer "d:"')

            elif 'open e drive' in query:
                engine.say('opening sir!')
                engine.runAndWait()
                os.system('cd..')
                os.system('cd..')
                os.system('explorer "e:"')

            elif 'open g drive' in query:
                engine.say('opening sir!')
                engine.runAndWait()
                os.system('cd..')
                os.system('cd..')
                os.system('explorer "g:"')




            

            
            elif 'open youtube' in query:
                engine.say('opening sir!')
                engine.runAndWait()
                webbrowser.open('youtube.com')

            elif 'close youtube' in query:
                engine.say('closing sir!')
                engine.runAndWait()
                os.system('taskkill /im iexplore.exe')

            

            elif 'open google' in query:
                webbrowser.open('www.google.com')
                engine.say('opening sir!')

            elif 'close google' in query:
                engine.say('closing sir!')
                engine.runAndWait()
                os.system('taskkill /im iexplore.exe')

            elif 'close internet explorer' in query:
                engine.say('closing sir!')
                engine.runAndWait()
                os.system('taskkill /im iexplore.exe')

            elif 'close browser' in query:
                engine.say('which one sir!')
                

            elif 'play music' in query:
                random=np.random.randint(0,373)
                music_dir='G:\\Songs'
                songs=os.listdir(music_dir)
                os.startfile(os.path.join(music_dir,songs[random]))

            elif 'play bb ki vines' in query:
                random=np.random.randint(0,52)
                video_dir='G:\\Videos\\BB ki Vines'
                songs=os.listdir(video_dir)
                os.startfile(os.path.join(video_dir,songs[random]))

            elif 'close video' in query:
                engine.say('closing sir!')
                engine.runAndWait()
                os.system('taskkill /im wmplayer.exe')

            elif 'the time' in query:
                strTime=datetime.datetime.now().strftime('%H:%M:%S')
                engine.say("Sir! the time is : ")
                engine.say(strTime)
                engine.runAndWait()



            elif "open chrome" in query:
                chromepath="C:\\Program Files (x86)\\Google\Chrome\\Application\\chrome.exe"
                engine.say('opening sir!')
                os.startfile(chromepath)

            elif "open internet explorer" in query:
                iepath='C:\\Program Files (x86)\\Internet Explorer\\iexplore.exe'
                engine.say('opening sir!')
                engine.runAndWait()
                os.startfile(iepath)
                

            elif 'open mozilla firefox' in query:
                mfpath="C:\\Program Files (x86)\\Mozilla Firefox\\firefox.exe"
                engine.say('opening Sir!')
                engine.runAndWait()
                os.startfile(mfpath)

            elif 'close mozilla firefox' in query:
                engine.say('closing sir!')
                engine.runAndWait()
                os.system('taskkill /im firefox.exe')

            elif 'who are you' in query:
                engine.say('I am September, I am your friend, to follow your instructions')
                engine.runAndWait()

            elif 'open website' in query:
                engine.say('which website sir!')
                engine.runAndWait()
                engine.stop()
                c=takeCommand().lower()
                a=webbrowser.open(br1+c+br2)
                engine.say('opening sir!')
                engine.runAndWait()
                
            elif 'coronavirus details in india' in query:
                engine.say("Fetching Sir!")
                engine.runAndWait()
                engine.say("Please wait....")
                engine.runAndWait()
                sleep(2)
                a=webbrowser.open("www.covid19india.org")
                sleep(2)
                query=query.replace('wikipedia',"")
                results=wikipedia.summary("coronavirus india",sentences=3)
                print(results)
                engine.say(results)
                engine.runAndWait()
                
                
            elif 'open my instagram' in query:
                engine.say("Opening Sir!!!!")
                engine.runAndWait()
                driver=webdriver.Chrome("G:\\Software\\chromedriver")
                driver.get("https://www.instagram.com/?hl=en")
                sleep(3)
                engine.say("Please tell me your username and password sir!")
                engine.runAndWait()
                c=takeCommand().lower()
                if "know" in c:
                    engine.say("just kidding sir! please wait i am opening your account")
                    engine.runAndWait()
                    sleep(2)
                    driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[2]/div/label/input").send_keys("username")
                    driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[3]/div/label/input").send_keys("password")
                    sleep(2)
                    driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[4]/button').click()
                    sleep(3)
                    engine.say("Please tell me the code you received in your number")
                    engine.runAndWait()
                    c=takeCommand().lower()
                    engine.say(c)
                    engine.runAndWait()
                    engine.say("please confirm by saying yes,")
                    engine.runAndWait()
                    engine.say("if wrong say no!")
                    engine.runAndWait()
                    confirm=takeCommand().lower()
                    if "yes" in confirm:
                    
                        driver.find_element_by_xpath("/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div[1]/div/label/input").send_keys(c)
                        driver.find_element_by_xpath("/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div[2]/button").click()
                        sleep(3)
                        driver.find_element_by_xpath("/html/body/div[4]/div/div/div[3]/button[2]").click()
                        sleep(1)
                        engine.say("Here it is")
                        engine.runAndWait()
                    
                    elif "no" in confirm:
                         engine.say("please repeat the code again")
                         engine.runAndWait()
                         c=takeCommand().lower()
                         sleep(5)
                         driver.find_element_by_xpath("/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div[1]/div/label/input").send_keys(c)
                         driver.find_element_by_xpath("/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div[2]/button").click()
                         sleep(2)
                         driver.find_element_by_xpath("/html/body/div[4]/div/div/div[3]/button[2]").click()
                         sleep(1)
                         engine.say("Here it is")
                         engine.runAndWait()
                        
                    
                    
                    
            elif "on youtube" in query:
                 driver=webdriver.Chrome("G:\\Software\\chromedriver")
                 driver.get("https://www.youtube.com/")
                 sleep(1)
                 engine.say("please tell me what you want to play")
                 engine.runAndWait()
                 c=takeCommand().lower()
                 sleep(5)
                 
                 driver.find_element_by_xpath("/html/body/ytd-app/div/div/ytd-masthead/div[3]/ytd-searchbox/form/div/div[1]/input").send_keys(c)
                 driver.find_element_by_xpath("/html/body/ytd-app/div/div/ytd-masthead/div[3]/ytd-searchbox/form/button").click()
                 sleep(3)
                 engine.say("please click on the relevant suggestion")
                 engine.runAndWait()
               
                
                
                    
            elif 'open folder of c drive' in query:
                engine.say('which folder sir!')
                engine.runAndWait()
                c=takeCommand().lower()
                engine.say('opening sir!')
                engine.runAndWait()
                os.system('cd..')
                os.system('cd..')
                os.system(exp2+c+exp1)


            elif 'open folder of d drive' in query:
                engine.say('which folder sir!')
                engine.runAndWait()
                c=takeCommand().lower()
                engine.say('opening sir!')
                engine.runAndWait()
                os.system('cd..')
                os.system('cd..')
                os.system(exp3+c+exp1)


            elif 'open folder of e drive' in query:
                engine.say('which folder sir!')
                engine.runAndWait()
                c=takeCommand().lower()
                engine.say('opening sir!')
                engine.runAndWait()
                os.system('cd..')
                os.system('cd..')
                os.system(exp4+c+exp1)


            elif 'open folder of g drive' in query:
                engine.say('which folder sir!')
                engine.runAndWait()
                c=takeCommand().lower()
                engine.say('opening sir!')
                engine.runAndWait()
                os.system('cd..')
                os.system('cd..')
                os.system(exp5+c+exp1)


            elif 'close drive' in query:
                engine.say('closing sir!')
                engine.runAndWait()
                os.system('taskkill /im explorer.exe')




        ## NORMAL FUNCTIONS
        #    

            elif 'close chrome' in query:
                engine.say('closing sir!')
                engine.runAndWait()
                os.system('taskkill /im chrome.exe')

            elif 'stop music' in query:
                engine.say('stopping sir!')
                engine.runAndWait()
                os.system('taskkill /im wmplayer.exe')

            elif "shutdown system" in query:
                engine.say('Tell me the password sir!!!!')
                engine.runAndWait()
                c=takeCommand().lower()
                if "i love you" in c:
                    engine.say('shutting down sir! have a nice day')
                    engine.runAndWait()
                    os.system('shutdown -s -t 20')
                else:
                    engine.say('Wrong Password Sir!!!, cant shut sown')
                    engine.runAndWait()

            elif "cancel shutdown" in query:
                engine.say('cancelling sir!')
                engine.runAndWait()
                os.system('shutdown -a')

            elif "restart system" in query:
                engine.say('Tell me the password sir!!!!')
                engine.runAndWait()
                c=takeCommand().lower()
                if "i love you" in c:
                    engine.say('restarting sir! have a nice day')
                    engine.runAndWait()
                    os.system('shutdown -r -t 20')
                else:
                    engine.say('Wrong Password Sir!!!, cant restart')
                    engine.runAndWait()
            
            elif "cancel restart" in query:
                engine.say('cancelling sir!')
                engine.runAndWait()
                os.system('shutdown -a')

            elif 'close yourself' in query:
                engine.say('closing sir! thank you for your time')
                engine.runAndWait()
                os.system('taskkill /im Code.exe')        



            elif 'thank you' in query:
                engine.say('Welcome Sir! I am quiting now, Have a nice day sir!')
                engine.runAndWait()
                break
        
else:
    engine.say('Sorry wrong otp entered')
    engine.say('cant login')
    engine.runAndWait()
         


    


