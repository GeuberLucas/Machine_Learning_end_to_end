from flask import Flask,request
import joblib

#Instancia
api=Flask(__name__)
#load model
model= joblib.load('model\Modelo_Floresta_Aleatoria_v1.pkl')

@api.route('/Welcome',methods=['GET'])
def Helloword():
    return {'Retorno': "Bem vindo ao simulador de aluguel!!"}

@api.route('/Rent-Forecast',methods=['Post'])
def Prevision():
    try:
        response=model.Predict()
        return response
    except:
        return {"Error":500}




if __name__ == '__main__':
    api.run(debug=True)