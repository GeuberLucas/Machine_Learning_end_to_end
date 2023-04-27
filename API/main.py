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
        bodyData= request.get_json()
        response=model.Predict([bodyData['city'],\
            bodyData['area'],\
            bodyData['rooms'],\
            bodyData['bathroom'],\
            bodyData['parking spaces'],\
            bodyData['floor'],\
            bodyData['animal'],\
            bodyData['furniture'],\
            bodyData['hoa (R$)'],\
            bodyData['rent amount (R$)'],\
            bodyData['property tax (R$)']])
    
        return response
    except:
        return {"Error":500}




if __name__ == '__main__':
    api.run(debug=True)