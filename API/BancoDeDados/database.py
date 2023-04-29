import sqlite3


class LogDb:
    def __init__(self):
            self.connection=sqlite3.connect('BancoApi.db',check_same_thread=False)
            self.cursor= self.connection.cursor()


    def CriaTabela(self):
            query = '''
                Create Table LogAPI(
                    id integer not null primary key autoIncrement,
                    Inputs varchar(255),
                    Predict text,
                    Start text,
                    End text,
                    Processing text)


                '''
            self.cursor.execute(query)


    def Consulta_tabela(self):
            query_con= '''
            select * from LogAPI
                '''
            self.cursor.execute(query_con).fetchall()

    def InsereDado(self,Inputs,Start,End,Processing,Predict):
            query_insert = f'''
                INSERT INTO LogAPI(Inputs, Start, End, Processing,Predict)
                VALUES ('{Inputs}','{Start}','{End}','{Processing}','{Predict}');
                '''
            print(query_insert)
            self.cursor.execute(query_insert)
            self.connection.commit()

    def CloseConecction(self):
           self.cursor.close()