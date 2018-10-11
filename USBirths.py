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
to check the values of each dictionary as sanity check
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