from django.shortcuts import render
from meldining.models import Cuisine, CuisineType
from django.http import JsonResponse
from Melbourne.settings import MEDIA_URL
# Create your views here.


def GetCuisine(request):
    if request.method == "GET":
        try:

            data = list(Cuisine.objects.all().values("title", "imageURL"))
            json_list = []
            for i in data:
                base_url = "{0}://{1}{2}{3}".format(request.scheme, request.get_host(), MEDIA_URL, i['imageURL'])
                i['imageURL'] = base_url
                json_list.append(i)

            return JsonResponse({"Cuisine": json_list}, safe=False)

        except KeyError:
            return JsonResponse({"Cuisine": []})
        except ValueError:
            return JsonResponse({"Cuisine": []})
        except:
            return JsonResponse({"Cuisine": []})


def GetCuisineType(request):
    if request.method == "GET":
        try:
            data = list(CuisineType.objects.values("title", "imageURL", "description", "address", "tel", "price"))
            json_list = []
            for i in data:
                base_url = "{0}://{1}{2}{3}".format(request.scheme, request.get_host(), MEDIA_URL, i['imageURL'])
                i['imageURL'] = base_url
                json_list.append(i)

            return JsonResponse({"CuisineType": json_list}, safe=False)

        except KeyError:
            return JsonResponse({"Cuisine": []})
        except ValueError:
            return JsonResponse({"Cuisine": []})
        except:
            return JsonResponse({"Cuisine": []})

