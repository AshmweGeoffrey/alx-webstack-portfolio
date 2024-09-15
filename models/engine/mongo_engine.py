from mongoengine import connect,disconnect,Document

class MongoStorage:
    __engine = None
    __session = None
    def __init__(self):
        self.__engine = connect('Ax', host='localhost', port=27017)
        self.engine = self.__engine
    def save(self,document):
        # Call the save method directly on the document
        if isinstance(document, Document):
            document.save()
        else:
            raise TypeError("document must be an instance of mongoengine.Document")
    def close(self):
        disconnect()