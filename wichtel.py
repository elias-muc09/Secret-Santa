import smtplib
import random


personen = {
    "Name1": "mail1",
    "Name2": "mail2",
    "Name3": "mail3",
    "Name4": "mail3",
    "Name5": "mail4"
    
}


verfuegbare_personen = list(personen.keys())


ziehungen = {}


for person in personen:

    moegliche_ziehungen = [p for p in verfuegbare_personen if p != person]
    

    gezogene_person = random.choice(moegliche_ziehungen)
    
    ziehungen[person] = gezogene_person

    verfuegbare_personen.remove(gezogene_person)

user = ("")
pwd = ("")


server = smtplib.SMTP("", )
server.starttls()  
server.login(user, pwd)  


for person, gezogen in ziehungen.items():
    RCPT_TO = personen[person]  
    mail_text = f"Hallo {person}, du wichtelst fuer {gezogen}!"
    subject = "Wichteln Zuordnung"
    
    
    DATA = "From:%s\nTo:%s\nSubject:%s\n\n%s" % (user, RCPT_TO, subject, mail_text)
    

    server.sendmail(user, RCPT_TO, DATA)


server.quit()

print("Alle E-Mails wurden versendet.")
