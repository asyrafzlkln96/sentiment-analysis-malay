from rest_framework.decorators import renderer_classes, api_view
from rest_framework_swagger.renderers import OpenAPIRenderer, SwaggerUIRenderer
import coreapi
from rest_framework import response

# noinspection PyArgumentList
@api_view()
@renderer_classes([SwaggerUIRenderer, OpenAPIRenderer])
def schema_view(request):
    print("---inside schema view-----")
    # noinspection PyArgumentList
    schema = coreapi.Document(
    title='Keyword Classifier API',
    #url='Your host url',
    content=
        {
            'Keyword Classifier Model Status': coreapi.Link(
                url='/api/spice/KeywordClassifier',
                action='post',
                #encoding='application/json',
                fields=
                [
                    coreapi.Field('refer to documentation the JSON format', required=True, location='form', type='string', description='')
                ],
                description='Get prediction model status'
            ),
            'Keyword Classifier Prediction': coreapi.Link(
                url='/api/spice/KeywordClassifier',
                action='post',
                #encoding='application/json',
                fields=
                [
                    coreapi.Field('refer to documentation the JSON format', required=True, location='form', type='string', description='')
                ],
                # {
                #         "RequestHeader": {
                #             "EventName": "evTextCategorization",
                #             "DateTimeSend": "03/05/2018 14:39:48",
                #             "MsgID": "123",
                #             "EnableNormalize": "True",
                #             "Domain": "TMFulfillment",
                #             "ModelID": 48
                #         },
                #         "InputStruct": [
                #               {
                #                   "TextID": "123456",
                #                   "TextInput": "technician datang but my modem still problem"
                #               }
                #         ]
                # },
                description='Perform key classifier'
            ),
        }
    )
    # schema = generator.get_schema(request)
    return response.Response(schema)
