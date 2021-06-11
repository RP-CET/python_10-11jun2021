#sends email via Outlook
#pip install pywin32

import win32com.client

subject = 'email subject'
body = '<html><body>' + 'This is a test email. June Python 2021<br />' + '</body></html>'
recipient = 'jason_lim@rp.edu.sg; abc@xyz.com'


#Create and send email
olMailItem = 0x0
obj = win32com.client.Dispatch("Outlook.Application")
newMail = obj.CreateItem(olMailItem)
newMail.Subject = subject
newMail.HTMLBody = body
newMail.To = recipient
newMail.CC = recipient

#newMail.display()
newMail.Send()
print("Sent")
