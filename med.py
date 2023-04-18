#!/usr/bin/python3
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# تحديد الرابط الهدف
med = input ("url====>")
target_url = "https://www." + med

# إرجاع قائمة المسارات
def get_paths(url):
    # إرجاع الصفحة كنص HTML
    page = requests.get(url).text
    # تحويل النص الHTML إلى كائن BeautifulSoup
    soup = BeautifulSoup(page, 'html.parser')
    # إنشاء قائمة فارغة لتخزين المسارات
    paths = []
    # البحث عن جميع العناصر <a> في الصفحة واستخراج قيمة href لكل عنصر
    for link in soup.find_all('a'):
        path = link.get('href')
        # تجاهل الروابط الخارجية والروابط الفارغة والرابط المؤدي لنفس الصفحة
        if path and 'http' not in path and '#' not in path and path not in paths:
            # إضافة المسار إلى القائمة واستخدام urljoin() لحساب الرابط الكامل للمسار
            paths.append(urljoin(url, path))
    return paths

# فحص جميع المسارات وطباعة نتائج الفحص
for path in get_paths(target_url):
    response = requests.get(path)
    print(f"{path}: {response.status_code}")
