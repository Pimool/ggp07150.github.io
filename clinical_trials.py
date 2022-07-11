import pandas as pd
import json
import os

path = 'C:/Users/CRS-P-135/Desktop/AllAPIJSON'

NCTID, Sponsor, Study_Country, Phase, Study_date_first, Study_date_last = [], [], [], [], [], []

dir_list = os.listdir(path)
dir_list.remove('Contents.txt')
for dir in dir_list:
    json_list = os.listdir(f'{path}/{dir}')

    for json_path in json_list:
        try :
            with open(f'{path}/{dir}/{json_path}') as f:
                json_data = json.load(f)
        except :
            with open(f'{path}/{dir}/{json_path}', encoding = 'utf-8') as f:
                json_data = json.load(f)

        #NCTID
        print(NCTID)
        NCTID.append(json_data['FullStudy']['Study']['ProtocolSection']['IdentificationModule']['NCTId'])
        #Sponsor
        try :
            Sponsor.append(json_data['FullStudy']['Study']['ProtocolSection']['SponsorCollaboratorsModule']['LeadSponsor']['LeadSponsorName'])
        except KeyError:
            Sponsor.append('')
        #Study Location_Country
        try :
            Study_Country.append(json_data['FullStudy']['Study']['ProtocolSection']['ContactsLocationsModule']['LocationList']['Location'][0]['LocationCountry'])
        except KeyError:
            Study_Country.append('')
        #Phase
        try :
            Phase.append(json_data['FullStudy']['Study']['ProtocolSection']['DesignModule']['PhaseList']['Phase'])
        except KeyError:
            Phase.append('')
        # First_Study_day
        Study_date_first.append(json_data['FullStudy']['Study']['ProtocolSection']['StatusModule']['StudyFirstSubmitDate'])
        # Last_Study_day
        Study_date_last.append(json_data['FullStudy']['Study']['ProtocolSection']['StatusModule']['LastUpdateSubmitDate'])

df = pd.DataFrame(zip(NCTID, Sponsor, Study_Country, Phase, Study_date_first, Study_date_last), columns = ['NCTID', 'Sponsor', 'Study_Country', 'Phase', 'Study_date_first', 'Study_date_last'])

print(df)