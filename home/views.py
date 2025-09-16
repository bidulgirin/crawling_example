from django.shortcuts import redirect, render

# Create your views here.


from django.contrib import admin
from home.models import NewData
# 크롤링을 위한 import 
import requests
from bs4 import BeautifulSoup


def home(request):
    datas = NewData.objects.all()
    context={
        "datas" : datas
    }
    return render(request, "index.html", context)


# 크롤링 데이터 폼을 만들어야겠다...
def crawling(request):
    # create 할것 (craw)
    if request.method == "GET":
        # crawling 에서 받을 값을 담아오자
        url_name = request.GET.get("url", None)
        if url_name:
            
            title_name = request.GET.get("title", None)
            content_name = request.GET.get("content", None)
            author_name = request.GET.get("author", None)
            
            # 정적 크롤링 해보기
            url = url_name
            response = requests.get(url)
            
            if response.status_code == 200:  # 정상 응답 반환 시 아래 코드블록 실행
                soup = BeautifulSoup(response.content, 'html.parser')  # 응답 받은 HTML 파싱
                # 지금은 클래스로만 찾아요
                titles = soup.select(f'.{title_name}')
                print("GET데이터들")
                print(titles)
                # 일단 print로 찍어 봅시다.
                
                # 여기서 알고리즘 연습의 중요성을 느낍니다...
                newData = []
                for t in titles:
                    print(t)
                    newData.append(NewData(title = t.get_text(),
                                           author = "",
                                           content = "",
                                           ))
                if newData:
                    # 여러개의 데이터값을..넣으려고...해봤다...
                    NewData.objects.bulk_create(newData , batch_size=None, ignore_conflicts=False)
                  

            else:
                print('error')  # 오류 시 메시지 출력
    return redirect("home") # 메인페이지로 다시돌아가

# 1단계
# 크롤링을 한다.
# 크롤링을 한 데이터를 데이터 베이스에 넣는다.

# 2단계
# 크롤링을 할 대상을 html input 에 적는다.
# class 또는 id 로 대상을 찾도록 한다.
# title, content, author 에 대한 데이터를 각자 넣는다.


# 3단계
# 크롤링을 할 대상을 html input 에 적는다
# class 또는 id로 대상을 찾도록 한다
# 넣을 데이터베이스의 컬럼에 따라 html 의 form 이 동적으로 변경된다
# 
