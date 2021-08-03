import re
#  下方引号内添加替换掉请求头内容
headers_str = """
Accept: application/json, text/javascript, */*; q=0.01
Accept-Encoding: gzip, deflate, br
Accept-Language: zh-CN,zh;q=0.9,en;q=0.8
Cache-Control: no-cache
Connection: keep-alive
Content-Length: 77
Content-Type: application/json
User-Agent: Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1
X-Apple-App-Id: 632
X-Apple-Frame-Id: daw-10beaddd-c22f-4fd4-8aba-ef4909a721dd
X-Requested-With: XMLHttpRequest

"""

pattern = '^(.*?):(.*)$'


for line in headers_str.splitlines():
    print(re.sub(pattern,'\'\\1\':\'\\2\',',line).replace(' ',''))
