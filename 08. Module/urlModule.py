import urllib.request

def get_web(url):
    response = urllib.request.urlopen(url)
    data = response.read()
    decoded = data.decode('UTF-8')
    return decoded

url = input('웹 페이지 주소를 입력해주세요. ')
content = get_web(url)
print(content)
