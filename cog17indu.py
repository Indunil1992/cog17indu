import boto3
cognito_idp = boto3.client("cognito-idp")

def handler(event, context):
    try:
        data = cognito_idp.list_users(
            UserPoolId="us-east-1_HdYJb7Znp",
            Limit=10
        )
    except BaseException as e:
        print(e)
        raise(e)
    
    return {"message": "Successfully executed"}
