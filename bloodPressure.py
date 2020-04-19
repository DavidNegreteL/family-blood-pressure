import matplotlib.pyplot as plt
from time import sleep
import csv
def registrar(dias):
    for registro in range(dias):
        sys = int(input('¿Cuál es la presión sistólica?: '))
        diast = int(input('¿Cuál es la presión diastólica?: '))
        pulse = int(input('¿Cuál es el puslo?: '))
        rdiast = [diast]
        rsys = [sys]
        rpulse = [pulse]
        with open('DB_syst.csv', mode='a' , newline='') as reg_sys:
            registro_sys = csv.writer(reg_sys,delimiter=',',quotechar='"',quoting=csv.QUOTE_MINIMAL)
            registro_sys.writerow(rsys)
        with open('DB_diast.csv', mode='a' , newline='') as reg_diast:
            registro_diast = csv.writer(reg_diast,delimiter=',',quotechar='"',quoting=csv.QUOTE_MINIMAL)
            registro_diast.writerow(rdiast)
        with open('DB_pulse.csv', mode='a' , newline='') as reg_pulse:
            registro_pulse = csv.writer(reg_pulse,delimiter=',',quotechar='"',quoting=csv.QUOTE_MINIMAL)
            registro_pulse.writerow(rpulse)
def graficarsys():
    valorSys = list()
    with open('DB_syst.csv') as valorS:
        valorSys_lectura = csv.reader(valorS,delimiter=',',quotechar='"')
        for row in valorSys_lectura:
            valorSys.append(float(','.join(row)))
            print(row)
            print(valorSys)
        plt.plot(valorSys)
        plt.title('Blood Pressure')
        plt.ylabel('Systolic pressure (mmHg)')
        plt.xlabel('Days')
        plt.show()

def graficardiast():
    valorDiast = list()
    with open('DB_diast.csv') as valorD:
        valorDiast_lectura = csv.reader(valorD,delimiter=',',quotechar='"')
        for row in valorDiast_lectura:
            valorDiast.append(float(','.join(row)))
            print(row)
            print(valorDiast)
        plt.plot(valorDiast)
        plt.title('Blood Pressure')
        plt.ylabel('Diastole pressure (mmHg)')
        plt.xlabel('Days')
        plt.show()

def graficarpulse():
    valorPulse = list()
    with open('DB_pulse.csv') as valorP:
        valorPulse_lectura = csv.reader(valorP,delimiter=',',quotechar='"')
        for row in valorPulse_lectura:
            valorPulse.append(float(','.join(row)))
            print(row)
            print(valorPulse)
        plt.plot(valorPulse)
        plt.title('Pulse')
        plt.ylabel('Pulse (pulse/min)')
        plt.xlabel('Days')
        plt.show()
def graficacompleta():
    valorSys = list()
    with open('DB_syst.csv') as valorS:
        valorSys_lectura = csv.reader(valorS,delimiter=',',quotechar='"')
        for row in valorSys_lectura:
            valorSys.append(float(','.join(row)))

    valorDiast = list()
    with open('DB_diast.csv') as valorD:
        valorDiast_lectura = csv.reader(valorD,delimiter=',',quotechar='"')
        for row in valorDiast_lectura:
            valorDiast.append(float(','.join(row)))

    valorPulse = list()
    with open('DB_pulse.csv') as valorP:
        valorPulse_lectura = csv.reader(valorP,delimiter=',',quotechar='"')
        for row in valorPulse_lectura:
            valorPulse.append(float(','.join(row)))
    plt.plot(valorSys,'m.-',label='Systolic (mmHg)')
    plt.plot(valorDiast,'k.-',label='Diastolic (mmHg)')
    plt.plot(valorPulse,'g.-',label='Pulse (pulse/min)')
    plt.title('Blood Pressure')
    plt.ylabel('')
    plt.xlabel('Days')
    plt.legend()
    plt.show()
    

if __name__=='__main__':
    dias = int(input('¿Durante cuántos días se hará el registro de presión arterial?: '))
    registrar(dias)
    graficarsys()
    graficardiast()
    graficarpulse()
    graficacompleta()