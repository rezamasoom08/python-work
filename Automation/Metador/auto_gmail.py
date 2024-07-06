import yagmail

yag = yagmail.SMTP("linuxhawks@gmail.com", "80#z@naheb@S")

try:
    yag.send(to = "reza.masoom.08@gmail.com", subject = " Testing Automation", contents = "Just a test", attachments = [r"hello.xlsx"])
    print("Email sent to recipients")

except:
    print("Error,email not sent")