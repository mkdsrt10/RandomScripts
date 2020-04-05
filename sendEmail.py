# Send email to freshers with phone no., email, Name of respective team captain.
# Also send email to respective captain and vice captain about their info.

import smtplib

# SportInfo = {'Hockey':'Vaid Prakash Choudhry : 8888888888\nNitesh Kumar : 9999999999', 'Football':'Usman : 7777777777\nHarshit : 6666666666'}
SportsCap = {'Hockey':['niteshbyadwal111@gmail.com'], 'Basketball':["pradeeppetermurmu@gmail.com"], 'Squash':['bhandarimohit0509@gmail.com'], 'Volleyball': ['nqahmad1997@gmail.com'], 'Athletic':["neerajkumar.dakshana17@gmail.com"], 'Table':['lokeshchakri999@gmail.com'], 'Tennis':['karanmittalchd@gmail.com'], 'Cricket': ['gnjn007@gmail.com'],
 'Weight Lifting':['rustagi1998@gmail.com'], 'Squash':[]}   #, "abdmayank0@gmail.com"
def sendemailtoFresher(receivers, sport):
    gmail_id = 'abdmayank0@gmail.com'
    gmail_pwd = 'abd100test'
    # receivers = ['dmayank0@gmail.com']
    subject = "Info of %s Team of Nilgiri"%(sport)
    body = SportInfo[sport]
    email_text = """\
    From: %s
    To: %s
    Subject: %s

    Following is the contact info of team Captain & Vice-captain:
    %s
    """ % (gmail_id, ", ".join(receivers), subject, body)

    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(gmail_id, gmail_pwd)
    server.sendmail(gmail_id, receivers, email_text)
    server.close()
    print 'sent'

def sendemailVC(count):
#    gmail_id = 'abdmayank0@gmail.com'
    gmail_id = 'dmayank0@gmail.com'
    gmail_pwd = 'Mayank@20'
#    subject = "Info of Freshers of Nilgiri want to play %s"%(sport)
    subject = 'Urgent, Very important, long term impacting and Life changing | %d'%(count)
    print subject
#    receivers = SportsCap[sport]
    receivers = ['dmayank0@gmail.com']
    email_text = """\

        Hello Jeff,
        
        
        
        I am Mayank, a 3rd-year student from IIT Delhi Computer Science major. Currently, I have been working on a credit card & repayment platform, essentially for college students. I had worked on quite a few projects related to credit cards and credit systems in India in the recent past. A few are : credit card comparison engine and a recommender engine over it, a financial charge calculating engine for credit cards and also a financial news aggregator.
        
        
        As I see you are in Delhi and it can be a lifetime opportunity for me to meet you and share my ideas with you. I am writing this mail to give me 30 mins to meet you. I know you must be on a very tight schedule thus I am okay to meet you during any time of the day or at the airport. I am just very positive and I believe this is a great chance to meet my legend. Fingers crossed.
        
        
        Yours sincerely
        
        Mayank Dubey
        
        
        PS: Not looking for a selfie or write a social media post on how I met Jeff. Looking to see someone who runs one of the greatest startups in the world and meeting my legend
        
        
        
        About me: I have been working on quite a few projects related to credit cards and credit systems in India. I had built a credit-card comparison engine that actually compares different credit cards and not just like the current so-called comparison site which just lists the cards out. This was a project I have done in the guidance of KUNAL SHAH, founder CRED, founder of Freecharge. I have extended this engine to a credit card recommendation system during my internship at CRED. I have also build a financial info aggregator (finspace.in [1] & Playstore link [2]) that aimed to improve financial literacy for the students.
        
        
        [1] http://www.finspace.in [1]
        
        [2] https://play.google.com/store/apps/details?id=com.finspace

    """
    # gmail_id, ", ".join(receivers), subject,
    # From: %s
    # To: %s
    # Subject: %s

#    for data in datas:
#        email_text += "%s   %s   %s   %s\n"%(data[2], data[3], data[4], data[6])

    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(gmail_id, gmail_pwd)
    server.sendmail(gmail_id, receivers, email_text)
    server.close()
    print 'sent'

for i in range(2):
    sendemailVC(i)
