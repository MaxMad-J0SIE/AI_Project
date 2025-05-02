import numpy as np
from custom_functions import CustomMethodes
cm = CustomMethodes()
import mysql.connector

class DataHolder:

    def __init__(self):
        self.mydb = None
        self.mycursor = None
        try:
            self.mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="123",
                database="ai_data"
            )
            self.mycursor = self.mydb.cursor()
            print("Connected to MySQL Database")

        except mysql.connector.Error as err:
            print(f"Error during database connection in __init__: {err}")

        self.table1 = np.array([
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 1, 1, 0, 0, 0,
            0, 0, 0, 0, 1, 0, 1, 0, 0, 0,
            0, 0, 0, 1, 0, 0, 1, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 1, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 1, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 1, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 1, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        ])

        self.answer_key1 = 1

        self.table2 = np.array([
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 1, 1, 0, 0, 0, 0,
            0, 0, 0, 1, 0, 0, 1, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 1, 0, 0, 0,
            0, 0, 0, 0, 0, 1, 0, 0, 0, 0,
            0, 0, 0, 0, 1, 0, 0, 0, 0, 0,
            0, 0, 0, 1, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 1, 1, 1, 1, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        ])

        self.answer_key2 = 2

        self.bias = 0.5

        self.acceptable_error = 0.4

        self.mycursor.execute("SELECT * FROM hidden_layer_1 where weights_id=1")
        self.weights1 = self.mycursor.fetchall()
        self.mycursor.execute("SELECT * FROM hidden_layer_1 where weights_id=2")
        self.weights2 = self.mycursor.fetchall()
        self.mycursor.execute("SELECT * FROM hidden_layer_1 where weights_id=3")
        self.weights3 = self.mycursor.fetchall()
        self.mycursor.execute("SELECT * FROM hidden_layer_1 where weights_id=4")
        self.weights4 = self.mycursor.fetchall()
        self.mycursor.execute("SELECT * FROM hidden_layer_1 where weights_id=5")
        self.weights5 = self.mycursor.fetchall()
        self.mycursor.execute("SELECT * FROM hidden_layer_1 where weights_id=6")
        self.weights6 = self.mycursor.fetchall()
        self.mycursor.execute("SELECT * FROM hidden_layer_2 where weights_id=1")
        self.weights11 = self.mycursor.fetchall()
        self.mycursor.execute("SELECT * FROM hidden_layer_2 where weights_id=2")
        self.weights12 = self.mycursor.fetchall()
        self.mycursor.execute("SELECT * FROM hidden_layer_2 where weights_id=3")
        self.weights13 = self.mycursor.fetchall()
        self.mycursor.execute("SELECT * FROM output_layer")
        self.output_weights = self.mycursor.fetchall()
        print(f"{self.weights1}\n{self.weights2}\n{self.weights3}\n{self.weights4}\n{self.weights5}\n{self.weights6}\n{self.weights11}\n{self.weights12}\n{self.weights13}\n{self.output_weights}\n")
        print(f"{self.weights1[0][1]} weights 1 1")

dh = DataHolder()