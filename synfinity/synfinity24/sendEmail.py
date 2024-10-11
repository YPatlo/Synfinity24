from __future__ import print_function
import os
import sib_api_v3_sdk
from sib_api_v3_sdk.rest import ApiException
from pprint import pprint

def sendEmailPy(event, sklEmail, sklName, teachEmail, accTeach, teamEmail, teamName, studentDetails):
    configuration = sib_api_v3_sdk.Configuration()
    configuration.api_key['api-key'] = os.environ['API_KEY']
    api_instance = sib_api_v3_sdk.TransactionalEmailsApi(sib_api_v3_sdk.ApiClient(configuration))

    to = [
            {
                "email": teamEmail,
                "name": teamName
            },
            {
                "email": sklEmail,
                "name": sklName
            },
            {
                "email": teachEmail,
                "name": accTeach
            }
        ]
    templateId = 2
    bcc = [{ "email": "patloyashwanthkumar2+synfinity@gmail.com" }]
    reply_to = {
            "email": "synfinity@gsshsr.in",
            "name": "GSSE Synfinity 2024"
        }
    params = {
            "event": event,
            "teamName": teamName,
            "schoolDetails": "School Name: " + sklName +"\nAccompanying Teacher: " + accTeach,
            "studentDetails": studentDetails,
            "contactDetails": "School Email: " + sklEmail + "\nTeam Email: " + teamEmail + "\nAccompanying Teacher Email: " + teachEmail,
            "email": sklEmail + " &  " + teamEmail + " & " + teachEmail
        }
    headers = {
            "accept": "application/json",
            "content-type": "application/json",
            "api-key": os.environ['API_KEY']
        }
    send_smtp_email = sib_api_v3_sdk.SendSmtpEmail(template_id=templateId, params=params, to=to, bcc=bcc, reply_to=reply_to, headers=headers)

    try:
        api_response = api_instance.send_transac_email(send_smtp_email)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SMTPApi->send_transac_email: %s\n" % e)
