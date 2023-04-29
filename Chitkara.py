import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json
import time
import os
from webdriver_manager.chrome import ChromeDriverManager

with open('cookies.txt', 'r') as f:
       value1 = f.read()
with open('creds.txt', 'r') as f:
       value = f.read().split(',')
       #print(value)
       rollno = value[0]
       password = value[1]
print(rollno)
headers = {
"Cookie": f"_ga=GA1.4.1663202068.1609231179; ext_name=ojplmecpdpgccookcobabopnaifgidhf; _gcl_au=1.1.1280124026.1622616168; PHPSESSID={value1}",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36",
    "domain": "punjab.chitkara.edu.in"
    }


url = "https://punjab.chitkara.edu.in//Library/Student/ajaxInitStudentMarks.php" 
res = requests.post(url, headers=headers)


if 'Oops..Your session is' in res.text:
    print('Fetching Cookies will take time according to your Network Speed')

    driver = webdriver.Chrome('chromedriver', chrome_options=options)
    options.add_argument('headless')
    options.add_argument('window-size=1920x1080')
    options.add_argument("disable-gpu")
    driver = webdriver.Chrome()
    driver.get('https://punjab.chitkara.edu.in//Interface/index.php')
    driver.delete_all_cookies()
    driver.add_cookie({'domain': 'punjab.chitkara.edu.in', 'name': 'PHPSESSID', 'path': '/', 'value': f"{value1}"})
    driver.refresh()
    time.sleep(2)
    x = driver.find_element(By.XPATH, '//*[@id="username"]')
    x.send_keys(rollno)
    y = driver.find_element(By.XPATH, '//*[@id="password"]')
    y.send_keys(password)
    driver.find_element(By.XPATH, '//*[@id="form1"]/div[3]/input[1]').click()
    driver.close()
    
    
   # value = driver.get_cookie('PHPSESSID')['value']
    #with open('cookies.txt', 'w+') as f:
            #f.write(value)
headers1 = {
"Cookie": f"_ga=GA1.4.1663202068.1609231179; ext_name=ojplmecpdpgccookcobabopnaifgidhf; _gcl_au=1.1.1280124026.1622616168; PHPSESSID={value1}",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36",
    "domain": "punjab.chitkara.edu.in"
    }
n = 0
while(n<1):
    
    os.system('cls')
    #with open('cookies.txt', 'r') as f:
           #value1 = f.read()
           

    payload = { 'rClassId': '4502'}
    payload1 = {'studyPeriodId': '4502'}
    url = "https://punjab.chitkara.edu.in//Library/Student/ajaxInitStudentMarks.php" 
    res = requests.post(url, headers=headers1, data = payload1).json()
    #print(res)
    url1 = 'https://punjab.chitkara.edu.in//Library/Student/ajaxAttendanceList.php'
    att = requests.post(url1, headers=headers1, data = payload).json()
    all_marks = res['info']
    attendance = att['info']
    #print(all_marks)
    print('------Marks of 5th Sem-----' + '\n')
    for i in all_marks:
        print(i['subject'] + ' - ' + i['obtained'],end='\n')
    print()
    print('------Attendance of 5th Sem-----' + '\n')
    for i in attendance:
        print(i['subjectName1'] + ' - ' + i['finalPercentage'] +'%',end='\n')
    print()
    print('Made By RSkillers')
    with open('details.txt', 'w+') as f:
        f.write('''Marks of 3rd Semester

''')
        for i in all_marks:
            x = (i['subject'] + ' - ' + i['obtained'])
            f.write(x + '\n')
        f.write('''

Attendance of 3rd Semester

''')
        for i in attendance:
            x = (i['subjectName1'] + ' - ' + i['finalPercentage'] +'%')
            f.write(x + '\n')
    time.sleep(300)





