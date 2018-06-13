# Redis数据库的地址和端口
from urllib.parse import urlencode

HOST = '192.168.111.133'
PORT = 6379
POOL_NAME = 'proxies-set'

# 如果Redis有密码，则添加这句密码，否则设置为None或''
PASSWORD = None

# 获得代理测试时间界限
get_proxy_timeout = 20

# 代理池数量界限
POOL_LOWER_THRESHOLD = 100
POOL_UPPER_THRESHOLD = 1000

# 检查周期
VALID_CHECK_CYCLE = 60
POOL_LEN_CHECK_CYCLE = 20

# 测试API，用百度来测试
url='http://weixin.sogou.com/antispider/?from=%2fweixin'
requestdata = {
    'page': 1,
    'type': 2,
    's_from': ' input',
    'query': '故事会'
}
requestdata = urlencode(requestdata)
TEST_API = url+requestdata
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 \
    (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36',
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Accept-Language': 'zh-CN,zh;q=0.8'
}