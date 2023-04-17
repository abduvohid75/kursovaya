import json
import time
from datetime import datetime



def get_data():
    with open('operations.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
        print(data)
    return data

def filter_data(data):
    data = [x for x in data if 'state' in x and x['state'] == 'EXECUTED']
    return data

def sort_data(data):
    data = sorted(data, key=lambda x: x['date'], reverse=True)
    return data[:5]

def format_data(data):
    formatted_data = []
    for row in data:
        date = datetime.strptime(row['date'], '%Y-%m-%dT%H:%M:%S.%f').strftime("%d.%m.%Y")
        description = row['description']
        if "from" in row and "to" in row:
            from_arrow = "->"
            sender = row['from'].split()
            sender_bill = sender.pop(-1)
            sender_info = " ".join(sender)
            sender_bill = f"{sender_bill[:4]} {sender_bill[4:6]}** ****{sender_bill[-4:]}"
            sender1 = row['to'].split()
            sender_bill1 = sender1.pop(-1)
            sender_info1 = " ".join(sender1)
            sender_bill1 = f" **{sender_bill1[-4:]}"
            if "operationAmount" in row:
                summ = row['operationAmount']['amount']
                curensy = row['operationAmount']['currency']['name']
                summ = f"{summ} {curensy}"
            else:
                sender_account_index = ""
        else:
            sender_info = "Новый счет"
            sender_info1 =""
            sender_bill = ""
            sender_bill1 = ""
            curensy = ""
            summ = ""
            from_arrow = ""

        formatted_data.append(f"""
{date} {description}
{sender_info} {sender_bill} {from_arrow} {sender_info1} {sender_bill1}
{summ}\
        """)
    return formatted_data







