from flask_restful import Resource
from model.item import ItemModel
from model.article import ArticleModel

class Item(Resource):
    def get(self):
        all_item = ArticleModel.find_all_item()
        result = []
        for item in all_item:
            item = ItemModel(item)
            print(item.name)
            print(item.amount())
            result.append({'item' : item.name , 'item_amount' : item.amount()})
            print(result)
        return {'itemList' : result}



