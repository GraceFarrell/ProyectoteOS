import json
import boto3
def Take_Orders(orders):
	orders = orders.replace("'", "\"")    
	data = json.loads(orders)  
	return data

def Recieve_Orders():
	sqs = boto3.client('sqs')
	response = sqs.receive_message(QueueUrl = 'https://sqs.us-east-1.amazonaws.com/292274580527/cc406_team2')
	
	message_string = ""

	for message in response["Messages"]:
		message_string = message['Body']
		receipt = message["ReceiptHandle"]

	return Take_Orders(message_string), receipt
