import mechanize #sudo pip install python-mechanize

import time

# br = mechanize.Browser() #initiating a browser
#
# br.set_handle_robots(False) #ignore robots.txt
#
# br.addheaders = [("User-agent","Mozilla/5.0")] #our identity
#
# gitbot = br.open("https://www.smilemiddle.com/pages/contact-us") #requesting the github base url
#
# br.select_form(nr=2) #the sign up form in github is in third position(search and sign in
#
# # formscome before signup)
#
# # br["_wpcf7"] = "104" #username for github
# #
# # br["_wpcf7_version"] = "4.4.2" #email for github
# #
# # br["_wpcf7_locale"] = "en_US" #password for github
# #
# # br["_wpcf7_unit_tag"] = "wpcf7-f104-p18-o1" #us
# #
# # br["_wpnonce"] = "3a450a8e70" #em
#
# # br["your-name"] = "Mayank"
# #
# # br["text-487"] = "Dubey" #u
# #
# # br["your-email"] = "dmayank0@gmail.com" #
# #
# # br["your-message"] = "Hi, I am Mayank Dubey an undergrad at IIT Delhi. I was AIR 66 in JEE, one of the most competetive examination where more than 12 lakh student compete. During my last 2 years at IIT Delhi I have developed a huge interest in coding. Is there any"         # Your message here.
# #
# # br["your-subject"] = "Application for Inernship"
#
# br["contact[name]"] = "Mayank"
# br["contact[email]"] = "dmayank0@gmail.com"
# br["contact[phone]"] = "8503936914"
# br["contact[body]"] = "TEST TEST TEST"
n = 0

while n < 100 :
    print("Loop :", n)
    br = mechanize.Browser() #initiating a browser

    br.set_handle_robots(False) #ignore robots.txt

    br.addheaders = [("User-agent","Mozilla/5.0")] #our identity

    gitbot = br.open("https:///") #requesting the github base url

    br.select_form(nr=0) #the sign up form in github is in third position(search and sign in

    # formscome before signup)

    # br["_wpcf7"] = "104" #username for github
    #
    # br["_wpcf7_version"] = "4.4.2" #email for github
    #
    # br["_wpcf7_locale"] = "en_US" #password for github
    #
    # br["_wpcf7_unit_tag"] = "wpcf7-f104-p18-o1" #us
    #
    # br["_wpnonce"] = "3a450a8e70" #em

    br["your-name"] = "Shivam"
    #
    br["text-487"] = "Mishra" #u
    #
    br["your-email"] = "shivam@ahataxis.com" #
    #
    br["your-message"] = """Hello Asha mam,
I have been following you since last 5 years now but recently I have been trying to get in touch with you and doing efforts for same restlessly. The reason is that I believe the fellowship can help me a lot in terms of figuring out my future plans and also the exposure can empower me to work on bigger projects. I don't have any mentor in the Industry, but I believe having one like you can change everything. I Believe under your guidance I can scale myself as well I can scale the movement you are pushing for. I want to closely work with you on things that you can plan for Indian Entrepreneurship system. I just seek 10 mins to convince you of my eligibility for RC fellowship, I am super excellent at anything I do and I am known for getting work done at any cost. I want to be a part of the eminent network that you have built and I believe I will be the best RC fellow ever. I just want an opportunity and I promise you that I will never fail you and you will always be proud of me and the investment you will make on me."""         # Your message here.
    #
    br["your-subject"] = "FOR RC FELLOWSHIP"
    # print "heey"
    # br["g7-name"] = "Mayank"
    # br["g7-email"] = "dmayank"+str(n)+"0@gmail.com"
    # br["g7-website"] = "http://ihaveeverywheretogo.in/contact/"
    # br["g7-comment"] = "TEST TEST TEST"+str(100+(n*5))
    sign_up = br.submit()

    print sign_up.geturl()
    print sign_up.getcode()

    # printing the end time
    print("The time of code execution end is : ")
    print(time.ctime())

    time.sleep(120)

    n = n + 1
