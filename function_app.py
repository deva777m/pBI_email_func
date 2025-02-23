import logging
import os
import azure.functions as func
from azure.communication.email import EmailClient, EmailContent, EmailAddress, EmailMessage

app = func.FunctionApp()

@app.timer_trigger(schedule="0 30 8 * * *", arg_name="myTimer", run_on_startup=False,
                    use_monitor=False) 
def pBIEmailFunction(myTimer: func.TimerRequest) -> None:
    if myTimer.past_due:
        logging.info('The timer is past due!')

    logging.info('Python timer trigger function executed.')

    try:
        connection_string = os.environ["AZURE_COMMUNICATION_EMAIL_CONNECTION_STRING"]
        client = EmailClient.from_connection_string(connection_string)
        
        content = EmailContent(
            subject="Azure Email Communication Service Notification",
            plain_text="This email is sent from the Azure Communication Email Service using our timer trigger function."
        )
        
        recipient = EmailAddress(email=os.environ["EMAIL_RECIPIENT"])
        message = EmailMessage(
            sender=os.environ["EMAIL_SENDER"],
            content=content,
            recipients=[recipient]
        )
        
        result = client.send(message)
        logging.info(f"Email sent successfully. Message Id: {result.message_id}")
    except Exception as e:
        logging.error(f"Error sending email: {e}")

@app.timer_trigger(schedule="0 * * * * *", arg_name="myTimer", run_on_startup=False,
              use_monitor=False) 
def timer_trigger(myTimer: func.TimerRequest) -> None:
    
    if myTimer.past_due:
        logging.info('The timer is past due!')

    logging.info('Python timer trigger function executed.')

@app.timer_trigger(schedule="0 0 9 * * *", arg_name="myTimer", run_on_startup=False,
              use_monitor=False) 
def timer_trigger_emails(myTimer: func.TimerRequest) -> None:
    
    if myTimer.past_due:
        logging.info('The timer is past due!')

    logging.info('Python timer trigger function executed.')