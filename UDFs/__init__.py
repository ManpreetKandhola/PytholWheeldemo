from function1 import stringLength
from function2 import stringToUpper
from function1 import get_service_client_sas, create_directory

some_string = "Hello, Universe!"
sas_token = "?sv=2022-11-02&ss=bfqt&srt=sco&sp=rwdlacupyx&se=2023-10-02T14:56:19Z&st=2023-10-02T06:56:19Z&spr=https&sig=ct2yz18En%2FwNL0IzqSaL8dmYMBJuh45l2Nt72hek%2Fs8%3D"

print(stringLength(some_string))
print(stringToUpper(some_string))
print(get_service_client_sas(any,"waphadlprod001",sas_token))
