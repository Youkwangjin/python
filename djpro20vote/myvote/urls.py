from django.urls import path
from myvote import views


urlpatterns = [
    path('', views.DispFunc, name='disp'), # 요청이 gogo/을 의미.
    path('<int:question_id>', views.DetailFunc, name='detail'), # 인자 컴버터 <type:name> 요청이 gogo/1 or gogo/2
    path('<int:question_id>/vote', views.VoteFunc, name='vote'), # gogo/5/vote name 매핑은
    path('<int:question_id>/results', views.ResultFunc, name='results'),
]
