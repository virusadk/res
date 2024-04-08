import requests
from datetime import date
import codecs
from telegram import send_telegram
from telegramchannel import send_channel

dt_now = current_date = date.today()
fdate = f'{dt_now}'
year = fdate.split('-')[0]
month = fdate.split('-')[1]
day = int(fdate.split('-')[2])
fday =f'{day}'
kol = len(fday)
if int(kol) == 1:
    days = f'0{fday}'
else:
    days = fday
# print(kol)
daypr = int(day) - 1
fdaypr = f'{daypr}'
kolfdaypr = len(fdaypr)
if int(kolfdaypr) == 1:
    dayspr = f'0{daypr}'
else:
    dayspr = daypr
# print(dt_now)
# print(year)
# print(month)
# print(day)
# print(daypr)


def main():
    mass_game =[]
    date_mass = [dayspr,days]
    mes = [month]
    
    for mess in mes:
        me = mess
        da = f'{year}-{me}'
        for datet in date_mass:
            dar = f'{da}-{datet}'
            # print(dar)
        
        
            
            cookies = {
                'cud': 'rBMAD2YCXpW9EQt3B/I3Ag==',
                '_ym_uid': '1711431339727122409',
                '_ym_d': '1711431339',
                'xq_icm': '13000',
                'acceptCookies': 'true',
                'lang': '0',
                '_gid': 'GA1.2.2085068874.1712207000',
                '_ga_Y9VSRWL1PZ': 'GS1.2.1712217974.8.1.1712220769.0.0.0',
                '_ga': 'GA1.2.698336348.1711431335',
                '_ym_isad': '2',
                '_gat': '1',
                '_ga_NBF6PN1P8S': 'GS1.2.1712302856.17.1.1712303784.0.0.0',
            }

            headers = {
                'authority': 'd.betcity.by',
                'accept': 'application/json, text/plain, */*',
                'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
                'content-type': 'application/x-www-form-urlencoded',
                # 'cookie': 'cud=rBMAD2YCXpW9EQt3B/I3Ag==; _ym_uid=1711431339727122409; _ym_d=1711431339; xq_icm=13000; acceptCookies=true; lang=0; _gid=GA1.2.2085068874.1712207000; _ga_Y9VSRWL1PZ=GS1.2.1712217974.8.1.1712220769.0.0.0; _ga=GA1.2.698336348.1711431335; _ym_isad=2; _gat=1; _ga_NBF6PN1P8S=GS1.2.1712302856.17.1.1712303784.0.0.0',
                'origin': 'https://betcity.by',
                'referer': 'https://betcity.by/',
                'sec-ch-ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Opera";v="108"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-site',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 OPR/108.0.0.0',
            }

            params = {
                'rev': '5',
                'date': dar,
                'ver': '456',
                'csn': 'lsmif5',
                'ids_sp':'46',
            }

            response = requests.get('https://d.betcity.by/api/v1/results', params=params, cookies=cookies, headers=headers)
            # print(response.content)
            resultline = response.json()
            # print(resultline)
            tr = 46
            tr1 = str(tr)
            
            for game in resultline['reply']['sports'][tr1]['chmps']:
                evts = resultline['reply']['sports'][tr1]['chmps'][game]['evts']
                for igra in evts:
                
                    # print(game)
                    try:
                        ddate = resultline['reply']['sports'][tr1]['chmps'][game]['evts'][igra]['date_ev']
                    except:
                        pass
                    date = ddate[:-9]
                    # print(date)
                    try:
                        team1 = resultline['reply']['sports'][tr1]['chmps'][game]['evts'][igra]['name_ht']
                        team2 = resultline['reply']['sports'][tr1]['chmps'][game]['evts'][igra]['name_at']
                    except:
                        pass
                    with codecs.open('spisok.txt','r' ,'utf-8') as file:
                                    
                        for item in file.readlines():
                            
                            line = item.strip()
                            # print(line)
                            liga = line.split('--')[1]
                            dateinspisok = line.split('--')[2]
                            dateinspisok1 = dateinspisok[:-6]
                            # print(dateinspisok1)
                            team1surename = line.split('--')[3]
                            # print(team1surename)
                            team2surename = line.split('--')[4]
                            stavka = line.split('--')[5]
                            # print(team2surename)
                    # print(date)

                    
                            
                            # print(dateinspisok)        
                            if (date == dateinspisok1) and (team1surename == team1) and (team2surename == team2):
                                
                                
                            

                                try:
                                    score = resultline['reply']['sports'][tr1]['chmps'][game]['evts'][igra]['sc_ext_ev']
                                except:
                                    pass
                                print(date,team1,team2)
                                print(score)
                                schet = []
                                
                                
        #                         score2 = score.replace(',', "")
                                
        #                         # schet.append(score3)
        #                         try:
        #                             set = score2.split(' ')[0]
                                    
        #                             schet.append(set)
        #                         except:
        #                             pass
        #                         try:
        #                             set = score2.split(' ')[1]
                                    
        #                             schet.append(set)
        #                         except:
        #                             pass
        #                         try:
        #                             set = score2.split(' ')[2]
                                    
        #                             schet.append(set)
        #                         except:
        #                             pass
        #                         try:
        #                             set = score2.split(' ')[3]
                                    
        #                             schet.append(set)
        #                         except:
        #                             pass
        #                         try:
        #                             set = score2.split(' ')[4]
                                    
        #                             schet.append(set)
        #                         except:
        #                             pass
        #                     # print(set_mass)
        #                         sum_point = summ_point_set_mass(schet)
        #                         # print(sum_point)
        #                         ishod = []
                                
        #                         if ('ТМ' in stavka):
        #                             try:
        #                                 set1 = sum_point[0]
        #                                 if (set1 <= 18):
        #                                     ishod.append('1:\U00002714')
        #                                 else:
        #                                     ishod.append('1:\U0000274C')
        #                                 print(set1)
        #                             except:
        #                                 pass
        #                             try:
        #                                 set2 = sum_point[1]
        #                                 if (set2 <= 18):
        #                                     ishod.append('2:\U00002714')
        #                                 else:
        #                                     ishod.append('2:\U0000274C')
        #                                 print(set2)
        #                             except:
        #                                 pass
        #                             try:
        #                                 set3 = sum_point[2]
        #                                 if (set3 <= 18):
        #                                     ishod.append('3:\U00002714')
        #                                 else:
        #                                     ishod.append('3:\U0000274C')
        #                                 print(set3)
        #                             except:
        #                                 pass
        #                             try:
        #                                 set4 = sum_point[3]
        #                                 if (set4 <= 18):
        #                                     ishod.append('4:\U00002714')
        #                                 else:
        #                                     ishod.append('4:\U0000274C')
        #                                 print(set4)
        #                             except:
        #                                 pass
        #                             try:
        #                                 set5 = sum_point[4]
        #                                 if (set5 <= 18):
        #                                     ishod.append('5:\U00002714')
        #                                 else:
        #                                     ishod.append('5:\U0000274C')
        #                                 print(set5)
        #                             except:
        #                                 pass
        #                             game = []
        #                             game.append(dateinspisok)
        #                             game.append(liga)
                                
        #                             game.append(team1surename)
        #                             game.append(team2surename)
                                    
        #                             game.append(stavka)
        #                             game.append(ishod)
        #                             mass_game.append(game)
        #                             print(ishod)
        #                         if ('ТБ' in stavka):
        #                             try:
        #                                 set1 = sum_point[0]
        #                                 if (set1 >= 19):
        #                                     ishod.append('1:\U00002714')
        #                                 else:
        #                                     ishod.append('1:\U0000274C')
        #                                 print(set1)
        #                             except:
        #                                 pass
        #                             try:
        #                                 set2 = sum_point[1]
        #                                 if (set2 >= 19):
        #                                     ishod.append('2:\U00002714')
        #                                 else:
        #                                     ishod.append('2:\U0000274C')
        #                                 print(set2)
        #                             except:
        #                                 pass
        #                             try:
        #                                 set3 = sum_point[2]
        #                                 if (set3 >= 19):
        #                                     ishod.append('3:\U00002714')
        #                                 else:
        #                                     ishod.append('3:\U0000274C')
        #                                 print(set3)
        #                             except:
        #                                 pass
        #                             try:
        #                                 set4 = sum_point[3]
        #                                 if (set4 >= 19):
        #                                     ishod.append('4:\U00002714')
        #                                 else:
        #                                     ishod.append('4:\U0000274C')
        #                                 print(set4)
        #                             except:
        #                                 pass
        #                             try:
        #                                 set5 = sum_point[4]
        #                                 if (set5 >= 19):
        #                                     ishod.append('5:\U00002714')
        #                                 else:
        #                                     ishod.append('5:\U0000274C')
        #                                 print(set5)
        #                             except:
        #                                 pass
        #                             game = []
        #                             game.append(dateinspisok)
        #                             game.append(liga)
                                
        #                             game.append(team1surename)
        #                             game.append(team2surename)
                                    
        #                             game.append(stavka)
        #                             game.append(ishod)
        #                             mass_game.append(game)
        #                         # print(ishod)
        #                         # print(game)
        # print(mass_game)
        # s = sorted(mass_game, key=lambda student: student[0])
        # message = ''
        # for g in s:
        #     # print(g[2],g[3],g[4]) 
        #     # with codecs.open('spisok.txt', 'a', 'utf-8') as file:
        #     #     file.write(f'\n{g[0]}--{g[1]}--{g[2]}--{g[3]}--{g[4]}--{g[7]}') 
        #     #     file.close()
        #     # fsets = ''
        #     # for g8 in g[8]:
        #     #     fesets = f'{g8} '
        #     #     fsets = fsets + fesets
        #     mess = f'\U0001F4C6 {g[0]} \n' \
        #                 f'\U0001F3D3 {g[1]}\n' \
        #                 f'\U0001F9D1 {g[2]} - {g[3]} \n' \
        #                 f'\U0001F4B2 Ставка: {g[4]} \n'\
        #                 f'\U0001F4B2 Результат: \n'\
        #                 f'{g[5]}\n'\
        #                 \
        #                 f'----------------------------------------------------------\n'\
        #                 # f'\n' 
        #     message = message + mess  
                        
        # send_telegram(message)
        # send_channel(message)
                                
                                    


                    
                

                # schet = []
                
                # try:
                #     score1 = score.split(' (')[1]
                # except:
                #     pass
                # score2 = score1.replace(',', "")
                # score3 = score2.replace(')', "")
                # # schet.append(score3)
                # try:
                #     set = score3.split(' ')[0]
                    
                #     schet.append(set)
                # except:
                #     pass
                # try:
                #     set = score3.split(' ')[1]
                    
                #     schet.append(set)
                # except:
                #     pass
                # try:
                #     set = score3.split(' ')[2]
                    
                #     schet.append(set)
                # except:
                #     pass
                # try:
                #     set = score3.split(' ')[3]
                    
                #     schet.append(set)
                # except:
                #     pass
                # try:
                #     set = score3.split(' ')[4]
                    
                #     schet.append(set)
                # except:
                #     pass
            # print(set_mass)
                # sum_point = summ_point_set_mass(schet)
def summ_point_set_mass(set_mass):
    # Создаем пустой массив
    summ_set_mass = []
    # Цикл переборки полученного массива
    for si in (set_mass):
        
        # Обработка исключений счетчика сумм
        try:
            # Парсим строку по заданному символу и присваиваем нужную часть строки переменной
            s1 = si.split(':')[0] 
            # Парсим строку по заданному символу и присваиваем нужную часть строки переменной           
            s2 = si.split(':')[1]    
            # Получаем сумму переменных    
            summ = int(s1) + int(s2)
            # Добавляем полученную сумму в массив
            summ_set_mass.append(summ)
        # Выполняется в случае возникновения исключения
        except:
            # Пропустить - ничего не выполнять
            pass
    # Возвращаем полученный массив значений
    return(summ_set_mass)
if __name__ == '__main__':
    main()