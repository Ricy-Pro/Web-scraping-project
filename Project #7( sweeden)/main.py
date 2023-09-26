from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv
import time
import requests
driver = webdriver.Firefox() 
company_details = []

cnt=0

def is_in_this_category(category_id, electrician_name):
    driver.get(f"https://svensksolenergi.se/sok-medlemsforetag/#!?ids={category_id}")
    cnt=0
    while True:
        page_source = driver.page_source
        soup = BeautifulSoup(page_source, "html.parser")
        companies = soup.find_all("li", {"class": "mira-list-item"})

        if not companies:
            break  # No more pages to scrape

        # Check if the electrician's name exists on the current page
        for s, company in enumerate(companies):
            if s != 0:
                electrician_name1 = company.find("span", {"x-text": "item.contact"}).text.strip()
                if electrician_name == electrician_name1:
                    return True
        next_button_1= soup.find("div",{"x-show":"pages > 1"})
        is_button = next_button_1 is not None and "display: none" not in next_button_1.get('style', '').lower()
        
        # Wait for the "Next" button to become clickable
       
        total=soup.find("span",{"x-text":"total"}).text.strip()
        # Check if the "Next" button is disabled, indicating no more pages
        if is_button==False or float(total)/12-cnt<1:
            break
        else:
            next_button = WebDriverWait(driver, 40).until(
            EC.visibility_of_element_located((By.XPATH, "//span[contains(text(), 'Nästa')]"))
        )
            next_button.click()
            cnt=cnt+1
    
    return False

def check_category(category_name, category_id, electrician_name):
    category_button = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, f"//span[contains(text(), '{category_name}')]"))
    )
    category_button.click()
    is_in_category = is_in_this_category(category_id, electrician_name)
    category_button.click()  # Uncheck the category
    return is_in_category        
    
    
