from django.shortcuts import redirect, render
from django.contrib import admin
from home.models import NewData
# 크롤링을 위한 import 
import requests
from bs4 import BeautifulSoup

# DRF ( 원활한 데이터 편집을 위해 해놓았으나. 아직. 어떻게 이용할지는 계획에 없다.)
from home.serializers import NewsSerializer

# api 를 사용할까...?

# 홈 랜더
# 크롤링 데이터를 보여준다ㄴㄴ
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

# 크롤링데이터
def delete_data(request):
    # 체크박스로 선택한 애들을 배열형태로 전달받기
    # pk = [1,2,3] ...
    if request.method == "POST":
        pks = request.POST.getlist("pk", None) # get 으로하면 하나만 가져와서 배열에 들어있는 값을 얻을수없었다
        # getlist 를 사용하여 pk 키를 갖는 배열값을 얻을수있었다
        if pks:
            NewData.objects.filter(pk__in=pks).delete()
    # 실제로 데이터를 지울지 아니면 soft delete 를 할 지 고민고민~
    return redirect("home")
