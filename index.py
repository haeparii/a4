#!python
#-*- coding: utf-8 -*-

import sys
import codecs
import cgi

import cgitb
cgitb.enable()

sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())

print("Content-Type: text/html")    
print()                             

import cgi
form = cgi.FieldStorage()
pageid = form["id"].value

print('''
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>a4 : 읽고 쓰는 삶!</title>
    <link rel="stylesheet" href="style.css">

</head>

<body>
<h1><a href="index.py?id=a4">a4</a></h1>
    <div id="grid">
        <ol>
            <li><a href="index.py?id=manuscript">Manuscript</a></li>
            <li><a href="index.py?id=beingsiin" >Beingsiin</a></li>
            <li><a href="index.py?id=coccodrillo">Coccodrillo</a></li>
        </ol>
        <div id="article">
        <h2>{title}</h2>
        <p>
        <img class="img_size" src="img/a4.jpg" title="a4 paper" alt="a4 paper">
        </p>
        <p>
            A 계열의 종이는 금강비율의 크기로 정의되어 있으며, 실제 크기는 이론적으로 계산된 수치를 밀리미터 단위로 반올림한 것이다. A0은 넓이가 1m²가 되고 앞의 비율을 만족하는 종이이며, A1, A2, A3, A4 등의 종이 크기는 각각 그 이전 크기의 종이를 짧은 변에 평행하도록 이등분하여 자른 것이다. 따라서 A 계열 종이를 반으로 접거나 자르면 보다 작은 크기의 A 계열 종이가 된다. 가장 널리 쓰이는 A4는 210 × 297mm 크기이다.    
        </p>
        </div>
    </div>
</body>
</html>
'''.format(title=pageid))