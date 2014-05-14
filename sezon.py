import urllib2
import re
import hashlib, datetime, os
import libxml2dom, threading
import csv

stats = dict()
l_meczy = dict()
wygrane = dict()

SEZON = '08'

def my_round(x):
	if x <= 1:
		return round(x,3)
	else:
		return round(x,1)
		
		
def wypisz():
	for k, v in stats.iteritems():
		s = [ (x/l_meczy[k]) for x in v]
		print k, l_meczy[k], wygrane[k]
		s2 = [my_round(x) for x in s]
		print s2

def wczytaj():
	nazwa_pliku = 'przed' + SEZON + '.dat'
	f = open(nazwa_pliku, 'rb')
	#f = open('przed08.dat', 'rb')
	x = f.read()
	f.close()
	lines = x.split("\n")
	lines.pop()
	for i in range(len(lines)):
		akt = lines[i].split(', ')
		akt.pop()
		
		name = akt[0]
		l_meczy[name] = float(akt[1])
		wygrane[name] = float(akt[2])		
		
		del akt[0:3]
		s = [float(x) for x in akt]
		stats[name] = s
		
	#print stats
	#print lines
	
def inicjuj():
	f = open('przed06.dat', 'rb')
	x = f.read()
	f.close()
	lines = x.split("\n")
	lines.pop()
	for i in range(len(lines)):
		akt = lines[i].split(', ')
		akt.pop()
		
		name = akt[0]
		l_meczy[name] = 0.0
		wygrane[name] = 0.0		
		
		del akt[0:3]
		s = [0.0 for x in akt]
		stats[name] = s

def symuluj():
	nazwa_pliku = 'sezon' + SEZON + '.dat'
	f = open(nazwa_pliku, 'rb')
	#f = open('sezon08.dat', 'rb')
	x = f.read()
	f.close()
	lines = x.split("\n")
	lines.pop()
	for i in range(len(lines)):
	#for i in range(2):
		akt = lines[i].split(', ')
		akt.pop()
		#print akt
		home = akt[1]
		away = akt[2]
		s_home = akt[3:21]
		s_away = akt[21:]
		
		#del s_home[11]
		#for i in range(6):
		#	s_home.pop(11)
		#	s_away.pop(11)
		#for i in range(3):
		#	pomoc = s_home[11].split('-');
		#	statystyki.append(float(pomoc[0]));
		#	statystyki.append(float(pomoc[1]));
		
		wynik = s_home.pop(0)  #wynik 'W' albo 'L'
		s_away.pop(0)          #

		s_home.pop(0)  # minuty
		s_away.pop(0)  #
		
		sh = []
		sa = []
		
		for j in range(len(s_home)):
			if j not in (9, 10, 11, 12, 13, 14):
				sh.append(float(s_home[j]))
			if j in (9, 11, 13):
				pomoc = s_home[j].split('-');
				#print pomoc;
				sh.append(float(pomoc[0]));
				sh.append(float(pomoc[1]));
			
		for j in range(len(s_away)):
			if j not in (9, 10, 11, 12, 13, 14):
				sa.append(float(s_away[j]))
			if j in (9, 11, 13):
				pomoc = s_away[j].split('-');
				#print pomoc;
				sa.append(float(pomoc[0]));
				sa.append(float(pomoc[1]));
		
		for j in range(len(sa)):
			sh.append(sa[j]);
		
		for j in range(len(sh)):
			sa.append(sh[j]);
		
		
		#print sh;
		#print sa;
		
		
		
		if l_meczy[home]>0 and l_meczy[away]>0:
		
			srednie_home = [round(x/l_meczy[home], 1) for x in stats[home]]
			srednie_away = [round(x/l_meczy[away], 1) for x in stats[away]]
		
			#print home, l_meczy[home], wygrane[home], srednie_home
			#print away, l_meczy[away], wygrane[away], srednie_away
			#print wynik, sh[0], sa[0]
			#print
		
		
			print wygrane[home],
			fin.write(str(wygrane[home]))
			fin.write(' ');
			for i in range(len(srednie_home)):
				print srednie_home[i],
				fin.write(str(srednie_home[i]))
				fin.write(' ')
			print 
			fin.write('\n')
			
		
			print wygrane[away],
			fin.write(str(wygrane[away]))
			fin.write(' ');
			for i in range(len(srednie_away)):
				print srednie_away[i],
				fin.write(str(srednie_away[i]))
				fin.write(' ')
			print 
			fin.write('\n')
		
		
			print wynik, sh[0], sa[0]
			fout.write(str(sh[0]) + ' ' + str(sa[0]) + '\n')
		
		#tab = [round(x/y,2) for x in sh for y in sa]
		#print tab
			
		if not home in l_meczy:
			l_meczy[home] = 0
			wygrane[home] = 0
		l_meczy[home] += 1
		
		if not away in l_meczy:
			l_meczy[away] = 0
			wygrane[away] = 0
		l_meczy[away] += 1
		
		if wynik=='W':
			wygrane[home] += 1
		else:
			wygrane[away] += 1
			
		if not home in stats:
			stats[home] = sh
		else:
			for j in range(len(stats[home])):
				stats[home][j] += sh[j]
				
		if not away in stats:
			stats[away] = sa
		else:
			for j in range(len(stats[away])):
				stats[away][j] += sa[j]
				
	


nazwa_input  = 'wejscie' + SEZON + '.dat'
nazwa_output = 'wyjscie' + SEZON + '.dat'

fin  = open(nazwa_input,  'w')
fout = open(nazwa_output, 'w')

wczytaj()
#inicjuj()
#wypisz()
symuluj()
#wypisz()

fin.close()
fout.close()
