import urllib2
import re
import hashlib, datetime, os
import libxml2dom, threading
import pickle

LICZBA_DRUZYN = 30
SEZON = '06'

druzyny_slownik = {
'Indiana' : 'Indiana Pacers',
'Boston' : 'Boston Celtics',
'Dallas' : 'Dallas Mavericks',
'New Jersey' : 'New Jersey Nets',	  	
'Houston':'Houston Rockets',
'New York':'New York Knicks',
'Memphis':'Memphis Grizzlies',
'Philadelphia':'Philadelphia 76ers', 		  	
'New Orleans':'New Orleans Hornets',
'Toronto':'Toronto Raptors',
'San Antonio':'San Antonio Spurs',
'Chicago':'Chicago Bulls',
'Denver':'Denver Nuggets',
'Cleveland':'Cleveland Cavaliers',
'Minnesota':'Minnesota Timberwolves',
'Detroit':'Detroit Pistons', 		  	
'Portland':'Portland Trail Blazers',
'Oklahoma City':'Oklahoma City Thunder',
'Seattle':'Seattle Supersonics',
'Milwaukee':'Milwaukee Bucks', 		  	
'Utah':'Utah Jazz',
'Atlanta':'Atlanta Hawks', 		  	
'Golden State':'Golden State Warriors',
'Charlotte':'Charlotte Bobcats', 		  	
'L.A.Clippers':'Los Angeles Clippers',
'Miami':'Miami Heat', 		  	
'L.A.Lakers':'Los Angeles Lakers',
'Orlando':'Orlando Magic', 		  	
'Phoenix':'Phoenix Suns',
'Washington':'Washington Wizards', 		  	
'Sacramento':'Sacramento Kings'}

miesiace = {
'Sep' : 1,
'Oct' : 2,
'Nov' : 3, 
'Dec' : 4,
'Jan' : 5,
'Feb' : 6, 
'Mar' : 7,
'Apr' : 8,
'May' : 9 }

		
dh = dict()
da = dict()

def wczytajDruzyny():
	#inicjujDruzyny()
	for i in range(LICZBA_DRUZYN):
		print "http://www.hoopsstats.com/basketball/fantasy/nba/cos/team/schedule/{}/{}/1-1-7".format(SEZON, (i+1))
		f = urllib2.urlopen("http://www.hoopsstats.com/basketball/fantasy/nba/cos/team/schedule/{}/{}/1-1-7".format(SEZON, (i+1)))
		s = f.read()
		f.close();
		dom = libxml2dom.parseString(s, html=1)
		home = dom.xpath('.//title/text()')
		home = home[0].toString()
		name = home[0:home.index(' NBA')]
		
		
		lista_dom = dom.xpath('.//table[@class="statscontent"]')
		
		lista = []
		daty = []
		
		for nrMeczu in range(len(lista_dom)):
		#for nrMeczu in range(2):
			#for nrMeczu in [0]:
			
			statystyki = []
			
			aktMecz_dom = lista_dom[nrMeczu]
			statystyki_dom = aktMecz_dom.xpath('.//td//center/text()')
			for i in range(len(statystyki_dom)):
				statystyki.append(statystyki_dom[i].toString())
			data = aktMecz_dom.xpath('.//td[1]/text()')
			data = data[0].toString()
			#away = aktMecz_dom.xpath('
			
			w_domu = 0
			
			gdzie = aktMecz_dom.xpath('.//td[2]/a/text()')
			if (len(gdzie)>0):
				gdzie = gdzie[0].toString()
				miejsce = gdzie[3:]
				away = druzyny_slownik[miejsce]
				#print 'HOME   ' + away
				w_domu = 1
			
			gdzie = aktMecz_dom.xpath('.//td[2]/a/b/text()')			
			if (len(gdzie)>0):
				gdzie = gdzie[0].toString()
				miejsce = gdzie[3:]
				away = druzyny_slownik[miejsce]
				#print '   AWAY   ' + away
				w_domu = 0
			
			lista.append(statystyki);
			daty.append(data)
			
			if w_domu == 1:				
				dh[(name,data)] = []
				dh[(name,data)].append(away)
				dh[(name,data)].append(statystyki)
			else:				
				da[(away,data)] = []
				da[(away,data)].append(name)
				da[(away,data)].append(statystyki)
			
			#druzyny[name].mecze[data] = statystyki
			#print(cos.toString())
			
			
		#for nr in range(82):
			#print daty[nr]
			#for i in range(len(lista[nr])):
				#print lista[nr][i],
				##druzyny[name].statystyki[	
			#print ''
		

wczytajDruzyny()

#print dh
#print da

dm = dict()

for k, v in dh.iteritems():
	if not k[1] in dm:
		dm[k[1]] = []
	dm[k[1]].append(k[0])
	dm[k[1]].append(v[0])
	dm[k[1]].append(v[1])
	dm[k[1]].append(da[k][1])
	
	
#print dh['Boston Celtics', 'Feb 9']
#print da['Boston Celtics', 'Feb 9']
#print dm['Mar 14']


#print dm

lista = []

for k, v in dm.iteritems():
	for i in (range(len(v)/4)):
		pom = []
		pom.append(k)
		pom.append(v[4*i])
		#print 'k = ', k
		#print 'v = ',  v
		pom.append(v[4*i+1])
		pom.append(v[4*i+2])
		pom.append(v[4*i+3])
		lista.append(pom);
	
def comparator(x, y):
	m1 = miesiace[x[0].split()[0]]
	d1 = int(x[0].split()[1])
	m2 = miesiace[y[0].split()[0]]
	d2 = int(y[0].split()[1])
	
	#print m1, d1, m2, d2
	
	if m1 != m2:
		return m1-m2
	else:
		return d1-d2	
	
lista.sort(comparator)

for i in range(len(lista)):
	print lista[i][0] + ',',
	print lista[i][1] + ',',
	print lista[i][2] + ',',
	for j in range(len(lista[i][3])):
		print lista[i][3][j] + ',',
	for j in range(len(lista[i][4])):
		print lista[i][4][j] + ',',
	print ''

#for k, v in druzyny.iteritems():
	#v.wypisz()
	



	


