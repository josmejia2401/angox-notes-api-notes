from src.main.utils.core import ControllerDataBase
from src.main.utils.core import ConfigDTO
from src.main.dto.dto import NoteDTO


class Controller1(ControllerDataBase):

    def __init__(self, config: ConfigDTO = None):
        ControllerDataBase.__init__(self, config, 'nn_notes_notes')

    def create(self, payload=None) -> any:
        note_dto = NoteDTO(payload)
        note_dto.validate(['accountId', 'title', 'content'])
        response = self.get_service().create(note_dto.to_json())
        return response

    def update(self, id=None, payload=None, upsert=False) -> any:
        note_dto = NoteDTO(payload, True, True)
        note_dto.validate(['accountId', 'title', 'content'])
        response = self.get_service().update(id, note_dto.to_json(), upsert)
        return response

    def delete(self, id=None) -> int:
        if id is None or not id:
            raise Exception('the ID is not found')
        response = self.get_service().delete(id)
        return response

    def get(self, id=None) -> any:
        if id is None or not id:
            raise Exception('the ID is not found')
        response = self.get_service().get(id)
        return response

    def get_all(self, accountId=None, orderBy=None, offset=None, limit=None) -> any:
        if accountId is None or not accountId:
            raise Exception('the ID is not found')
        if orderBy:
            orderBy = [(orderBy, -1)]
        response = self.get_service().get_many(payload_where={'accountId': accountId}, order_by=orderBy, offset=offset, limit=limit)
        return response
