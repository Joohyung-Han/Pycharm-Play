# lotto. py


# import requests

# def main():
#     for i in range(1,4):
#         main_url = "https://dhlottery.co.kr/gameResult.do?method=byWin&" + str(i)
#         response = requests.get(main_url, verify=False)
#         print(response)
#
# if __name__=="__main__":
#     main()


# import requests


# def main():
# main_url = "https://dhlottery.co.kr/gameResult.do?method=byWin&drwNo="
# for i in range(1,4):
#     response=requests.get(main_url+str(i))
#     print(response)

# if __name__ == "__main__":
#     main()


# article > div:nth-child(2) > div > div.win_result


# import requests
# from bs4 import BeautifulSoup
#
# def main():
#     basic_url = "https://dhlottery.co.kr/gameResult.do?method=byWin&drwNo="
#     for i in range(1,4):
#         resp = requests.get(basic_url + str(i))
#         soup = BeautifulSoup(resp.text, 'lxml')
#         line = str(soup.find("meta", {"id":"desc","name":"description"})['content'])
#         print(line)
#
# if __name__=="__main__":
#     main()


# import requests
# from bs4 import BeautifulSoup
#
# def main():
#     basic_url= "https://dhlottery.co.kr/gameResult.do?method=byWin&drwNo="
#     for i in range(1,5):
#         resp = requests.get(basic_url + str(i))
#         soup = BeautifulSoup(resp.text, "lxml")
#         line = str(soup.find("meta",{"id":"desc","name":"description"})['content'])
#
#         print("당첨회차:" +str(i))
#
#         begin = line.find("당첨번호")
#         begin = line.find(" ",begin) + 1
#         end = line.find(".", begin)
#         numbers = line[begin:end]
#         print(",당첨번호"+numbers)
#
#         begin = line.find("총")
#         begin = line.find(" ", begin) + 1
#         end = line.find("명", begin)
#         persons = line[begin:end]
#         print(",당첨인원" + numbers)
#
#         begin = line.find("당첨금액")
#         begin = line.find(" ", begin) + 1
#         end = line.find("원", begin)
#         amount = line[begin:end]
#         print(",당첨금액" + numbers)
#
# if __name__=="__main__":
#     main()


# lotto.py

import requests
from bs4 import BeautifulSoup
import pymysql
import sys

# 웹 크롤링 한 결과를 저장할 리스트
from requests.models import Response

# lotto_list = []
# basic_url = "https://dhlottery.co.kr/gameResult.do?method=byWin&drwNo="


# def crawler():
#     for i in range(1, 919):
#         crawler_url = basic_url + str(i)
#         print("crawler: " + crawler_url)
#         resp = requests.get(crawler_url)
#         soup = BeautifulSoup(resp.text, "lxml")
#         line = str(soup.find("meta", {"id": "desc", "name": "description"})['content'])
#         begin = line.find("당첨번호")
#         begin = line.find(" ", begin) + 1
#         end = line.find(".", begin)
#         numbers = line[begin:end]
#         begin = line.find("총")
#         begin = line.find(" ", begin) + 1
#         end = line.find("명", begin)
#         persons = line[begin:end]
#         begin = line.find("당첨금액")
#         begin = line.find(" ", begin) + 1
#         end = line.find("원", begin)
#         amount = line[begin:end]
#         info = {}
#         info["회차"] = i
#         info["번호"] = numbers
#         info["당첨자"] = persons
#         info["금액"] = amount
#         lotto_list.append(info)
#
#
# def insert():
#     db = pymysql.connect(host="192.168.56.101", user="lotto", passwd="edu.123", db="lotto")
#     cursor = db.cursor()
#     for dic in lotto_list:
#         count = dic["회차"]
#         numbers = dic["번호"]
#         persons = dic["당첨자"]
#         amounts = dic["금액"]
#         print("insert to database at " + str(count))
#         numberlist = str(numbers).split(",")
#         sql = "INSERT INTO `lotto`. `data`(`count`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `persons`, `amounts`) VALUES('%d', '%d', '%d', '%d', '%d', '%d', '%d', '%d', '%d', '%s')" % (count, int(numberlist[0]), int(numberlist[1]), int(numberlist[2]), int(numberlist[3]), int(numberlist[4]), int(numberlist[5].split("+")[0]), int(numberlist[5].split("+")[1]), int(persons), str(amounts))
#         try:
#             cursor.execute(sql)
#             db.commit()
#         except:
#             print(sys.exc_info()[0])
#             print(sys.exc_info()[1])
#             db.rollback()
#             break
#     db.close()
#
#
# def analysis():
#     db = pymysql.connect(host="192.168.56.101", user="lotto", passwd="edu.123", db="lotto")
#     cursor = db.cursor()
#
#     myarray = [0 for i in range(46)]
#     for i in range(1, 7):
#         sql = "select `"
#         sql += str(i)
#         sql += "` from data"
#
#         try:
#             cursor.execute(sql)
#             results = cursor.fetchall()
#
            # 해당 숫자의 뽑힌 횟수를 하나씩 증가
            # for row in results:
            #     k = row[0]
            #     count = myarray[k]
            #     myarray[k] = count + 1
            #
            # print(myarray)
        # except:
        #     print(sys.exc_info()[0])
    # print(myarray[1:46])
    # cursor.close()
    # db.close()
