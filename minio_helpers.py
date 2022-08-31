from minio import Minio
from minio.error import S3Error

def getMinioClient():
    client = Minio(
        f'localhost:9000',
        access_key='voQhnSTDPz992mXC',
        secret_key='9HM93xMWuW8qf7f5Wbhm0YfOckYNDHE1',
        secure=False
    )
    return client

def getDatabaseFile():
    minio = getMinioClient()

    bucket_name = 'beersite'
    object_name = 'database.sqlite'
    file_path = './database.sqlite'
    
    minio.fget_object(bucket_name, object_name, file_path)
