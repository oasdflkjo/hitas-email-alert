# TODO find out how to run this in google cloud as a serverless cloud function

import requests
import smtplib
import ssl

# send email function


def send_email(msg, to):
    port = 587  # For starttls
    smtp_server = "smtp.gmail.com"
    sender_email = "your.bot.email@gmail.com"
    receiver_email = to
    # hide this for security reasons when uploading to github
    # just google how to send mail from gmail with python to get this
    password = "your_google_app_password"
    context = ssl.create_default_context()
    with smtplib.SMTP(smtp_server, port) as server:
        server.ehlo()  # Can be omitted
        server.starttls(context=context)
        server.ehlo()  # Can be omitted
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, msg)


# main crawl function that has print debugging statements cos I'm fast and lazy
def main():
    with open("log.txt", "r+") as f:
        text = int(f.read())
        print("current value in file: " + str(text))
        response = requests.get(
            "https://www.att.hel.fi/fi/omistusasunnot/asunto-oy-helsingin-siili")
        print("response status code: " + str((response.status_code)))
        content = response.text
        match = "Vapaa"
        match_count = content.count(match)
        print("found matches: " + str(match_count))
        if match_count != text:
            if(match_count > text):
                print("count has changed to bigger")
                msg = "www.att.hel.fi/fi/omistusasunnot/asunto-oy-helsingin-siili"
                email = "your@email.com"
                send_email.send_email(msg, email)
                print("emails send")
            else:
                print("count has changed to smaller")
            file = open("log.txt", "w")
            file.write(str(match_count))
            file.close()
            print("file updated")
        else:
            print("count was same and no emails were sent")
    print("closing")


if __name__ == "__main__":
    main()
