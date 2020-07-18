#imports
import requests
from bs4 import BeautifulSoup
import tkinter

location = input("Enter City: ")

#get accuweather
r = requests.get()