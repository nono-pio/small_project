import sqlite3
import os

class DataHandle:
    def __init__(self, database_name : str) -> None:
        self.connection = sqlite3.connect(f"{os.path.dirname(os.path.abspath(__file__))}/{database_name}")
        self.connection.row_factory = sqlite3.Row
    
    def createToDo(self, objective : str, completed : str = "F") -> None:
        cursor = self.connection.cursor()
        query = f"INSERT INTO ToDo (objective,completed) VALUES ('{objective}','{completed}');"
        cursor.execute(query)
        cursor.close()
        self.connection.commit()
    
    def createManyToDo(self, datas:list[tuple[str]]):
        print(datas)
        datas = [(d[0], 'F' if type(d) == str else d[1] ) for d in datas]
        cursor = self.connection.cursor()
        query = f"INSERT INTO ToDo (objective,completed) VALUES (?,?)"
        cursor.executemany(query, datas)
        cursor.close()
        self.connection.commit()
    
    def getToDo(self, form=None):
        cursor = self.connection.cursor()
        query = "SELECT * FROM ToDo"
        cursor.execute(query)
        data = cursor.fetchall()
        cursor.close()
        self.connection.commit()
        return self.format(data, form)
    
    def getToDoByOrderAlphObj(self, form=None, inverse=False):
        cursor = self.connection.cursor()
        query = f"SELECT * FROM ToDo ORDER BY objective {'DESC' if inverse else ''}"
        cursor.execute(query)
        data = cursor.fetchall()
        cursor.close()
        self.connection.commit()
        return self.format(data, form)
    
    def getToDoCompletedOrStartByMake(self, form=None):
        cursor = self.connection.cursor()
        query = "SELECT * FROM ToDo WHERE completed = 'T' OR objective LIKE 'Make%' "
        cursor.execute(query)
        data = cursor.fetchall()
        cursor.close()
        self.connection.commit()
        return self.format(data, form)

    def getTwoToDo(self, form=None, start="start"):
        cursor = self.connection.cursor()
        query = f"SELECT * FROM ToDo {'ORDER BY id DESC' if start=='end' else ''} LIMIT 2"
        cursor.execute(query)
        data = cursor.fetchall()
        cursor.close()
        self.connection.commit()
        return self.format(data, form)

    def getAllObjective(self, form=None):
        cursor = self.connection.cursor()
        cursor.execute("SELECT objective FROM ToDo")
        data = cursor.fetchall()
        cursor.close()
        self.connection.commit()
        return self.format(data, form)

    def getAllObjectiveCompleted(self, form=None):
        cursor = self.connection.cursor()
        cursor.execute("SELECT objective FROM ToDo WHERE completed='T'")
        data = cursor.fetchall()
        cursor.close()
        self.connection.commit()
        return self.format(data, form)
    
    def getAllObjectiveCompletedAndStartByMake(self, form=None):
        cursor = self.connection.cursor()
        cursor.execute("SELECT objective FROM ToDo WHERE completed='T' AND objective LIKE 'Make%' ")
        data = cursor.fetchall()
        cursor.close()
        self.connection.commit()
        return self.format(data, form)

    def updateComplete(self, id):
        cursor = self.connection.cursor()
        concurrentCompleted = self.getDataFromId(id)['completed']
        query = f"UPDATE ToDo SET completed='{'T' if concurrentCompleted == 'F' else 'F'}' WHERE id={id}"
        cursor.execute(query)
        cursor.close()
        self.connection.commit()
    
    def getDataFromId(self, id):
        cursor = self.connection.cursor()
        cursor.execute(f"SELECT * FROM ToDo WHERE id={id}")
        data = cursor.fetchone()
        cursor.close()
        self.connection.commit()
        return dict(data)
    
    def deleteFromId(self, id):
        cursor = self.connection.cursor()
        query = f"DELETE FROM ToDo WHERE id={id}"
        cursor.execute(query)
        cursor.close()
        self.connection.commit()

    def makeQuery(self, query : str) -> None:
        cursor = self.connection.cursor()
        cursor.execute(query)
        cursor.close()
        self.connection.commit()
    
    def format(self, datas, form):
        match form:
            case None: return datas
            case "tuple": return [tuple(data) for data in datas]
            case "dict": return [dict(data) for data in datas]
            case "list": return [list(data) for data in datas]
        return datas