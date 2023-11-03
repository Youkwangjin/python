from django.db import models
from django.template.defaultfilters import title

# Spring JPA 라고 생각하자

# 논리적인 테이블
class Guest(models.Model): # (id, title, content, regdate)
    # myno = models.AutoField(auto_created=True, primary_key=True)
    title = models.CharField(max_length = 100)
    content = models.TextField()
    regdate = models.DateTimeField()
    
    # 옵션(있으면 편하고 없어도 무관하다) 출력창에 연습이라는 문자열이 나오는 이유
    def __str__(self):
        return self.title
    
    # 정렬 방법 2
    class Meta:
        # ordering = ('title',) # 오름차순 정렬 tulpe 타입으로 적어줘야 한다.
        # ordering = ('title','-id')
        ordering = ('-id',) # id descend
    
