#Reading data from CDC US Births
f=open("US_births_1994-2003_CDC_NCHS.csv","r")
reader=f.read()
data=reader.split('\n')
#Displaying the first 10 rows into resulting list
print(data[0:10])

#Creating a CSV reader function to pull data easier
def read_csv(csv_name):
    opener=open(csv_name,"r")
    reader=opener.read()
    string_list=[]
    data=reader.split("\n")
    string_list=data[1:]
    final_list=[]
    for row in string_list:
        int_fields=[]
        string_fields=row.split(',')
        for item in string_fields:
            int_converter=int(item)
            int_fields.append(int_converter)
        final_list.append(int_fields)
    return final_list

cdc_list=read_csv("US_births_1994-2003_CDC_NCHS.csv")
#Checking function for first 10 rows of data
print(cdc_list[0:10])

#Create a function to calculate the births per months
def month_births(input_listoflist):
    births_per_month={}
    for row1 in input_listoflist:
        month=row1[1]
        births=row1[-1]
        if month in births_per_month:
            births_per_month[month] = births_per_month[month] + births
        else: 
            births_per_month[month]=births
    return births_per_month

cdc_list=read_csv("US_births_1994-2003_CDC_NCHS.csv")
cdc_month_births=month_births(cdc_list)
#Checking function for data accuracy
print(cdc_month_births)

'''
Creating a function to dwelve deeper into data and check the
births per day of week
'''

def dow_births(input_listoflists):
    day_of_week={}
    for row1 in input_listoflists:
        day=row1[-2]
        births=row1[-1]
        if day in day_of_week:
            day_of_week[day]=day_of_week[day] + births
        else: 
            day_of_week[day]=births
    return day_of_week

cdc_day_births=dow_births(cdc_list)
#Checking function for data accuracy
print(cdc_day_births)

'''Create a function that calculates a wide variety of totals from:
annual births, monthly births, DOM, and DOW'''

def calc_count(input_list,column):
    tot_births_value={}
    column_number=column-1
    for rows in input_list[1:]:
        if rows[column_number] in tot_births_value:
            tot_births_value[rows[column_number]]+=1
        else:
            tot_births_value[rows[column_number]]=1
    return tot_births_value

cdc_list=read_csv("US_births_1994-2003_CDC_NCHS.csv")
data=cdc_list
cdc_year_births=calc_count(data,1)
cdc_month_births=calc_count(data,2)
cdc_dom_births=calc_count(data,3)
cdc_dow_births=calc_count(data,4)
#Checking function for data accuracy
print(cdc_year_births)
print(cdc_month_births)
print(cdc_dom_births)
print(cdc_dow_births)

'''
Creating a function to calculat the MAX and MIN values of any dictionary
to check the values of each dictionary as sanity check.
'''
def maxmin_dict (dictionary):
    maxmin_result={}
    min=None
    max=None
    v_list=list(dictionary.values())
    for item in v_list:
        if max is None or item>max:
            max=item
        if min is None or item<min:
            min=item
    maxmin_result['Max']=max
    maxmin_result['Min']=min
    return maxmin_result

'''
Creating a function that extracts the same values across years and calculates the 
differences between consecutive values to show if number of births is increasing or decreasing
to see if there any possible trends.
'''

def yearchangecalc(input_list,parameter1,parameter2):
    #parameter1 is month, date_of_month, day_of_week
    if parameter1=='month':
        column_selector=1
    if parameter1=='date_of_month':
        column_selector=2
    if parameter1=='day_of_week':
        column_selector=3
    #parameter2 is what month, what date, what day
    selector=parameter2
    #print error
    if parameter1=='month' and parameter2>12:
        return 'Month does not work with parameter2.'
    if parameter1=='date_of_month' and parameter2>31:
        return 'Date of month does not work with parameter2.'
    if parameter1=='day_of_week' and parameter2>7:
        return 'Day of week does not work with parameter2.'
    if parameter2<=0:
        return 'Parameter 2 cannot be less than 1.'
    #iterate over every list of list
    annual_changes={}
    for date in input_list:
        year=date[0]
        births=date[4]
        if year in annual_changes and date[column_selector]==parameter2:
            annual_changes[year]=annual_changes[year]+births
        if year not in annual_changes and date[column_selector]==parameter2:
            annual_changes[year]=births
    return annual_changes

'''
Found new dataset that provides a more comprehensive picture of the
births from 2000 - 2014. Determine strategy to combine CDC data with
SSA data...specifically lets figure a way to deal with the overlapping
time periods in the datasets.
'''

ssa_list=read_csv('US_births_2000-2014_SSA.csv')
print(ssa_list[0:10])

#So we can see that the SSA list is conveniently the same format as the CDC list
#that we have been using before. Now we just need to create a general function that
#lets us merge these two lists and perhaps even future lists and deal with overlapping
#dates. ###If two dates overlap, we will take the average of the two births.

def list_merger(list1,list2):
  list_merger=[]
  for rows1 in list1:
    births=rows1[4]
    for rows2 in list2:
      if rows1[0]==rows2[0] and rows1[1]==rows2[1] and rows1[2]==rows2[2] and rows1[3]==rows2[3]:
        births=(rows1[4]+rows2[4])/2
    data1=[rows1[0],rows1[1],rows1[2],rows1[3],births]
    list_merger.append(data1)
  for rows2 in list2:
    births=rows2[4]
    for rows1 in list1:
      if rows1[0]!=rows2[0] and rows1[1]!=rows2[1] and rows1[2]!=rows2[2] and rows1[3]!=rows2[3]:
        data2=[rows2[0],rows2[1],rows2[2],rows2[3],births]
    list_merger.append(data2)   
  return list_merger