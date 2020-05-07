from django.urls import re_path, include

urlpatterns = [
    re_path(r'^taggit_autosuggest/', include('taggit_autosuggest.urls')),
]
