# 멀티 프로세스
import requests  # 접근하는 방법
from bs4 import BeautifulSoup as bs
import time
from multiprocessing import Pool

# 스크래핑 대상 컨텐츠 : http://beomi.github.io/beomi.github.io_old/

# 하이퍼 링크 읽기
def get_links():
    data = requests.get("http://beomi.github.io/beomi.github.io_old/").text  # 문자열 읽기
    soup = bs(data, 'html.parser')
    print(type(soup))  # <class 'bs4.BeautifulSoup'>
    my_titles = soup.select('h3 > a')
    data = []
    for title in my_titles:
        data.append(title.get('href'))
    return data

def get_content(link):   # 여기서 link는 https://beomi.github.io 뒤에 오는 URL
    abs_link = "https://beomi.github.io" + link  # 완전한 link 읽기
    # print(abs_link)
    data = requests.get(abs_link).text
    print(data)
    soup = bs(data, 'html.parser')
    print(soup.select('h1')[0].text)

if __name__ == '__main__':
    print(get_links())
    # 갯수 확인
    print(len(get_links()))
    start_time = time.time()

    ''' 직렬 방법
    for link in get_links():
        get_content(link)
    '''

    # 병렬 방법
    pool = Pool(processes=4)
    pool.map(get_content, get_links())

    # 소요시간
    print("---%s 초---"%(time.time() - start_time))
    #  직렬 : 7.770294666290283 초
    #  병렬 : 4.703183650970459 초
    
    