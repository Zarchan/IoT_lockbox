from typing import List, Optional
import boto3
from botocore.exceptions import ClientError

# Simple Email Service client
# https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ses.html#id78
_ses = boto3.client('ses', region_name='us-west-2')


def send_email(
        sender: str, recipients: List[str], subject: str,
        body_text: str, body_html: Optional[str] = None,
        charset: Optional[str] = 'UTF-8'
) -> bool:
    """
    Sends email using the AWS Simple Email Service
    :param sender: email of sender
    :param recipients: list of recipient emails
    :param subject:
    :param body_text:
    :param body_html: optional HTML version of message
    :param charset: which charset to use
    :return: success/failure
    """
    body = {
        'Text': {
            'Charset': charset,
            'Data': body_text,
        },
    }
    if body_html is not None:
        body['Html'] = {
            'Charset': charset,
            'Data': body_html,
        }

    try:
        _ = _ses.send_email(
            Destination={
                'ToAddresses': recipients,
            },
            Message={
                'Body': body,
                'Subject': {
                    'Charset': charset,
                    'Data': subject,
                },
            },
            Source=sender
        )
    except ClientError as e:
        print(e.response['Error']['Message'])
        return False
    return True


if __name__ == '__main__':
    if send_email(
        sender='Princess <chandlerzach@seattleu.edu>',
        recipients=['trann23@seattleu.edu'],
        subject='Subject',
        body_text='(body text)'
    ):
        print('success')
    else:
        print('failure')
