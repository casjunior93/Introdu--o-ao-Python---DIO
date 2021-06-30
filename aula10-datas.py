from datetime import date, time, datetime, timedelta

def com_date():
    #data atual
    data_atual = date.today()
    data_atual = data_atual.strftime('%A/%B/%Y')
    print(data_atual)

def com_time():
    horario = time(hour=15, minute=18,second=30)
    print(horario.strftime('%H:%M:%S'))

def com_datetime():
    #data atual
    data_atual = datetime.now()
    print(data_atual.strftime('%m/%Y %H:%M:%S'))
    print(data_atual.strftime('%c'))
    print(data_atual.hour)
    print(data_atual.minute)
    print(data_atual.day)
    print(data_atual.date())
    print(data_atual.weekday())

    tupla = ("Seg", "Ter", "Qua", "Qui", "Sex", "Sab", "Dom")

    print(tupla[data_atual.weekday()])

    data_criada = datetime(2021,6,20,15,30,20)
    print(data_criada.strftime('%c'))

    nova_data = datetime.now() - timedelta(days=365)

    nova_data2 = datetime.now() - data_criada

    print(nova_data)
    print(nova_data2)

    data = datetime(1815, 12, 10, 00, 00, 00).strftime('%d/%m/%Y')
    hora = time(hour=13, minute=14, second=00)
    print('{} às {}'.format(data, hora))


if __name__ == "__main__":
    com_datetime()