#
#
# def main():
#     crawler()
#     insert()
#
#
# if __name__ == "__main__":
#     main()


# lotto.py

import requests
from bs4 import BeautifulSoup
import pymysql
import sys
from matplotlib import pyplot as plt

# 웹 크롤링 한 결과를 저장할 리스트
lotto_list = []

# 로또 웹 사이트의 첫 주소
main_url = "https://dhlottery.co.kr/gameResult.do?method=byWin"

# 각 회차별 당첨정보를 알 수 있는 주소
basic_url = "https://dhlottery.co.kr/gameResult.do?method=byWin&drwNo="


def getLast():
    resp = requests.get(main_url)
    soup = BeautifulSoup(resp.text, "lxml")
    line = str(soup.find("meta", {"id": "desc", "name": "description"})['content'])

    begin = line.find(" ")
    end = line.find("회")

    if begin == -1 or end == -1:
        print("not found last lotto number")
        exit()

    return int(line[begin + 1: end])


def checkLast():
    db = pymysql.connect(host="192.168.56.101", user="lotto", passwd="edu.123", db="lotto")
    cursor = db.cursor()

    sql = "SELECT MAX(count) FROM data"
    try:
        cursor.execute(sql)
        result = cursor.fetchone()
    except:
        print(sys.exc_info()[0])
    db.close()

    return (int)(result[0])


def crawler(fromPos, toPos):
    for i in range(fromPos + 1, toPos + 1):
        crawler_url = basic_url + str(i)
        print("crawler: " + crawler_url)

        resp = requests.get(crawler_url)
        soup = BeautifulSoup(resp.text, "lxml")
        line = str(soup.find("meta", {"id": "desc", "name": "description"})['content'])

        begin = line.find("당첨번호")
        begin = line.find(" ", begin) + 1
        end = line.find(".", begin)
        numbers = line[begin:end]

        begin = line.find("총")
        begin = line.find(" ", begin) + 1
        end = line.find("명", begin)
        persons = line[begin:end]

        begin = line.find("당첨금액")
        begin = line.find(" ", begin) + 1
        end = line.find("원", begin)
        amount = line[begin:end]

        info = {}
        info["회차"] = i
        info["번호"] = numbers
        info["당첨자"] = persons
        info["금액"] = amount

        lotto_list.append(info)


def insert():
    db = pymysql.connect(host="192.168.56.101", user="lotto", passwd="edu.123", db="lotto")
    cursor = db.cursor()

    for dic in lotto_list:
        count = dic["회차"]
        numbers = dic["번호"]
        person = dic["당첨자"]
        amount = dic["금액"]

        print("insert to database at " + str(count))
        numberlist = str(numbers).split(",")

        sql = "INSERT INTO `lotto`. `data`(`count`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `person`, `amount`) " \
              "VALUES('%d', '%d', '%d', '%d', '%d', '%d', '%d', '%d', '%d', '%s')" \
              % (count,
                 int(numberlist[0]),
                 int(numberlist[1]),
                 int(numberlist[2]),
                 int(numberlist[3]),
                 int(numberlist[4]),
                 int(numberlist[5].split("+")[0]),
                 int(numberlist[5].split("+")[1]),
                 int(person),
                 str(amount))
        try:
            cursor.execute(sql)
            db.commit()
        except:
            print("error, rollback")
            db.rollback()
            break
    db.close()

def analysis():
    db = pymysql.connect(host="192.168.56.101", user="lotto", passwd="edu.123", db="lotto")
    cursor = db.cursor()

    myarray = [0 for i in range(46)]
    for i in range(1, 7):
        sql = "select `"
        sql += str(i)
        sql += "` from data"

        try:
            cursor.execute(sql)
            results = cursor.fetchall()

            # 해당 숫자의 뽑힌 횟수를 하나씩 증가
            for row in results:
                k = row[0]
                count = myarray[k]
                myarray[k] = count + 1

            #print(myarray)
        except:
            print(sys.exc_info()[0])
    print(myarray[1:46])
    plt.plot(myarray[1:])
    plt.ylim(0, 140)
    plt.show()
    cursor.close()
    db.close()

def main():
    last = getLast()
    dblast = checkLast()

    if dblast < last:
        print("최신 회차는 " + str(last) + " 회 이며, 데이터베이스에는 " + str(dblast) + "회 까지 저장되어 있습니다.")
        print("업데이트를 시작합니다.")
        crawler(dblast, last)
        dblast = dblast+1
        insert()

    analysis()

if __name__ == "__main__":
    main()