def extract_company_info(company):
    
    company_name = company.find("span", {"x-text": "item.name"}).text.strip()
    if company_name in visited_companies:
        return
    visited_companies.add(company_name)
    electrician_name = company.find("span", {"x-text": "item.contact"}).text.strip()
    email = company.find("a", {"x-text": "item.email"}).text.strip()
    website = company.find("a", {"x-text": "item.url"}).text.strip()
    linkedin = company.find("a", string="Linkedin").get('href')
    address = company.find("span", {"x-text": "item.address"}).text.strip()
    zipcode = company.find("span", {"x-text": "item.zip"}).text.strip()
    city = company.find("span", {"x-text": "item.city"}).text.strip()
    
    # Check certification status
    certified1_div = company.find("div", {"x-show": "item.attributes.includes('certified')"})
    certified2_div = company.find("div", {"x-show": "item.attributes.includes('certified2')"})
    checkmark_div = company.find("span", {"x-show": "item.attributes.includes('premium')"})
    is_certified1 = certified1_div is not None and "display: none" not in certified1_div.get('style', '').lower()
    is_certified2 = certified2_div is not None and "display: none" not in certified2_div.get('style', '').lower()
    grey_checkmark= checkmark_div is not None and "display: none" not in checkmark_div.get('style', '').lower()
    category_url="https://svensksolenergi.se/sok-medlemsforetag/#!?ids="
    
    category1=check_category("Besiktningsföretag","1489",electrician_name)
    
    category2=check_category("Byggföretag","2619",electrician_name)
    
    category3=check_category("Elhandelsföretag","2504",electrician_name)
    
    category4=check_category("Elnätsföretag","2585",electrician_name)
    
    category5=check_category("Fastighetsföretag","2597",electrician_name)
    
    category6=check_category("Finansiering av solprojekt","5308",electrician_name)
    
    category7=check_category("Forskning","2618",electrician_name)
    
    category8=check_category("Grossist","2507",electrician_name)
    
    category9=check_category("Innovationsföretag","2505",electrician_name)
   
    category10=check_category("Installationsföretag","2506",electrician_name)
    
    category11=check_category("Juridiskt konsultföretag","2586",electrician_name)
    
    category12=check_category("Kringtjänster","2508",electrician_name)
    
    category13=check_category("Medlemsorganisation","2704",electrician_name)

    category14=check_category("Projektutvecklare, t ex solparker","2509",electrician_name)

    category15=check_category("Tekniskt konsultföretag","2511",electrician_name)

    category16=check_category("Tillverkare","2503",electrician_name)

    category17=check_category("Universitet och högskola","2617",electrician_name)

    category18=check_category("Utbildningsföretag","2512",electrician_name)

    category19=check_category("YH-utbildare","2661",electrician_name)
    
    category20=check_category("Blekinge","2539",electrician_name)
    
    category21=check_category("Dalarna","2540",electrician_name)
    
    category22=check_category("Gotland","2541",electrician_name)
    
    category23=check_category("Gävleborg","2542",electrician_name)
    
    category24=check_category("Halland","2543",electrician_name)
    
    category25=check_category("Jämtland","2544",electrician_name)
    
    category26=check_category("Jönköping","2545",electrician_name)
    
    category27=check_category("Kalmar","2546",electrician_name)
    
    category28=check_category("Kronoberg","2547",electrician_name)
   
    category29=check_category("Norrbotten","2548",electrician_name)
    
    category30=check_category("Skåne","2549",electrician_name)
    
    category31=check_category("Stockholm","2550",electrician_name)
    
    category32=check_category("Södermanland","2551",electrician_name)

    category33=check_category("Uppsala","2552",electrician_name)

    category34=check_category("Värmland","2553",electrician_name)

    category35=check_category("Västerbotten","2554",electrician_name)

    category36=check_category("Västernorrland","2555",electrician_name)

    category37=check_category("Västmanland","2556",electrician_name)

    category38=check_category("Västra Götaland","2557",electrician_name)
    
    category39=check_category("Örebro","2558",electrician_name)
    
    category40=check_category("Östergötland","2560",electrician_name)
    
    
    
    

    if email.split('@')[0] == "info":
        company_details.append({
            "Company Name": company_name,
            "Electrician Name": electrician_name,
            "Contact Email": email,
            "Website": website,
            "Person Email": "-",
            "Local address": address,
            "Post code": zipcode,
            "City": city,
            "LinkedIn": linkedin,
            "Registered for electrical safety":is_certified1,
            "Has certified installers":is_certified2,
            "Platinum/Gold Status":grey_checkmark,
            "Besiktningsföretag":category1,
            "Byggföretag":category2,
            "Elhandelsföretag":category3,
            "Elnätsföretag":category4,
            "Fastighetsföretag":category5,
            "Finansiering av solprojekt":category6,
            "Forskning":category7,
            "Grossist":category8,
            "Innovationsföretag":category9,
            "Installationsföretag":category10,
            "Juridiskt konsultföretag":category11,
            "Kringtjänster":category12,
            "Medlemsorganisation":category13,
            "Projektutvecklare, t ex solparker":category14,
            "Tekniskt konsultföretag":category15,
            "Tillverkare":category16,
            "Universitet och högskola":category17,
            "Utbildningsföretag":category18,
            "YH-utbildare":category19,
            "Blekinge":category20,
            "Dalarna":category21,
            "Gotland":category22,
            "Gävleborg":category23,
            "Halland":category24,
            "Jämtland":category25,
            "Jönköping":category26,
            "Kalmar":category27,
            "Kronoberg":category28,
            "Norrbotten":category29,
            "Skåne":category30,
            "Stockholm":category31,
            "Södermanland":category32,
            "Uppsala":category33,
            "Värmland":category34,
            "Västerbotten":category35,
            "Västernorrland":category36,
            "Västmanland":category37,
            "Västra Götaland":category38,
            "Örebro":category39,
            "Östergötland":category40,
            


        })
    else:
        company_details.append({
            "Company Name": company_name,
            "Electrician Name": electrician_name,
            "Contact Email": "-",
            "Website": website,
            "Person Email": email,
            "Local address": address,
            "Post code": zipcode,
            "City": city,
            "LinkedIn": linkedin,
            "Registered for electrical safety":is_certified1,
            "Has certified installers":is_certified2,
            "Platinum/Gold Status":grey_checkmark,
            "Besiktningsföretag":category1,
            "Byggföretag":category2,
            "Elhandelsföretag":category3,
            "Elnätsföretag":category4,
            "Fastighetsföretag":category5,
            "Finansiering av solprojekt":category6,
            "Forskning":category7,
            "Grossist":category8,
            "Innovationsföretag":category9,
            "Installationsföretag":category10,
            "Juridiskt konsultföretag":category11,
            "Kringtjänster":category12,
            "Medlemsorganisation":category13,
            "Projektutvecklare, t ex solparker":category14,
            "Tekniskt konsultföretag":category15,
            "Tillverkare":category16,
            "Universitet och högskola":category17,
            "Utbildningsföretag":category18,
            "YH-utbildare":category19,
            "Blekinge":category20,
            "Dalarna":category21,
            "Gotland":category22,
            "Gävleborg":category23,
            "Halland":category24,
            "Jämtland":category25,
            "Jönköping":category26,
            "Kalmar":category27,
            "Kronoberg":category28,
            "Norrbotten":category29,
            "Skåne":category30,
            "Stockholm":category31,
            "Södermanland":category32,
            "Uppsala":category33,
            "Värmland":category34,
            "Västerbotten":category35,
            "Västernorrland":category36,
            "Västmanland":category37,
            "Västra Götaland":category38,
            "Örebro":category39,
            "Östergötland":category40,
        })

