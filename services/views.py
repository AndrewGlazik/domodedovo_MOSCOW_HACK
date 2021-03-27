import json

from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt


@method_decorator(csrf_exempt, name='dispatch')
class ServicesDME(View):
    def post(self, request):
        json_request = json.loads(request.body)

        data = {
            "serviceProviderHeader":
                {
                    "prefLanguage": "en_US",
                    "serviceID": "fmg/lounges/atlanticLounge",
                    "bookingID": 449543055,
                    "extBookingID": "AL1448370465369",
                    "bookingStatus": 101,
                    "currentWizardStep": 1
                },
            "serviceFormPage":
                {
                    "id": 1,
                    "title": "Step 1",
                    "wizardStep": 1,
                    "serviceFormElements":
                        [
                            {
                                "id": 10,
                                "title": "1. Date and Flight data",
                                "footerText": "",
                                "serviceElements":
                                    [
                                        {
                                            "id": 101,
                                            "elementType": "text",
                                            "valueDefinition": "Flight number",
                                            "value": "",
                                            "editable": True,
                                            "contentCategory": "flightNr",
                                            "contentKey": "departure",
                                            "mandatory": True
                                        },
                                        {
                                            "id": 102,
                                            "elementType": "date",
                                            "valueDefinition": "Day",
                                            "value": "",
                                            "editable": True,
                                            "contentCategory": "date",
                                            "contentKey": "departure",
                                            "mandatory": True
                                        },
                                        {
                                            "id": 103,
                                            "elementType": "time",
                                            "valueDefinition": "Departure / arrival time",
                                            "value": "",
                                            "editable": True,
                                            "contentCategory": "time",
                                            "contentKey": "departure",
                                            "mandatory": True
                                        }
                                    ]
                            }
                        ]
                },
            "validationError": "",
            "bookingFee":
                {
                    "preTaxFee": 25.0,
                    "taxRate": 19.0,
                    "taxInvoiceInfoText":
                        {
                            "line1": "Umsätze 19%",
                            "line2": "",
                            "line3": ""
                        },
                    "customInfoText":
                        [
                            "1110",
                            "50440"
                        ]
                },
            "termConditionURL": "http://www.munich-airport.de/de/general/impressum/index.jsp"
        }
        return JsonResponse(data, content_type='application/json')
