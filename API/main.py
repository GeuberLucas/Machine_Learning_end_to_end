import BancoDeDados.database as db
from flask import Flask, make_response,request
import joblib
from datetime import datetime
import pathlib 
#Instancia
api=Flask(__name__)

#classe de log
lg= db.LogDb()
try:
    lg.Consulta_tabela()
except:
    lg.CriaTabela()
#load model
path= pathlib.Path('./model/Modelo_Floresta_Aleatoria_v1.pkl').absolute()
model= joblib.load(path)

@api.route('/Welcome',methods=['GET'])
def Helloword():
    return {'Retorno ':"Bem vindo ao simulador de aluguel!!"}

@api.route('/Rent-Forecast',methods=['Post'])
def Prevision():
    try:
        ini=datetime.now()
        bodyData= request.json
        city=float(bodyData['city'])
        area=float(bodyData['area'])
        rooms=float(bodyData['rooms'])
        bathroom=float(bodyData['bathroom'])
        parkingspaces=float(bodyData['parkingspaces'])
        floor=float(bodyData['floor'])
        animal=float(bodyData['animal'])
        furniture=float(bodyData['furniture'])
        hoa =float(bodyData['hoa(R$)'])
        propertyTax=float(bodyData['propertytax(R$)'])
        lista=[city,area,rooms,bathroom,parkingspaces,floor,animal,furniture,hoa,propertyTax]
        
        Inputs=''
        for value in lista:
            print(value)
            Inputs += ';'+str(value)
        
        response=model.predict([lista])
        end= datetime.now()
        processing= end-ini
        lg.InsereDado(Inputs,str(ini),str(end),str(processing),str(response))

        return {'valor do Aluguel':str(response)}
   
        
    except ValueError:
        print("Could not convert data to an integer.")
    except Exception as err:
        if not bodyData['city']:
            return make_response('Informe o city', 400)
        if not bodyData['area']:
            return make_response('Informe o area', 400)
        if not bodyData['rooms']:
            return make_response('Informe o rooms', 400)
        if not bodyData['bathroom']:
            return make_response('Informe o bathroom', 400)
        if not bodyData['parkingspaces']:
            return make_response('Informe o parking spaces', 400)
        if not bodyData['floor']:
            return make_response('Informe o floor', 400)
        if not bodyData['animal']:
            return make_response('Informe o animal', 400)
        if not bodyData['furniture']:
            return make_response('Informe o furniture', 400)
        if not bodyData['hoa(R$)']:
            return make_response('Informe o hoa (R$)', 400)
        if not bodyData['propertytax(R$)']:
            return make_response('Informe o property tax (R$)', 400)
        
       
        raise

       
        




if __name__ == '__main__':
    api.run(debug=True)