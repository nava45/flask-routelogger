# -*- coding: utf-8 -*-
import abc

from elasticsearch import Elasticsearch


class LogStore(object):
    '''
    Store the structured log fields in the given storage backend
    like elastic search, mongodb, filesystem
    '''
    __metaclass__ = abc.ABCMeta
    
    @abc.abstractmethod
    def write(self, field_dict):
        pass
    
    
class ESStore(LogStore):
    '''
    Elastic search is the backend for log storage
    '''
    
    def __init__(self, index, doc_type='v1', host="localhost", port=9200):
        self.index = index
        self.doc_type = doc_type
        self.host = host
        self.port = port
        
        self.conn = None
        self.conn = self.get_connection()
    
    def __connect(self):
        return Elasticsearch(host=self.host, port=self.port)
    
    def get_connection(self):
        if not self.conn:
            self.conn = self.__connect()
        return self.conn
    
    def write(self, field_dict):
        result = self.conn.index(index=self.index, doc_type=self.doc_type,
                                 body=field_dict)
        

class MongoStore(LogStore):
    def write(self, field_dict):
        pass
    
    
class FileSystemStore(LogStore):
    def write(self, field_dict):
        pass
    
    
    