import os, sys
import pandas as pd
from azure.storage.blob import BlockBlobService, PublicAccess, ContainerPermissions


def usqlml_main(df):
    res = df.append({'Name' : 'Sahil' , 'Age' : 22} , ignore_index=True)
    return res.astype(str)


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
      if blob.name.lower().endswith('.csv'):
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


def process_csv(file_name):
  try:
    df = pd.read_csv(file_name, sep=';')
    rst = usqlml_main(df)
    rst.to_csv('result_'+file_name, sep=';',index=False)
    return 'result_'+file_name
  except Exception as e:
    raise e


def run(account_name, container_name, sas_token, folder_name):
  try:
    file_name = download_file(
        account_name, container_name, sas_token, folder_name)
    if file_name != None:
      result_file = process_csv(file_name)
      if result_file != None:
        upload_file(account_name, container_name,
                    sas_token, folder_name, result_file)
    sys.stdout.write("Job is completed with file name " + result_file)
    sys.stdout.flush()
  except Exception as e:
    sys.stdout.write("Job is failed with exception")
    sys.stdout.write(e)
    sys.stdout.flush()


def start():
  account_name = os.environ['ACCOUNTNAME']
  container_name = os.environ['CONTAINERNAME']
  sas_token = os.environ['SASTOKEN']
  folder_name = os.environ['FOLDERNAME']
  ex = os.environ['EXCEPTION']
  
  if ex == "True":
    raise ValueError('oops!')
    os._exit(0)

  if account_name != None and container_name != None and sas_token != None and folder_name != None:
    run(account_name, container_name, sas_token, folder_name)


if __name__ == '__main__':
    start()
