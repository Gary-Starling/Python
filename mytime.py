import datetime

#Разбивае ввод даты
list_date = [int(x) for x in input().split()] 
current_data = datetime.date(list_date[0], list_date[1], list_date[2])
#print(current_data)
after_days = int(input())
delta = datetime.timedelta(days=after_days)
current_data = current_data + delta
print(current_data.year, current_data.month, current_data.day)