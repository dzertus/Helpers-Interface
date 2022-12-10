import requests



def download_file(url, path):
    myfile = requests.get(url)
    open(path, 'wb').write(myfile.content)