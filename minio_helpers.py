from minio import Minio
from minio.error import S3Error
from minio_secrets import *

def getMinioClient():
    print(access_key)
    client = Minio(
        f'localhost:9000',
        access_key=access_key,
        secret_key=secret_key,
        secure=False
    )
    return client

def getDatabaseFile():
    minio = getMinioClient()

    bucket_name = 'beersite'
    object_name = 'database.sqlite'
    file_path = './database.sqlite'
    
    minio.fget_object(bucket_name, object_name, file_path)
