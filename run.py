import os
import requests
import lxml

from dotenv import load_dotenv

import bs4
from bs4 import BeautifulSoup, element


load_dotenv()
headers = {
"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9", 
"Accept-Encoding": "gzip, deflate", 
"Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8", 
"Dnt": "1", 
"Upgrade-Insecure-Requests": "1", 
"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36", 
}


# headers = {'User-Agent':str(ua.chrome)}


# url = "https://hh.ru/search/vacancy?text=python&salary=&clusters=true&area=1&ored_clusters=true&enable_snippets=true"


     #  https://hh.ru/search/vacancy?text=python&salary=&clusters=true&area=1&ored_clusters=true&enable_snippets=true&page=0&hhtmFrom=vacancy_search_list   
     #  https://hh.ru/search/vacancy?text=python&salary=&clusters=true&area=1&ored_clusters=true&enable_snippets=true&page=39&hhtmFrom=vacancy_search_list
     #  https://hh.ru/search/vacancy?text=python&salary=&clusters=true&area=1&ored_clusters=true&enable_snippets=true&page=35&hhtmFrom=vacancy_search_list


# def get_all_page() -> int:
#     response = requests.get(url)
#     soup = BeautifulSoup(response.text, "lmxl")
#     return count_of_page

def main():
    url_full = "https://hh.ru/search/vacancy?text=python&salary=&clusters=true&area=1&ored_clusters=true&enable_snippets=true&page=0&hhtmFrom=vacancy_search_list"

    num_page = 0
    while(True):
        try:
            response = requests.get(url_full, headers=headers, allow_redirects=False)
        except requests.exceptions.TooManyRedirects:
            print("Fuck redirects")

        if (response.status_code != 200):
            break
        else:
            soup = BeautifulSoup(response.text, "lxml")
            data = soup.find_all("div", class_="serp-item")
            # print(data)
            # for item in data:
            #     title_job = item.select_one('a[data-qa="vacancy-serp__vacancy-title"]').text
            #     title_job_link = item.select_one('a[data-qa="vacancy-serp__vacancy-title"]').get("href")
            #     if type(item.select_one('span[data-qa="vacancy-serp__vacancy-compensation"]')) == bs4.element.Tag: # refactor
            #         salary_job = item.select_one('span[data-qa="vacancy-serp__vacancy-compensation"]').text
            #     else:
            #         salary_job = 'Not known'
            #     company_offer = item.select_one('a[data-qa="vacancy-serp__vacancy-employer"]').text
            #     company_offer_link = item.select_one('a[data-qa="vacancy-serp__vacancy-employer"]').get("href")
            #     print(company_offer_link)
            
                # select_one('a[data-autid="article-url"]').text
        num_page +=1
        url_full = f"https://hh.ru/search/vacancy?text=python&salary=&clusters=true&area=1&ored_clusters=true&enable_snippets=true&page={num_page}&hhtmFrom=vacancy_search_list"
    return num_page


if __name__ == "__main__":
    print(main())
