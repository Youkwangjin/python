from django.urls import path
from views import view1, view2

urlpatterns = [    
    path('list', view1.ListFunc),
    path('insert', view1.InsertFunc),
    path('search', view1.SearchFunc),
    path('content', view1.ContentFunc),
    path('update', view1.UpdateFunc),
    path('delete', view1.DeleteFunc),  
    # 댓글은 view2에서 처리한다.
    path('reply', view2.ReplyFunc),
    path('replyok', view2.ReplyOkFunc),
]