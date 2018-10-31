import json

import requests


# def lambda_handler(event, context):
#     """Sample pure Lambda function

#     Arguments:
#         event LambdaEvent -- Lambda Event received from Invoke API
#         context LambdaContext -- Lambda Context runtime methods and attributes

#     Returns:
#         dict -- {'statusCode': int, 'body': dict}
#     """

#     ip = requests.get('http://checkip.amazonaws.com/')

#     return {
#         "statusCode": 200,
#         "body": json.dumps({
#             'message': 'hello world',
#             'location': ip.text.replace('\n', ''),
#         })
#     }
    
print('Loading function')


def lambda_handler(event, context):
    #print("Received event: " + json.dumps(event, indent=2))
    conv_url = "https://www.converto.io/?v="
    yt_url = event['url']
    print("value1 = " + yt_url)

    if "youtube" in yt_url:
        vid_id = yt_url.split("?v=")[1]
        requests.get(conv_url + vid_id)

    return conv_url+vid_id  # Echo back the first key value
    #raise Exception('Something went wrong')