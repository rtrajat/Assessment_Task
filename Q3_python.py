from csv import DictReader
from collections import defaultdict
import operator
FCT_ORDERS_csvfile=open(r'C:\Users\asus\Downloads\FCT_ORDERS.csv', 'r', encoding='utf-8-sig')
DIM_VENDORS_csvfile=open(r'C:\Users\asus\Downloads\DIM_VENDORS.csv', 'r', encoding='utf-8-sig')
reader = list(DictReader(FCT_ORDERS_csvfile))
vendor_id = []
amt =[]
# filtering out records with non-successful orders
for row in reader:
    if row['STATUS']!='0':
        vendor_id.append(row['VENDOR_ID'])
        amt.append(row['AMT'])
res = list(zip(vendor_id,amt))
#peforming groupby on vendor id
dict_group=defaultdict(list)
for i in res:
    key=i[0]
    value=i[1]
    dict_group[key].append(int(value))
# summing up amount of each vendor
amount_sum={}
for k,v in dict_group.items():
    amount_sum[k]=sum(v)
#getting top 3 vendors based on amout
sorted_amount = sorted(amount_sum.items(), key=operator.itemgetter(1))[0:3]
reqd_vendor=[]
for i in sorted_amount:
    reqd_vendor.append(i[0])
# fetching out vendor type from Vendors table by using vendor id
vendor_reader=list(DictReader(DIM_VENDORS_csvfile))
vendor_id_type=[]
for row in vendor_reader:
    for i in reqd_vendor:
        if i==row['ID']:
            vendor_id_type.append(str(row['ID']+','+row['TYPE']))
print(vendor_id_type)

    