from flask_restful import Resource
from model.item import ItemModel
from model.article import ArticleModel

class Item(Resource):
    def get(self):
        all_item = ArticleModel.find_all_item()
        result = {}
        for item in all_item:
            item = ItemModel(item)
            result.update({'itemList' : item.name , 'item_amount' : item.amount()})
        return {'item' : result}



