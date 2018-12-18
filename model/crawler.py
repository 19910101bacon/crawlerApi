from model.article import ArticleModel

def crawlerFunction(item, first_day, last_day):    
    for i in range(20):

        article = ArticleModel('abcde' + str(i) , item, 'google', '20180715', 'zxcvbnmsdfghjkrtyuiortyudsfysd9fys0d9yfsdyf9syd9fsd98yf' + str(i**2))
        article.save_to_data()


