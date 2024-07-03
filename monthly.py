
import datetime
import os
import calendar
from datetime import timedelta, date
from dateutil.relativedelta import relativedelta
from calendar import monthrange

today = date.today()
date_stamp = today.replace(day=1)
"""
for delta in range(4):
    date_stamp = date_stamp + timedelta(-1)
    first_day_month = date_stamp.replace(day=1)
    last_day_month = date_stamp.replace(day=calendar.monthrange(date_stamp.year, date_stamp.month)[1])
    date_stamp = first_day_month

    first_date = first_day_month.timetuple()
    last_date = last_day_month.timetuple() 
    file_name = 'A%4d%03d%4d%03d.L3m_MO_CHL_chlor_a_4km.NRT.nc' % (first_date.tm_year, first_date.tm_yday, last_date.tm_year, last_date.tm_yday)
    print(file_name)
    #os.system('wget -nc https://oceandata.sci.gsfc.nasa.gov/ob/getfile/'+file_name+'?appkey=fb95de75edd756ef103e91b2ec74c2dda74a3f93 --no-check-certificate')
    os.system('wget -nc https://oceandata.sci.gsfc.nasa.gov/ob/getfile/AQUA_MODIS.20231001_20231031.L3m.MO.CHL.chlor_a.4km.NRT.nc?appkey=fb95de75edd756ef103e91b2ec74c2dda74a3f93 --no-check-certificate')
"""

for delta in range(6):
    date_stamp = date_stamp + timedelta(-1)
    first_day_month = date_stamp.replace(day=1)
    last_day_month = date_stamp.replace(day=calendar.monthrange(date_stamp.year, date_stamp.month)[1])
    date_stamp = first_day_month

    first_date = first_day_month.timetuple()
    last_date = last_day_month.timetuple() 
    file_name = '/home/anuj/Desktop/choloro/A%4d%03d%4d%03d.L3m_MO_CHL_chlor_a_4km.nc' % (first_date.tm_year, first_date.tm_yday, last_date.tm_year, last_date.tm_yday)
    
    first_part = str(first_date.tm_year)+""+str('%02d' % first_day_month.month)+"01"
    endmonth = monthrange(last_day_month.year, last_day_month.month)
    last_part = str(last_date.tm_year)+""+str('%02d' % last_day_month.month)+str(endmonth[1])
    file_to_download = "AQUA_MODIS."+first_part+"_"+last_part+".L3m.MO.CHL.chlor_a.4km.NRT.nc"
    print(file_to_download)
    outputfile = "/home/anuj/Desktop/choloro/"+file_to_download
    os.system('wget -nc https://oceandata.sci.gsfc.nasa.gov/ob/getfile/'+file_to_download+'?appkey=fb95de75edd756ef103e91b2ec74c2dda74a3f93 -O'+file_name+' --no-check-certificate')

