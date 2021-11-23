# TODO find out how to run this in gcloud

import requests
import smtplib
import ssl

# send email function


def send_email(recipient, subject, body):
    # google how to create app password for gmail
    user = "your.email@gmail.com"
    pwd = "yourAppPwd"
    # u can chain recipients together if u pass them as a list
    TO = recipient if isinstance(recipient, list) else [recipient]
    # generating the email message looks really awkward with the smtplib
    message = """From: %s\nTo: %s\nSubject: %s\n\n%s
    """ % (user, ", ".join(TO), subject, body)

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login(user, pwd)
        server.sendmail(user, TO, message)
        server.close()
        print('successfully sent the mail')
    except:
        print("failed to send mail")


# main crawl function with print statements as a script debugging tool (fast and lazy)
def main():
    with open("log.txt", "r+") as f:
        text = int(f.read())
        print("current value in file: " + str(text))
        site_address = "https://www.att.hel.fi/fi/omistusasunnot/asunto-oy-helsingin-priki-johanna"
        response = requests.get(site_address)
        print("response status code: " + str((response.status_code)))
        content = response.text
        match = "Vapaa"
        match_count = content.count(match)
        print("found matches: " + str(match_count))
        if match_count != text:
            if(match_count > text):
                print("count has changed to bigger")
                title = "Bot Triggered"
                send_email("your@email.com", title, site_address)
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
