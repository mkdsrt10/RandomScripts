import smtplib, ssl

# Create a secure SSL context
context = ssl.create_default_context()

def sendemailVC(count):
    gmail_id = 'abdmayank0@gmail.com'
    gmail_pwd = 'abd100test'
    subject = 'Urgent, Product delievery fraud | %d'%(count)
    receivers = ['escalations@flipkart.com', 'kalyan@flipkart.com', 'kalyan.krishnamurthy@flipkart.com']
    email_text = """

        Hello Flipkart,

        I have an order which was ought to be delivered by 22 June but I recieved a message that it was delivered on 20th June. We didn't recieve any order and no one even called us.

        These are the order details :

        Order ID: OD118899193433573000
        Order Date: 14-06-2020
        Invoice Date: 15-06-2020
        PAN: AAICA4872D
        CIN: U52100DL2010PTC202600

        Lenovo Ideapad C340 Core
        i3 10th Gen - 4 GB/256 GB
        SSD/Windows 10 Home
        C340-14IML Laptop

        Ship To
        Kirti Kumar Dubey
        H.No. 113, Raghuwanshipura,
        SohagpurDistrict: Hoshangabad,
        Madhya Pradesh, Sohagpur.
        Sohagpur 461771 Madhya Pradesh

        I have raised a complain also. They told me to look at neighbours and relative but when I asked to get the phone number of delievery agents they denied to give me that info.
        I request you to provide me the details of deleivery agent or let the product delievered ASAP. I have to get the order before 23rd in anycase.

    """

    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(gmail_id, gmail_pwd)
    server.sendmail(gmail_id, receivers, email_text)
    server.close()
    # print 'sent'

for i in range(2):
    sendemailVC(i)
