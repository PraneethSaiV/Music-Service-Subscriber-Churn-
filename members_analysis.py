#import os
#os.chdir('/media/vsppraneeth/01D3522569C0B1A0/WSDM')

import pandas as pd
import numpy as np

members = pd.read_csv('members.csv')

members['registration_init_time'] = pd.to_datetime(members['registration_init_time'],format = '%Y%m%d')
members['expiration_date'] = pd.to_datetime(members['expiration_date'],format = '%Y%m%d') 
members['msno'] = members['msno'].astype(str)
members['city'] = members['city'].astype('category')
members['gender'] = members['gender'].astype('category')
members['registered_via'] = members['registered_via'].astype('category')

# Fixing bad values
members.loc[(members['bd'] > 100) | (members['bd'] < 0), 'bd'] = np.mean(members['bd'].loc[(members['bd'] < 100) & (members['bd'] > 0)])
sum(members['gender'].isnull()) # what do I do about this?

members.to_csv('out_mem.csv')
