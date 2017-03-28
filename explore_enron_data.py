#coding:utf-8
#!/usr/bin/python
""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""
#位置udacity ml 数据集与问题 25/35
import pickle
#加载数据
enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))
#要找的人名
lis =['Lay','Skilling','Fastow']
#由于数据集人名是大写的，所以全转化成大写
lis = map(lambda x:x.upper(),lis)
#把这三个人的人名和数据同时存到pay这个列表里
pay=[]
for x in enron_data:
    if x[0:x.find(' ')] in lis:
        pay.append ((x[0:x.find(' ')],enron_data[x]['total_payments'])) 

#排序，输出根据payment排序结果的最大值
pay = sorted(pay,key=lambda x:x[1],reverse=1)
print pay[0]            
