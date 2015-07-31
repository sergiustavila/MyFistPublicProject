#!/usr/bin/pyton
import sys
from datetime import datetime
aaa=sys.argv[1]
if len(sys.argv)==2:
	t=datetime.now()
	bbb=t.strftime("%d/%m/%Y")	
else:
	bbb=sys.argv[2]
def countDays(aa=aaa,bb=bbb):
	myFormat="%d/%m/%Y"
	date1=aa
	date2=bb
	a=datetime.strptime(date1,myFormat)
	b=datetime.strptime(date2,myFormat)
	nrDays=abs(b-a)
	print nrDays.days
countDays ()

