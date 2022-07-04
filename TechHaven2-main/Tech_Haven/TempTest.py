import base64
def encoding(list):
    encodedList = []
    for eachitems in range(0,len(list)):
        message = list[eachitems]
        message_bytes = message.encode('ascii')
        base64_bytes = base64.b64encode(message_bytes)
        base64_message = base64_bytes.decode('ascii')
        encodedList.append(base64_message)
    return encodedList

def decoding(list):
    decodedList = []
    for eachitem in range (0,len(list)):
        base64_message = list[eachitem]
        base64_bytes = base64_message.encode('ascii')
        message_bytes = base64.b64decode(base64_bytes)
        message = message_bytes.decode('ascii')
        decodedList.append(message)
    print(decodedList)
    return decodedList



