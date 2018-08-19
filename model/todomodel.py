from model import db
class TodoModel:
    todoCollecton = db["Todo"]
    def __init__(self, text, completed, completedAt):
        self.text = text
        self.completed = completed
        self.completedAt = completedAt

    def json(self):
        return {'text' : self.text ,'completed' :self.completed ,"completedAt":self.completedAt }

    def update_to_db(self):
        self.todoCollecton.update({'text':self.text}, {"$set": self.json()})

    def save_to_db(self):
         self.todoCollecton.insert(self.json())

    @classmethod
    def find_by_name(self,name):
        returnList = []
        for todo in self.todoCollecton.find({'text':name}):
            returnList.append(
                {'text': todo['text'], 'completed': todo['completed'], 'completedAt': todo['completedAt']})
        return returnList

    @classmethod
    def find_all(self):
        returnList = []
        for todo in  self.todoCollecton.find({}):
            returnList.append({'text' : todo['text'],'completed' : todo['completed'],'completedAt':todo['completedAt']})
        return  returnList