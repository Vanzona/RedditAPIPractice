CLIENT_ID = 'UWaCDLkHhE6t0qQF7B9JJQ'
CLIENT_SECRET = 'jEm98gbmIlA8aYNXI5EULdR_eWlKSg'
import pandas
from openpyxl import load_workbook
import requests.auth

client_auth = requests.auth.HTTPBasicAuth(CLIENT_ID, CLIENT_SECRET)
data = {
    'grant_type': 'password',
    'username': 'chunkylver99',
    'password': 'MonkeyPrimus123$'
}

headers = {'User-Agent': 'PEEP/0.0.1'}
auth = requests.post('https://www.reddit.com/api/v1/access_token', data=data, headers=headers, auth = client_auth)
if auth.status_code == 200:
    print("nice")
    print(auth.json())
    token_id = auth.json()['access_token']

if token_id == 'null':
    print("NO VALUE")

OAUTH_ENDPOINT = 'https://oauth.reddit.com'

get_param = {
    'limit': 10,
}
headers_get = {
    'User-Agent': 'PEEP/0.0.1',
    'Authorization': 'Bearer ' + token_id
}
response1 = requests.get(OAUTH_ENDPOINT + '/r/poppunkers/hot/', headers =headers_get, params=get_param)

print(response1.status_code)
print(response1.json())

data = response1.json()
posts = data['data']['children']
after_key = data['data']['after']
before_key = data['data']['before']

df = pandas.DataFrame(posts)

# Create a Pandas Excel writer using XlsxWriter as the engine.
writer = pandas.ExcelWriter('C:\\Users\\Ian\\Documents\\Book1.xlsx', engine='openpyxl')
# Convert the dataframe to an XlsxWriter Excel object.
df.to_excel(writer, index= False, columns= 'A1', sheet_name='Sheet1')



# Close the Pandas Excel writer and output the Excel file.
writer.save()
