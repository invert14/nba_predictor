import urllib2
import re
import hashlib, datetime, os
import libxml2dom, threading
import pickle

LICZBA_DRUZYN = 30
SEZON = '08'
	

def wczytajDruzyny():
	#inicjujDruzyny()
	for i in range(LICZBA_DRUZYN):
		#print "http://www.hoopsstats.com/basketball/fantasy/nba/cos/team/profile/{}/{}/1-7-1".format(SEZON, (i+1))
		f = urllib2.urlopen("http://www.hoopsstats.com/basketball/fantasy/nba/cos/team/profile/{}/{}/1-7-1".format(SEZON, (i+1)))
		s = f.read()
		f.close();
		dom = libxml2dom.parseString(s, html=1)
		home = dom.xpath('.//title/text()')
		home = home[0].toString()
		name = home[0:home.index(' NBA')]
		
		lista_dom = dom.xpath('.//table[@class="statscontent"]')
				
		statystyki = []
			
		for nr in (2,3):
			
			
			aktMecz_dom = lista_dom[nr]
			statystyki_dom = aktMecz_dom.xpath('.//td//center/text()')
			for i in range(len(statystyki_dom)):
				if i in (12,14,16):
					pomoc = statystyki_dom[i].toString().split('-');
					statystyki.append(float(pomoc[0]));
					statystyki.append(float(pomoc[1]));
				if i not in (2,12,13,14,15,16,17):
					statystyki.append(float(statystyki_dom[i].toString()))
					
		statystyki.pop(18);			
		statystyki.pop(18);
		
		print name + ',',
		for	i in range(len(statystyki)):
			print str(statystyki[i])+',',
		print ''
				

wczytajDruzyny()
