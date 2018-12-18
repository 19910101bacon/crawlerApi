from model.article import ArticleModel

class ItemModel():
    def __init__(self, item):
        self.name = item


    @classmethod
    def find_by_item(cls, item):
        result = ArticleModel.query.filter_by(item = item).all()
        if result:
            return result
        return {"message" : "{item} do not find in database's item column, maybe it is not regular token nor you haven't start crawler api".format(item = item)}

    def titles(self, limit = 10):
        return [row.title for row in self.find_by_item(self.name)[0: limit]] 
            
    def amount(self):
        return len(self.find_by_item(self.name))



