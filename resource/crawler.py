from flask_restful import Resource, reqparse
from model.crawler import crawlerFunction
class Crawler(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('item',
            type = str,
            required = True,
            help = "This field cannot be blank"
            )
    parser.add_argument('first_day',
            type = str,
            required = True,
            help = "This field cannot be blank"
            )
    parser.add_argument('last_day',
            type = str,
            required = str,
            help = "This field cannot be blank"
            )

    def post(self):
        data = Crawler.parser.parse_args()
        if int(data['first_day'] > data['last_day']):
            return {"message" : "wrong date format"}
        
        crawlerFunction(data['item'], data['first_day'], data['last_day'])
        return {"message" : "crawling about {item} complete".format(item = data['item'])}



