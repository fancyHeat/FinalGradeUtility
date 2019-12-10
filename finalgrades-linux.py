from selenium import webdriver
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from filecmp import cmp
import pandas as pd
import credentials, time, os, smtplib

# Define Constants
ESERVICE_LANDING = "https://www.mnsu.edu/eservices/"
RECORDS_LANDING = "https://eservices.minnstate.edu/student-portal/secure/grades?campusid=071&functionId=3004"
LOGOUT = "https://eservices.minnstate.edu/student-portal/secure/logout.do"

# Initialize Driver
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_path = "/app/chromedriver"
driver = webdriver.Chrome(chrome_path, options=chrome_options)

def login():
    driver.get(RECORDS_LANDING)
    # Initial Login and Password
    element = driver.find_element_by_id("userName")
    element.send_keys(credentials.username)
    element = driver.find_element_by_id("password")
    element.send_keys(credentials.password)
    driver.find_element_by_xpath("/html/body/div/div[2]/div[1]/div[1]/form/table/tbody/tr[5]/td[2]/input").click()

    # Get HTML
    driver.find_element_by_xpath("/html/body/div[2]/div[1]/div/div[2]/div/div[1]/div/div/form/div/select").click()
    driver.find_element_by_xpath("/html/body/div[2]/div[1]/div/div[2]/div/div[1]/div/div/form/div/select/option[3]").click()
    driver.find_element_by_id("requestGradesBtn").click()

    # # Required Acknowledgments
    # driver.find_element_by_id("accept_tuition").click()
    # driver.find_element_by_id("understand_drop").click()
    # driver.find_element_by_name("emquery").click()
    #
    # # Acknowledge Bill
    # driver.find_element_by_name("Continue").click()


def getGrades():
    content = driver.page_source

    # Parse HTML
    df = pd.DataFrame(pd.read_html(content)[0])

    # Write to a file
    try:
        os.replace('new.html', 'old.html')
    except FileNotFoundError:
        pass

    df.to_html("new.html", index=False)


def refreshPage():
    driver.refresh()


def sendMail():
    # Formulate Message
    file = open("new.html", "r")
    html = file.read()
    file.close()
    msg = MIMEMultipart('alternative')
    msg['Subject'] = "UPDATE: There Has Been Updates To Your Final Grades"
    msg['From'] = credentials.gmail_username
    msg['To'] = credentials.to_address
    body = MIMEText(html, "html")
    msg.attach(body)

    server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    server.ehlo()
    server.login(credentials.gmail_username, credentials.gmail_password)
    server.sendmail(credentials.gmail_username, credentials.to_address, msg.as_string())
    server.quit()


def checkDifference():

    if cmp("new.html", "old.html") is False:
        sendMail()
        print("changed")
    else:
        print("no change")

login()
while True:
    refreshPage()
    getGrades()
    checkDifference()
    time.sleep(60)





