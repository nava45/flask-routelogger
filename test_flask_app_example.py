import unittest
from flask_routelogger import RouteLogger
from flask import Flask

from elasticsearch import Elasticsearch


class TestFlaskRouteLogger(unittest.TestCase):
    
    def elastic_search_query(self, respon_str):
        query_dict = {"query":{"bool": {"must":[{"query_string": 
                                                {"default_field":"v1.data","query":"%s" % respon_str}}], 
                                       "must_not":[],"should":[]}}, 
                      "from":0,
                      "size":10,
                      "sort":[],"aggs":{}}
        conn = Elasticsearch(host=self.host, port=self.port)
        res = conn.search(index=self.index, q=query_dict)
        
        # @todo: Need fix here to return the indexed results
        return res
    
    def setUp(self):
        app = Flask(__name__)
        rapp = RouteLogger(app, log_everything=True)
        app.debug = True
        self.app = app
        
        self.host = "localhost"
        self.port = 9200
        self.index = "route_loggerv1.0"
        
        
    def test_home_page(self):
        sample_output = "Response is good"
        
        self.app.route('/testing')
        def home_page():
            return sample_output
        
        cli = self.app.test_client()
        res = cli.get('/')
        
        assert sample_output == res.data
        
        flag = self.elastic_search_query(sample_output)
        
        assert flag
        
        
if __name__ == '__main__':
    unittest.main()
    

