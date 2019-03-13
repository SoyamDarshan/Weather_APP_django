# Weather_APP_django
Django implementation of a weather app

### Models

This has a models for each metric Rainfall, Tmax, Tmin.

Each model have common fields like Country, Value, Year, Month and Date_Val.

### Views

Here the GET request is being handled, a successful request will fetch the data in JSON format.

request should be sent along with parameters like
start_date
end_date
metric
country

All the fields are mandatory for a successful query.

## To run the app

Requirements : Django should be installed in the workstation.

### To run the server

```python manage.py runserver```

### To download weather data

```python manage.py download_weather_data```

### To load the data into the data models

```python weather_api/management/scripts/load_data_script.py```





## Future improvements

Handle the data by having a single model store data for all the fields.
Handle the url in a better way.
Work on creating templates for the display pages.



