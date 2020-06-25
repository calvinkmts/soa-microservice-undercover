from nameko.rpc import rpc, RpcProxy

import dependencies
import schemas


class WordService:
    name = 'word_service'
    database = dependencies.Database()

    def __init__(self):
        print("Service Constructor")

    ### WORDPACK ###
    @rpc
    def create_wordpack(self, data):
        result = {
            'err': 0,
            'msg': 'Wordpack Created'
        }
        self.database.create_wordpack(data)
        return schemas.CommandResultSchema().dumps(result)

    @rpc
    def update_wordpack(self, data):
        result = {
            'err': 0,
            'msg': 'Wordpack Updated'
        }
        if self.database.get_wordpack_by_id(data['id']):
            self.database.update_wordpack(data)
        else:
            result['err'] = 1
            result['msg'] = 'Wordpack Not Found'
        return schemas.CommandResultSchema().dumps(result)

    @rpc
    def delete_wordpack(self, data):
        result = {
            'err': 0,
            'msg': 'Wordpack Deleted'
        }
        if self.database.get_wordpack_by_id(data['id']):
            self.database.delete_wordpack(data)
        else:
            result['err'] = 1
            result['msg'] = 'Wordpack Not Found'
        return schemas.CommandResultSchema().dumps(result)

    @rpc
    def get_all_wordpack(self):
        result = self.database.get_all_wordpack()
        return schemas.WordpackSchema(many=True).dump(result)

    @rpc
    def get_wordpack_by_id(self, data):
        result = self.database.get_wordpack_by_id(data['id'])
        return schemas.WordpackSchema().dump(result)

    @rpc
    def search_wordpack(self, data):
        result = self.database.search_wordpack(data['keyword'])
        return schemas.WordpackSchema(many=True).dump(result)

    ### WORDPAIR###
    @rpc
    def create_wordpair(self, data):
        result = {
            'err': 0,
            'msg': 'Wordpair Added'
        }
        if self.database.get_wordpack_by_id(data['id_word_pack']):
            self.database.create_wordpair(data)
        else:
            result['err'] = 1
            result['msg'] = 'Wordpack Not Found'
        return schemas.CommandResultSchema().dumps(result)

    @rpc
    def update_wordpair(self, data):
        result = {
            'err': 0,
            'msg': 'Wordpair Updated'
        }
        if self.database.get_wordpair_by_id(data['id']):
            self.database.update_wordpair(data)
        else:
            result['err'] = 1
            result['msg'] = 'Wordpair Not Found'
        return schemas.CommandResultSchema().dumps(result)

    @rpc
    def delete_wordpair(self, data):
        result = {
            'err': 0,
            'msg': 'Wordpair Deleted'
        }
        if self.database.get_wordpair_by_id(data['id']):
            self.database.delete_wordpair(data)
        else:
            result['err'] = 1
            result['msg'] = 'Wordpair Not Found'
        return schemas.CommandResultSchema().dumps(result)

    @rpc
    def get_all_wordpair(self):
        result = self.database.get_all_wordpair()
        return schemas.WordpairSchema(many=True).dump(result)

    @rpc
    def get_wordpair_by_id(self, data):
        result = self.database.get_wordpair_by_id(data['id'])
        return schemas.WordpairSchema().dump(result)

    @rpc
    def get_all_wordpair_by_wordpack_id(self, data):
        result = self.database.get_all_wordpair_by_wordpack_id(data['id'])
        return schemas.WordpairSchema(many=True).dump(result)
    
    @rpc
    def get_wordpair_by_wordpack_id(self, data):
        result = self.database.get_wordpair_by_wordpack_id(data['id'])
        return schemas.WordpairSchema().dump(result)
        
    def __del__(self):
        print("Service Destructor")
