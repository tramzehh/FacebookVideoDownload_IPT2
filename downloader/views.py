from django.shortcuts import render
from django.views import View
import os
import re
import requests
from datetime import datetime

# Create your views here.
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
class IndexPage(View):
    def get(self, request, *args, **kwargs):
        return render(request, "downloader/home.html")

