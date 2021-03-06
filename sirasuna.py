import urllib.request
import codecs
import re
import datetime
import glob


def html_get():
    url = "http://shirasunaryou.sakura.ne.jp/cgi-bin/shirasuna/kondate/index.cgi?display=sp"
    title = "kondate_html_1now.txt"
    urllib.request.urlretrieve(url, "{0}".format(title))
    url = "http://shirasunaryou.sakura.ne.jp/cgi-bin/shirasuna/kondate/index.cgi?next=1&display=sp"
    title = "kondate_html_2next.txt"
    urllib.request.urlretrieve(url, "{0}".format(title))
    f = open('kondate_html.txt', 'w')
    for name in glob.glob('kondate_html_*.txt'):
        for line in codecs.open(name, 'r', 'shift_jis'):
            f.write(line[:-1])
    f.close()
    kondate_get()


def kondate_get():
    kondate = []

    f = codecs.open('kondate_html.txt', 'r', 'utf-8', 'ignore')
    file_1 = open('kondate_1.txt', 'w')
    file_2 = open('kondate_2.txt', 'w')
    file_3 = open('kondate_3.txt', 'w')
    file_4 = open('kondate_4.txt', 'w')
    file_5 = open('kondate_5.txt', 'w')

    file_line = f.readlines()
    for line in file_line:
        if not line[0] == "<":
            line = line.replace("<br>", "")
            kondate.append(" " + line)
        if line[0:4] == "<h2>":
            line = line.replace("<h2>", "")
            line = line.replace("</h2>", "")
            kondate.append(line)
        if line[0:4] == "<h4>":
            line = line.replace("<h4>", "")
            line = line.replace("</h4>", "")
            line = "\n" + line
            kondate.append(line)

    flag = 0
    for line in kondate:
        today = datetime.datetime.today()
        today += datetime.timedelta(days=flag)
        tmp = str(today.month) + "/" + str(today.day)
        if tmp in line:
            flag += 1
        if flag == 0:
            continue
        if flag == 1:
            file_1.write(line)
        elif flag == 2:
            file_2.write(line)
        elif flag == 3:
            file_3.write(line)
        elif flag == 4:
            file_4.write(line)
        elif flag == 5:
            file_5.write(line)

    f.close()
    file_1.close()
    file_2.close()
    file_3.close()
    file_4.close()
    file_5.close()
