from urllib.request import urlopen, Request
import json
import datetime
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = """
            Downloads the weather data from https://s3.eu-west-2.amazonaws.com/interview-question-data/metoffice/
            and saves them in fixture folder
            """

    def handle(self, **options):
        country_names = ["UK", "England", "Scotland", "Wales"]
        metrics = ["Tmax", "Tmin", "Rainfall"]
        #country_names = ["UK"]
        #metrics = ["Tmax"]
        download_path = "weather_api/fixtures"

        def myconverter(o):
            if isinstance(o, datetime.date):
                return o.__str__()

        for country in country_names:
            for metric in metrics:
                filename = "{0}_{1}.json".format(metric, country)
                req = Request("https://s3.eu-west-2.amazonaws.com/interview-question-data/metoffice/{0}-{1}.json".format(metric, country))
                print("Request")
                with urlopen(req) as response:
                    print("urlopen")
                    with open("{0}/{1}".format(download_path, filename), "w+") as outputfile:
                        result = json.loads(response.read().decode("utf-8"))
                        model_name = 'weather_api.{0}data'.format(metric)
                        load_data = []
                        for i in range(len(result)):
                            result[i]["country_name"] = "{0}".format(country)
                            #print(result[i])
                            result[i]["date_val"] = myconverter(datetime.date(result[i]["year"], result[i]["month"], 1))
                            print(result[i])
                            load_data.append({"model": model_name, "fields": result[i]})
                        #print(load_data)
                        json.dump(load_data, outputfile)
                print("{0} has been created in {1} directory.".format(filename, download_path))
