from src.main.utils.core import DTO
import datetime

class NoteDTO(DTO): 
    def __init__(self, dataAsJson={}, ignored_none=False, update=False):
        DTO.__init__(self, dataAsJson, ignored_none)
        self.accountId = None
        self.title = None
        self.content = None
        self.favorite = None
        self.category = None
        self.updateAt = datetime.datetime.utcnow()
        self.createAt = None
        if update == False:
            self.createAt = datetime.datetime.utcnow()
        if dataAsJson is None:
            return
        if 'accountId' in dataAsJson and dataAsJson['accountId']:
            self.accountId = dataAsJson['accountId']
        if 'title' in dataAsJson and dataAsJson['title']:
            self.title = dataAsJson['title']
        if 'content' in dataAsJson and dataAsJson['content']:
            self.content = dataAsJson['content']
        if 'favorite' in dataAsJson and dataAsJson['favorite']:
            self.favorite = dataAsJson['favorite']
        if 'category' in dataAsJson and dataAsJson['category']:
            self.category = dataAsJson['category']
