from urllib.request import urlretrieve

url = 'https://raw.githubusercontent.com/mohamedsiika/Football_Transfer/main/Summer_transfer_window_2022.csv'

urlretrieve(url,'transfers.csv')
