import os


print(os.listdir('../'), "1")

files = os.listdir('weather_api/fixtures/')
print(files)
manage = 'manage.py'


def loaddata(file):
    print(os.path.splitext(file))
    if os.path.splitext(file)[1] == '.json':
        print(file)
        os.system("python {0} loaddata {1}".format(manage, file))


for file in files:
    loaddata(file)