# The rest of your code remains the same

    
    




base_url = "https://svensksolenergi.se/sok-medlemsforetag/#!?page="
page_number = 1

# Navigate to the first page
driver.get(base_url + "1")

# Handle the cookie pop-up if it exists
try:
    # Wait for the cookie pop-up to appear
    time.sleep(3)
    cookie_popup = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "modal-cacsp-btn-accept"))
    )
    
    # Click the "Acceptera alla" button
    accept_cookies_button = cookie_popup.find_element(By.XPATH, "//a[contains(text(), 'Acceptera alla')]")
    accept_cookies_button.click()
except Exception as e:
    print("No cookie pop-up found or could not accept cookies:", str(e))
visited_companies = set()

while True:
    page_source = driver.page_source
    soup = BeautifulSoup(page_source, "html.parser")
    companies = soup.find_all("li", {"class": "mira-list-item"})
    
    if not companies:
        break  # No more pages to scrape
    
    # Skip the first item on each page (you can change this logic if needed)
    for s, company in enumerate(companies):
        if s != 0:
            extract_company_info(company)
    
    page_number += 1

    # Wait for the "Next" button to become clickable
    next_button = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "//span[contains(text(), 'Nästa')]"))
)


    # Check if the "Next" button is disabled, indicating no more pages
    # Check if the "Next" button is disabled, indicating no more pages
    
    if cnt>1000:
        break
    else:
        cnt=cnt+1
        print(cnt)
        next_button.click()
        
        

driver.quit()

csv_filename = "companies.csv"
with open(csv_filename, "w", newline="", encoding="utf-8") as csvfile:
    fieldnames = ["Company Name","Electrician Name","Person Email","Website","Contact Email","Post code","City","Local address","LinkedIn","Registered for electrical safety", "Has certified installers","Platinum/Gold Status","Besiktningsföretag","Byggföretag","Elhandelsföretag","Elnätsföretag","Fastighetsföretag","Finansiering av solprojekt","Forskning","Grossist","Innovationsföretag","Installationsföretag","Juridiskt konsultföretag","Kringtjänster","Medlemsorganisation","Projektutvecklare, t ex solparker","Tekniskt konsultföretag","Tillverkare","Universitet och högskola","Utbildningsföretag","YH-utbildare", "Blekinge","Dalarna",
            "Gotland",
            "Gävleborg",
            "Halland",
            "Jämtland",
            "Jönköping",
            "Kalmar",
            "Kronoberg",
            "Norrbotten",
            "Skåne",
            "Stockholm",
            "Södermanland",
            "Uppsala",
            "Värmland",
            "Västerbotten",
            "Västernorrland",
            "Västmanland",
            "Västra Götaland",
            "Örebro",
            "Östergötland"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(company_details)

print(f"Scraped data saved to {csv_filename}")
visited_companies.clear()