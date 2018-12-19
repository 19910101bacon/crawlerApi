from flask_restful import Resource, reqparse
from model.item import ItemModel

class Article(Resource):
    
    def get(self, item_name, id):
        result = ItemModel.find_by_item(item_name)
        if id <= len(result):
            result = result[id - 1].__dict__
            keys = ['title', 'item', 'source', 'date', 'content']
            result = {key : result[key]  for key in keys}
            print(result)
            return {'content' :result} 
        return {"message" : "That item's article do not enough, please cut down id number"} 


