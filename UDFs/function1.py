import os
from azure.storage.filedatalake import DataLakeDirectoryClient,DataLakeFileClient, DataLakeServiceClient,FileSystemClient
from azure.identity import DefaultAzureCredential


sas_token = "?sv=2022-11-02&ss=bfqt&srt=sco&sp=rwdlacupyx&se=2023-10-02T14:56:19Z&st=2023-10-02T06:56:19Z&spr=https&sig=ct2yz18En%2FwNL0IzqSaL8dmYMBJuh45l2Nt72hek%2Fs8%3D"

def stringLength(inStr):
    return len(inStr)


def get_service_client_sas(self, account_name: str, sas_token: str) -> DataLakeServiceClient:
    account_url = f"https://{account_name}.dfs.core.windows.net"
    # The SAS token string can be passed in as credential param or appended to the account URL
    service_client = DataLakeServiceClient(account_url, credential=sas_token)
    return service_client

service_client = get_service_client_sas(any,"waphadlprod001",sas_token)

def create_directory(self, file_system_client: FileSystemClient, directory_name: str) -> DataLakeDirectoryClient:
    directory_client = file_system_client.create_directory(directory_name)
    return directory_client

file_system_client = service_client.get_file_system_client("bronze")
print(file_system_client)

directory_client = create_directory(any,file_system_client,"Test/ManpreetTest/MKTestfolder")

def upload_file_to_directory(self, directory_client: DataLakeDirectoryClient, local_path: str, file_name: str):    
    file_client = directory_client.get_file_client(file_name)    
    with open(file=os.path.join(local_path, file_name), mode="rb") as data:
        file_client.upload_data(data, overwrite=True)

local_path = "C:\Users\manpreet.kandhola\Downloads"
file_name = "test.txt"

upload_file_to_directory(any,directory_client,local_path,file_name)
# upload_file_to_directory(any,directory_client)