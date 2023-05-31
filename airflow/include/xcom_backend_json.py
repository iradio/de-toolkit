from airflow.models.xcom import BaseXCom
import json
import uuid
from minio import Minio
import os
import io

XCOM_BUCKET_NAME = str(os.environ['XCOM_BUCKET_NAME'])

class CustomXComBackendJSON(BaseXCom):
    # the prefix is optional and used to make it easier to recognize
    # which reference strings in the Airflow metadata database
    # refer to an XCom that has been stored in a MinIO bucket
    PREFIX = "xcom_minio://"
    BUCKET_NAME = XCOM_BUCKET_NAME

    @staticmethod
    def serialize_value(
        value,
        key=None,
        task_id=None,
        dag_id=None,
        run_id=None,
        map_index= None,
        **kwargs
    ):
        
        
        # create the MinIO client with the credentials stored as env variables
        client = Minio(
            # f"{os.environ['MINIO_IP']}:{os.environ['MINIO_PORT']}",
            os.environ['MINIO_IP'],
            os.environ["MINIO_ACCESS_KEY"],
            os.environ["MINIO_SECRET_KEY"],
            secure=False
        )

        # make sure the file_id is unique, either by using combinations of
        # the task_id, run_id and map_index parameters or by using a uuid
        filename = "data_" + str(uuid.uuid4()) + ".json"
        # define the full key where the file should be stored
        minio_key = f"{run_id}/{task_id}/{filename}"

        # write the value to MinIO
        client.put_object(
            CustomXComBackendJSON.BUCKET_NAME,
            minio_key,
            io.BytesIO(bytes(json.dumps(value), 'utf-8')),
            -1, # -1 = unknown file size
            part_size=10*1024*1024,
        )

        # define the string that will be saved to the Airflow metadata 
        # database to refer to this XCom
        reference_string = CustomXComBackendJSON.PREFIX + minio_key

        # use JSON serialization to write the reference string to the
        # Airflow metadata database (like a regular XCom)
        return BaseXCom.serialize_value(value=reference_string)

    @staticmethod
    def deserialize_value(result):
        # retrieve the relevant reference string from the metadata database
        reference_string = BaseXCom.deserialize_value(result=result)

        # retrieve the key from the reference string 
        minio_key = reference_string.replace(CustomXComBackendJSON.PREFIX, "")

        # create the MinIO client with the credentials stored as env variables
        client = Minio(
            # f"{os.environ['MINIO_IP']}:{os.environ['MINIO_PORT']}",
            os.environ['MINIO_IP'],
            os.environ["MINIO_ACCESS_KEY"],
            os.environ["MINIO_SECRET_KEY"],
            secure=False
        )

        # get the object from the MinIO bucket
        response = client.get_object(
            CustomXComBackendJSON.BUCKET_NAME,
            minio_key
        )

        # return the contents of the retrieved object
        return json.loads(response.read())