from bs4 import BeautifulSoup as bs
from splinter import Browser
from webdriver_manager.chrome import ChromeDriverManager
import time
import requests
import os
import pandas as pd
from splinter import Browser
from webdriver_manager.chrome import ChromeDriverManager

def scrape():
                url='https://redplanetscience.com/'

                response=requests.get(url)
                soup = bs(response.text, "html.parser")
                executable_path = {"executable_path": ChromeDriverManager().install()}
                browser = Browser("chrome", **executable_path, headless=False)

                url='https://redplanetscience.com/'
                Browser.visit(url)
                html=Browser.html
                soup=bs(html1, 'html.parser')
                soup.find_all("div", class_="content_title")

                news_title1=soup.find_all("div", class_="content_title")[0].text
                news_paragraph=soup.find_all("div", class_="article_teaser_body")[0].text

                space_url='https://spaceimages-mars.com'
                Browser.visit(space_url)
                html2=Browser.html

                soup2=bs(html2,'html.parser')
                featured_image_url = space_url+"/"+soup2.find_all("a", class_="fancybox-thumbs")[0]["href"]
                featured_image_url

                #get facts into html table
                facts_url='https://galaxyfacts-mars.com'
                Browser.visit(facts_url)
                html3=Browser.html
                soup3=bs(html3,'html.parser')
                soup3.find_all('tbody')

                #get Mars hemispheres pictures
                hemi_url='https://marshemispheres.com/'
                Browser.visit(hemi_url)

                #HTML object
                html4=Browser.html
                soup4=bs(html4,'html.parser')

                hemi_site=soup4.find_all('div',class_='item')

                #empty img list
                hemi_img=[]
                titles=[]

                for pic in hemi_site:
                    hemi_img.append(hemi_url + pic.find('a')['href'])
                    titles.append(pic.find('h3').text.strip())

                print(hemi_img)
                print(titles)

                img_list=[]
                for item in range(len(hemi_img)):
                    img_list.append({'title':titles[item],'img_url':hemi_img[item]})
                img_list
                return img_list