# -*- coding: utf-8 -*-

import datetime
import json

from flask import request

from .log_store import ESStore

__version__ = '0.1'
__versionfull__ = __version__


def parse_meta_info_from_req(real_request):
    log_dict = {}
    
    log_dict["host"] = real_request.headers.get('Host')
    log_dict["remote_addr"] = real_request.remote_addr
    log_dict["user_agent"] = real_request.headers.get('User-Agent')
    log_dict["full_endpoint"] = real_request.full_path
    log_dict["is_ajax"] = real_request.is_xhr
    log_dict["http_method"] = real_request.method
    log_dict["timestamp"] = str(datetime.datetime.utcnow())
    log_dict["http_referrer"] = real_request.referrer
    
    return log_dict
    

def parse_meta_info_from_response(response_obj):
    resp_dict = {}
    resp_dict["data"] = response_obj.data.decode(response_obj.charset)
    resp_dict["status_code"] = response_obj.status_code
    return resp_dict
    

class RouteLoggerException(Exception):
    '''
    Router Logger Exception Which doesnot affect the flask application if any error throws through this
    @note: RouteLoggerException handler is silent boy
    '''
    def __init__(self, *args, **kwargs):
        print "I think Storage class is not found"


class RouteLogger(object):
    '''
    '''
    def __init__(self, app=None, with_jinja2_ext=True, config=None, log_everything=False):
        if not (config is None or isinstance(config, dict)):
            raise ValueError("`config` must be an instance of dict or None")

        self.with_jinja2_ext = with_jinja2_ext
        self.config = config
        self.log_all = log_everything

        self.app = app
        if app is not None:
            self.init_app(app, config)
            
    def init_app(self, app, config):
        '''
        '''
        base_config = app.config.copy()
        if self.config:
            base_config.update(self.config)
        if config:
            base_config.update(config)
        config = base_config
        
        config.setdefault('LOG_BACKEND', 'elasticsearch')
        config.setdefault('LOG_INDEX', 'route_loggerv1.0')
        config.setdefault('EXCLUDE_ROUTES', [])
        config.setdefault('INCLUDE_ROUTES', [])
        
        self.app = app
        self.config = config
        self.load_storage_class()
        self._do_logging(app, config)
    
    def load_storage_class(self):
        if self.config['LOG_BACKEND'].lower() == 'elasticsearch':
            self.writer_obj = ESStore(self.config["LOG_INDEX"])
            return
        
        raise RouteLoggerException("No Storage Class Found to write log message")
    
    def does_route_allowed(self, route_path):
        if self.log_all:
            return True
        
        return route_path in self.config["INCLUDE_ROUTES"] and route_path not in self.config["EXCLUDE_ROUTES"]
    
    def _do_logging(self, app, config):
        app.before_request(self._process_request)
        app.after_request(self._process_response)
        app.teardown_request(self._teardown_request)
        
    def _process_request(self):
        real_request = request._get_current_object()
        meta_data_as_dict = parse_meta_info_from_req(real_request)
        meta_data_as_dict['request_action'] = "_BEFORE_REQUEST_"
        
        if self.does_route_allowed(real_request.path):
            self.store_meta_fields(meta_data_as_dict, level="INFO")
           
    def _process_response(self, response):
        real_request = request._get_current_object()
        meta_data_as_dict = parse_meta_info_from_req(real_request)
        meta_resp_as_dict = parse_meta_info_from_response(response)
        meta_data_as_dict.update(meta_resp_as_dict)
        meta_data_as_dict['request_action'] = "_AFTER_RESPONSE_"
        
        if self.does_route_allowed(real_request.path):
            self.store_meta_fields(meta_data_as_dict, level="INFO")
            
        return response
        
    def _teardown_request(self, exc_msg):
        if exc_msg:
            real_request = request._get_current_object()
            meta_data_as_dict = parse_meta_info_from_req(real_request)
            meta_data_as_dict['exception_message'] = exc_msg
            meta_data_as_dict['request_action'] = "_EXCEPTION_"
            if self.does_route_allowed(real_request.path):
                self.store_meta_fields(meta_data_as_dict, level="ERROR")
                
        return exc_msg
    
    def store_meta_fields(self, input_fields, level="INFO"):
        '''
        @param: input_fields:
            :@param request_action: helpful to query based on the constant string
        '''
        input_fields['level'] = level
        self.writer_obj.write(input_fields)
    
    
    