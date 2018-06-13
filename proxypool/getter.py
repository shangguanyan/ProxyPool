from .utils import get_page,get_page1
from pyquery import PyQuery as pq
import re
import json
import time

class ProxyMetaclass(type):
    """
        元类，在FreeProxyGetter类中加入
        __CrawlFunc__和__CrawlFuncCount__
        两个参数，分别表示爬虫函数，和爬虫函数的数量。
    """

    def __new__(cls, name, bases, attrs):
        count = 0
        attrs['__CrawlFunc__'] = []
        for k, v in attrs.items():
            if 'crawl_' in k:
                attrs['__CrawlFunc__'].append(k)
                count += 1
        attrs['__CrawlFuncCount__'] = count
        return type.__new__(cls, name, bases, attrs)


class FreeProxyGetter(object, metaclass=ProxyMetaclass):
    def get_raw_proxies(self, callback):
        proxies = []
        print('Callback', callback)
        for proxy in eval("self.{}()".format(callback)):
            print('Getting', proxy, 'from', callback)
            proxies.append(proxy)
        return proxies

#里面的ip都不可用了
    # def crawl_ip181(self):
    #     start_url = 'http://www.ip181.com/'
    #     html = get_page(start_url)
    #     doc = pq(str(html))
    #     item = doc('p').html()
    #
    #     dict_json = json.loads(item)
    #     for result in dict_json.get('RESULT'):
    #         ip = result.get('ip')
    #         port = result.get('port')
    #         addr_port = ip + ':' + port
    #         yield addr_port.replace(' ', '')



    # def crawl_kuaidaili(self):
    #     for page in range(1, 10):
    #         # 国内高匿代理
    #         start_url = 'https://www.kuaidaili.com/free/inha/{}/'.format(page)
    #         html = str(get_page(start_url))
    #         ip_adress = re.compile(
    #             '<td data-title="IP">(.*)</td>\s*<td data-title="PORT">(\w+)</td>'
    #         )
    #         re_ip_adress = ip_adress.findall(str(html))
    #         for adress, port in re_ip_adress:
    #             result = adress + ':' + port
    #             yield result.replace(' ', '')

#有可用ip
    def crawl_xicidaili(self):
        for page in range(1, 4):
            start_url = 'http://www.xicidaili.com/wt/{}'.format(page)
            html = get_page(start_url)
            # html1 = str(get_page1(start_url)).replace("\n","")
            ip_adress = re.compile('<td class="country"><img src="http://fs.xicidaili.com/images/flag/cn.png" alt="Cn" /></td>\n.*?<td>(.*?)</td>\n.*?<td>(.*?)</td>')
            re_ip_adress = ip_adress.findall(html)
            for adress, port in re_ip_adress:
                result = adress + ':' + port
                yield result.replace(' ', '')
    #
#有可用ip
    def crawl_daili66(self, page_count=4):
        start_url = 'http://www.66ip.cn/{}.html'
        ip_port_pattern = re.compile('<tr><td>([0-9].*?)</td><td>([0-9]+)</td>')
        for page in range(1,4):
            url = start_url.format(page)
            html = get_page(url).replace('\n','')
            if html:
                re_ip_port = ip_port_pattern.findall(html)
                for ip,port in re_ip_port:
                    result = ip + ':' + port
                    yield result.replace(' ', '')

#有可用ip
    def crawl_data5u(self):
        for i in ['gngn', 'gnpt']:
            start_url = 'http://www.data5u.com/free/{}/index.shtml'.format(i)
            html = get_page(start_url).replace('\n','').replace('\s','').replace(' ','')
            ip_adress = re.compile(
                '<ulclass="l2">.*?<span><li>([0-9].*?)</li></span>.*?<span.*?><li.*?>([0-9]+)</li></span>'
            )
            # \s * 匹配空格，起到换行作用
            re_ip_adress = ip_adress.findall(html)
            for adress, port in re_ip_adress:
                result = adress + ':' + port
                yield result.replace(' ', '')
    # #
#不可用
    # def crawl_premproxy(self):
    #     for i in ['China-01', 'China-02', 'China-03', 'China-04', 'Taiwan-01']:
    #         start_url = 'https://premproxy.com/proxy-by-country/{}.htm'.format(
    #             i)
    #         html = str(get_page(start_url))
    #         if html:
    #             ip_adress = re.compile('<td data-label="IP:port ">(.*?)</td>')
    #             re_ip_adress = ip_adress.findall(html)
    #             for adress_port in re_ip_adress:
    #                 yield adress_port.replace(' ', '')

#不可用
    # def crawl_xroxy(self):
    #     for i in ['CN', 'TW']:
    #         start_url = 'http://www.xroxy.com/proxylist.php?country={}'.format(
    #             i)
    #         html = str(get_page(start_url))
    #         if html:
    #             ip_adress1 = re.compile(
    #                 "title='View this Proxy details'>\s*(.*).*")
    #             re_ip_adress1 = ip_adress1.findall(html)
    #             ip_adress2 = re.compile(
    #                 "title='Select proxies with port number .*'>(.*)</a>")
    #             re_ip_adress2 = ip_adress2.findall(html)
    #             for adress, port in zip(re_ip_adress1, re_ip_adress2):
    #                 adress_port = adress + ':' + port
    #                 yield adress_port.replace(' ', '')
