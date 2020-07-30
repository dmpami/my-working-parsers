import requests
import datetime
from bs4 import BeautifulSoup as BeautifulSoup
from time import sleep

# Логины ЛК телфина
login_array = [
["*****" ,"*****","login,"password"],

]
# Подсчет количества строк
len_m =	len(login_array)

#Отправляем заголовки
HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36','accep':'*/*'}

#Функция вывода баланса с Телфина 
def TelphinRequest(organization,department,login,password):
	s = requests.Session()
	url = "https://cabinet.telphin.ru/login"
	# Отправляем post запрос с атрибутами login и password
	r = s.post(url, headers=HEADERS, data={'LoginForm[username]':login,'LoginForm[password]':password})
	webpage = r.text
	#Передаем страницу в BeautifulSoup
	soup = BeautifulSoup(webpage,"html.parser")
	# Получаем значение нужного нам class
	items = soup.find_all(class_='balance-index')
	# Переводим данные в строку
	stritem = str(items)
	# Убераем лишнее из строки
	stritems = stritem[2:]
	start = stritems.find('>')
	end = stritems.find('<')
	# Выводим результат
	print ("\n Договор " + login + ' ' + organization + ' ' + department )
	print (' ' + stritems[start+1:end])
	# Записываем данные в файл
	f = open('balans_Telphin.txt', 'a')
	f.write("\n Договор " + login + ' ' + organization + ' ' + department)
	f.write(' \n ' + stritems[start+1:end] + '\n')
	f.close	
	
# ----- ----- ----- Начало программы ----- ----- -----
# Записываем текущую дату в файл
data_log = datetime.date.today()
file = open("balans_Telphin.txt", "w")
file.write('Данные актуальны на ' + str(data_log) + '\n')
file.close()

x = 0
while x < len_m:
	zapros = x+1
	print ('\n Запрос ' + str(zapros) + ' из ' + str(len_m))
	TelphinRequest(login_array[x][0],login_array[x][1],login_array[x][2],login_array[x][3])
	sleep(10.0)
	x += 1
print ('\n\n\n   -Завершение программы')	