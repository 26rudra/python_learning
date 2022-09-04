import boto3
import time
import datetime
import random

while True:  
        time.sleep(10)
        resource=boto3.resource("s3")
       
        
       
        ts=time.time()
       
        bucket=resource.Bucket(f"mynewbucket{ts}")
        response = bucket.create(
            ACL='public-read-write',
            CreateBucketConfiguration={
                'LocationConstraint': 'ap-south-1'
        },)
        s=random.randint(0,10)
        with open('/newprojectaws', 'w') as data:
            resource.Bucket(f'mynewbucket{ts}').upload_file('/newprojectaws', f'newfile{s}')


    
   

  
 
