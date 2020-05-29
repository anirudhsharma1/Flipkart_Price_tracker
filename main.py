import requests  # For sending requests
from bs4 import BeautifulSoup  # Using for get the information from the webpage
import time  # Using for delay in results
import smtplib  # Using for sending mails
import pyperclip  # Using for copying the text from the clipboard

# Put your item link OR you can directly paste it by using pyperclip module
URL = pyperclip.paste()  # We are pasting our copied link \
# OR we can put the link directly URL = "Put your link here"

# Put your User-Agent in HEADERS, you can search on google by "my user agent"
HEADERS = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                         "Chrome/83.0.4103.61 Safari/537.36"}

print("Welcome to Flipkart price tracking service!!\n")
# Your Desired Price
WANT_PRICE = int(input("Enter your desired Price: "))
EmailAddress = "Your email address"  # Your EmailAddress
print("Please Give us the Email password for login..")
password = str(input("Enter Password: "))  # Enter Your Email password 
print("Enjoy your coffee! While i getting you the best deal")
ReceiverAddress = "Receiver email address"  # Enter Receiver EmailAddress, For getting the mails in your inbox


# ReceiverAddress


# This is use for check the price and compare with our WANT_PRICE
def price_checker():
    price = int(get_price())  # Calling our get_price() function and convert price into integer

    if price > WANT_PRICE:
        print("Current item price is {}.".format(current))

    elif price is WANT_PRICE:
        print("Voilaa....current price({}) is same as your want-price.".format(current))
        send_mail()  # Calling our send_mail() function for send the update

    else:
        print("This is a deal! item price is {}.".format(current))
        send_mail()  # Calling our send_mail() function for send the update


# This is use for making connections and getting the title and price value from the URL
def get_price():
    global current  # Making a global variable for the price_checker () function for show the item-price
    page = requests.get(URL, headers=HEADERS)
    soup = BeautifulSoup(page.text, 'html.parser')
    elem_title = soup.select('._35KyD6')  # Selecting the title element by Css Path finder
    title = elem_title[0].text.strip()  # Getting title and removing free spaces and tabs from the title element
    elem_price = soup.select('#container > div > div.t-0M7P._3GgMx1._2doH3V > div._3e7xtJ > div._1HmYoV.hCUpcT > '
                             'div._1HmYoV._35HD7C.col-8-12 > div:nth-child(2) > div > div._3iZgFn > div._2i1QSc > div'
                             ' > div._1vC4OE._3qQ9m1')  # Selecting the price element by Css Path finder
    current = elem_price[0].text.strip()  # Getting current price from the link and removing free spaces.
    raw_price = current[1:].split(",")  # Removing ',' and unwanted elements from the price
    price = "".join(raw_price)  # Joining the price char after removing unwanted elements
    print(title)  # Printing the title of our product
    # price = 22000  # For testing purposes you can change the price value
    return price  # We are returning the price. for using in the price_checker() function


# This function is used to send updates through email
def send_mail():
    sub = "Product price is dropped"
    body = " Thank you for using this Service!!"
    mailtext = "Subject:" + sub + '\n\n' + body + '\n\n' + URL
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login(EmailAddress, password)
    server.sendmail(EmailAddress, ReceiverAddress, mailtext)
    print("Email has successfully sent!")
    pass


if __name__ == "__main__":
    while True:  # Starting infinite loop
        price_checker()  # Calling our function
        time.sleep(2)  # Given delay by 2 seconds, you can change the delay accordingly to your needs
