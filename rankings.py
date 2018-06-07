from bs4 import BeautifulSoup as soup
from requests import get
import os

url = 'http://www.fifa.com/fifa-world-ranking/ranking-table/men/'

#opening the connection and grabbing the page
response = get(url)

#html parser
html = soup(response.text, "html.parser")

ranking = html.select('.ranking')
print '\n'
print 'Rank \t',
print 'Team \t\t\t',
print 'Point \t\t',
print 'Pre Point \t\n'

try:
    for ranks in ranking:
        table = ranks.findAll('table',attrs={'class','tbl-ranking'})
        for tb in table:
            tbody = tb.select('tbody')
            for tbo in tbody:
                t = tbo.findAll('tr',attrs={'class','anchor'})
                for td in t:
                    ranks = td.findAll('td',attrs={'class','tbl-rank'})
                    for rank in ranks:
                        print rank.text + '\t',
                    teams = td.findAll('td',attrs={'class','tbl-teamname'})
                    #print team.text
                    for name in teams:
                        aTag = name.findAll('a')
                        for a in aTag:
                            MAX = 22
                            MIN = len(a.text)
                            diff = MAX - MIN
                            print a.text,
                            while diff > 0:
                                print '',
                                diff = diff - 1
                    points = td.findAll('td',attrs={'class','tbl-points'})
                    for point in points:
                        print point.text + '\t',
                    pre_points = td.findAll('td',attrs={'class','tbl-prevpoints'})
                    for pre in pre_points:
                        print pre.text
except Exception:
    print ''
