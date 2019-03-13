from django.shortcuts import render
from .models import RainfallData, TminData, TmaxData
from django.http import HttpResponse
import json
# Create your views here.


def view_data(request):
    start_date = request.GET.get('start_date')
    start_date_query = start_date + '-01'
    end_date = request.GET.get('end_date')
    end_date_query = end_date + '-01'
    metric = request.GET.get('metric')
    country = request.GET.get('country')

    # fetch values according to metric
    #    filter according to country

    if metric.lower() == 'rainfall':
        queryset_country = RainfallData.objects.filter(country_name=country)

    elif metric.lower() == 'tmax':
        queryset_country = TmaxData.objects.filter(country_name=country)

    elif metric.lower() == 'tmin':
        queryset_country = TminData.objects.filter(country_name=country)
    # filter according to the start_date and end_date provided
    queryset_1 = queryset_country.filter(
                                    date_val__range=(
                                        start_date_query, end_date_query
                                                     )
                                        ).order_by('date_val').values()
    result_dict = {}
    # store as "year-month": "value"
    for i in queryset_1:
        if i['month'] >= 10:
            new_date = (str(i['year']) + "-" + str(i['month']))
        else:
            new_date = (str(i['year']) + "-0" + str(i['month']))
        result_dict[new_date] = i['value']
    # print(result_dict)
    queryset_dump = json.dumps(result_dict)
    return HttpResponse(queryset_dump, content_type='application/json')
