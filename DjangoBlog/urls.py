"""DjangoBlog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
import xadmin
from book.views import BookListViewSet
from blog.views import BlogListView
from rest_framework.documentation import include_docs_urls
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'books', BookListViewSet)


urlpatterns = [
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', xadmin.site.urls),
    url(r'^', include(router.urls)),
    url(r'blogs/$', BlogListView.as_view(), name="blogs-list"),
    # 文档
    url(r'docs/', include_docs_urls(title='Your API',
                                    authentication_classes=[],
                                    permission_classes=[])),
]
