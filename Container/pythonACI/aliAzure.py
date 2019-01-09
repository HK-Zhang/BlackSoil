import os, sys
from azure.storage.blob import BlockBlobService, PublicAccess, ContainerPermissions
import time


def normailize_folder(folder_name):
  if folder_name.endswith('/'):
    return folder_name
  return folder_name+'/'


def download_file(account_name, container_name, sas_token, folder_name):
  try:
    block_blob_service = BlockBlobService(
        account_name=account_name, account_key=None, sas_token=sas_token)

    folder_name = normailize_folder(folder_name)
    generator = block_blob_service.list_blobs(container_name, folder_name)
    for blob in generator:
      if blob.name.lower().endswith('azureblob.csv'):
        file_name = blob.name.split('/')[-1]
        block_blob_service.get_blob_to_path(
            container_name, blob.name, file_name)
        return file_name
  except Exception as e:
    raise e
  return None


def upload_file(account_name, container_name, sas_token, folder_name, file_name):
  try:
    block_blob_service = BlockBlobService(
        account_name=account_name, account_key=None, sas_token=sas_token)

    folder_name = normailize_folder(folder_name)
    block_blob_service.create_blob_from_path(
        container_name, folder_name + file_name, file_name)
  except Exception as e:
    raise e

def run(account_name, container_name, sas_token, folder_name):
  try:
    time_start=time.time()
    file_name = download_file(
        account_name, container_name, sas_token, folder_name)
    time_end=time.time()
    print time_end-time_start
  except Exception as e:
    sys.stdout.write("Job is failed with exception")
    sys.stdout.write(e)
    sys.stdout.flush()

def runUpload(account_name, container_name, sas_token, folder_name, file_name):
  try:
    time_start=time.time()
    upload_file(
        account_name, container_name, sas_token, folder_name, file_name)
    time_end=time.time()
    print time_end-time_start
  except Exception as e:
    sys.stdout.write("Job is failed with exception")
    sys.stdout.write(e)
    sys.stdout.flush()

def start():
  account_name = "aspreactstorage"
  container_name = "2018demo"
  sas_token = "*"
  folder_name = "pythontest/"
  file_name = "azureblob1.csv"
  if account_name != None and container_name != None and sas_token != None and folder_name != None:
      runUpload(account_name, container_name, sas_token, folder_name,file_name)
    # run(account_name, container_name, sas_token, folder_name)


if __name__ == '__main__':
    start()
