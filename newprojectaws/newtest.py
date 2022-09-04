from importlib.resources import Resource
import boto3

resource=boto3.resource('s3')
list_=resource.buckets.all()
for buckets in list_:
    print(buckets.name)
for my_bucket_object in resource.objects.all():
    print(my_bucket_object)