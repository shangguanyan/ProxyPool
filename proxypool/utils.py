import asyncio
import asyncio

import aiohttp
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import requests,time
from proxypool.setting import *
from bs4 import BeautifulSoup


def get_page(url, options={}):
    # try:
    #     ua = UserAgent()
    # except FakeUserAgentError:
    #     pass
    # base_headers = {
    #     'User-Agent':  ua.random,
    #     'Accept-Encoding': 'gzip, deflate, sdch',
    #     'Accept-Language': 'zh-CN,zh;q=0.8'
    # }
    # headers = dict(base_headers, **options)
    # print('Getting', url)
    # try:
    #     r = requests.get(url, headers=headers)
    #     print('Getting result', url, r.status_code)
    #     if r.status_code == 200:
    #         return r.text
    # except ConnectionError:
    #     print('Crawling Failed', url)
    #     return None
    options = Options()
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)
    driver.get(url)
    #强制等待
    time.sleep(10)
    return driver.page_source

def get_page1(url):
    """将网页解析为 BeautifulSoup 对象并返回
    :param url: web url
    :return: BeautifulSoup
    """
    r = requests.get(url, headers=HEADERS)
    try:
        try:
            soup = BeautifulSoup(r.content.decode("utf-8"), 'lxml')
        except UnicodeDecodeError:
            soup = BeautifulSoup(r.text, 'lxml')
        return soup
    except ConnectionError:
        return None



class Downloader(object):
    """
    一个异步下载器，可以对代理源异步抓取，但是容易被BAN。
    """

    def __init__(self, urls):
        self.urls = urls
        self._htmls = []

    async def download_single_page(self, url):
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as resp:
                self._htmls.append(await resp.text())

    def download(self):
        loop = asyncio.get_event_loop()
        tasks = [self.download_single_page(url) for url in self.urls]
        loop.run_until_complete(asyncio.wait(tasks))

    @property
    def htmls(self):
        self.download()
        return self._htmls
