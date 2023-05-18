import boto3
import calendar
import os
from slack_sdk import WebClient
from datetime import datetime, timezone, date
from rocketry import Rocketry
from rocketry.conds import daily, every

app = Rocketry()

SLACK_BOT_TOKEN = os.environ["SLACK_BOT_TOKEN"]
THRESHOLD = 5

def get_current_costs() -> float:
    client = boto3.client('ce', 'us-east-1')  # AWS Cost Explorer client

    # Get the current date and the first day of the month
    end = datetime.now(timezone.utc).date()
    start = datetime(end.year, end.month, 1).date()

    try:
        # Retrieve the cost and usage data
        response = client.get_cost_and_usage(
            TimePeriod={
                'Start': start.isoformat(),
                'End': end.isoformat()
            },
            Granularity='MONTHLY',
            Metrics=['BlendedCost']
        )
    except Exception as e:
        print(e)
        return 0.0

    return response['ResultsByTime'][0]['Total']['BlendedCost']['Amount']

def get_end_of_month_projection(current_cost) -> float:
    current_date = datetime.now().date()
    days_in_month = calendar.monthrange(current_date.year, current_date.month)[1]
    current_day_of_month = current_date.day
    remaining_days = days_in_month - current_day_of_month
    projected_cost = (current_cost / current_date.day) * days_in_month
    projected_spending = (current_cost / current_date.day) * remaining_days

    return projected_cost, projected_spending

def send_slack_notification(message):
    client = WebClient(token=SLACK_BOT_TOKEN)

    return client.chat_postMessage(channel='#alerts', text=message)

def check_threshold_exceeded(projected_cost: float) -> bool:
    if projected_cost > THRESHOLD:
        message = f"ATTENTION! Projected end-of-month AWS costs of {projected_cost:.2f} USD exceeds {THRESHOLD} USD!"
        response = send_slack_notification(message)
        if response['ok']:
            print("Slack notification sent successfully!\n")
            return True
        else:
            print("Failed to send Slack notification.\n")
            return False

@app.task(daily.at("22:30"))
# @app.task(every("10 seconds"))
def main():
    current_cost = get_current_costs()
    projected_cost, projected_spending = get_end_of_month_projection(float(current_cost))
    print(f"Current month costs: {current_cost} USD")
    print(f"Projected end-of-month costs: {projected_cost:.2f} USD")
    print(f"Projected end-of-month spending: {projected_spending:.2f} USD")
    if check_threshold_exceeded(projected_cost):
        return
    else:
        print("No threshold exceeded.\n")

if __name__ == "__main__":
    app.run()
