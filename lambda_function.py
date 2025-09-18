import json
import boto3

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("StudentRecords")


def lambda_handler(event, context):
    try:
        if event["httpMethod"] == "POST":
            student = json.loads(event["body"])
            table.put_item(Item=student)
            return {
                "statusCode": 200,
                "body": json.dumps("Student record added successfully"),
            }

        elif event["httpMethod"] == "GET":
            student_id = event["queryStringParameters"]["student_id"]
            response = table.get_item(Key={"student_id": student_id})
            return {"statusCode": 200, "body": json.dumps(response.get("Item", {}))}
    except Exception as e:
        return {"statusCode": 500, "body": json.dumps(f"Error: {str(e)}")}
