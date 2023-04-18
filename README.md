# med
هذه الأداة هي عبارة عن سكربت يمكن استخدامه لفحص صحة الروابط الموجودة في صفحة ويب معينة. يتم تحديد صحة الرابط بتحديد حالة الاستجابة التي تتلقاها الأداة من الخادم الذي يقدم هذا الرابط.
كيفية الاستخدام

    تأكد من تثبيت Python 3 على جهاز الكمبيوتر الخاص بك.
    تثبيت الأداة عن طريق الأمر التالي:

pip install med

    قم بتشغيل الأمر med في موجه الأوامر في دليل الصفحة الإلكترونية التي تريد فحص روابطها. سيقوم الأمر بطباعة نتائج الفحص على الشاشة.

مثال:

arduino

med https://www.example.com

ستقوم هذه الأمر بفحص صفحة الويب في https://www.example.com وسيتم طباعة نتائج الفحص على الشاشة.
توثيق

توثيق الأداة يمكن العثور عليه في ملف docs.md.
المساهمة

للمساهمة في تطوير هذه الأداة، يرجى إرسال طلب اندماج (Pull Request) إلى هذا المستودع. يتمتع المساهمون النشطون بفرصة الانضمام إلى فريق تطوير الأداة.
الرخصة

هذه الأداة مرخصة بترخيص MIT. الرجاء الاطلاع على ملف LICENSE للحصول على مزيد من المعلومات.


MED Link Checker

MED is a simple command-line tool for checking the status of links in a given URL.
Installation

To install MED, simply clone the repository and install the required packages:

bash

git clone https://github.com/mohammed-bouchahma/med.git
cd med
pip install -r requirements.txt

Usage

To check the status of links in a URL, use the following command:

mathematica

python med.py <URL>

For example:

arduino

python med.py https://www.example.com/

The tool will then check all links in the given URL and return their status codes. It will also indicate any broken links (status code >= 400).

By default, MED will follow redirects up to a maximum of 10 times. You can change this by passing the --max-redirects argument:

arduino

python med.py <URL> --max-redirects 5

You can also choose to output the results to a file using the --output argument:

css

python med.py <URL> --output results.txt

License

This tool is released under the MIT License. Feel free to use, modify, and distribute it as you see fit.
