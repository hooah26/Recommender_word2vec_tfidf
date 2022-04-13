from bs4 import BeautifulSoup
import requests
import re
import pandas as pd
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from urllib.request import urlopen

df = pd.read_csv('./crawling_data/cleaned_names.csv')

df = df.sort_values(by = "drink_name")
df.info()
df.to_csv('./crawling_data/reviews_name_sort.csv', index=False)
