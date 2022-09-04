from asyncio.windows_events import NULL
from http import client
from importlib.resources import Resource
from re import X


import boto3
import time
import datetime
import random
import botocore
resource = boto3.resource('s3') 
response = resource.buckets.all()
for bucket in response:
    # print(bucket.name)
    N=bucket.name
    my_bucket=resource.Bucket(bucket.name)
    # response= resource.list_objects_v2(bucket.name)
    
    # list_=(map(lambda x: (x.bucket_name, x.key), my_bucket.objects.all()))
    # listkeys=my_bucket.bucket_name()
    
    # print(listkeys)
    for keys in resource.Object.all():
       list_= (keys.bucket_name)
       
for keys in response :
    list_2=(keys.name)  
    print(list_2)
    # for i in list_:
    #     print(i)
    # list_=filter(None,list(list_))
for i in list_2:    
    if i not in  list_:
        bucket=response.Bucket("nonamebuckt9898")
        response = bucket.delete()
  
    # print(list_)
    # else:
    #     my_bucket.delete_bucket(list_[0])   
    #      
   
    # # list2=list(filter(None,list_)) 
    # for i in list_:
    #     if len(list_)<1: 
    #         continue
            # my_bucket.delete_bucket(list2[0])
            # if my_bucket.all()
        # else:
        #     print(list_[0])

