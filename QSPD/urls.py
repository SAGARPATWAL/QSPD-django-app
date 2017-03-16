from django.conf.urls import url
from QSPD import views

urlpatterns=[url(r'^$',views.HomePageView.as_view()),
#url(r'^go-find-quote',views.post),
url(r'^ans/$',views.AnsPageView.as_view())

]
