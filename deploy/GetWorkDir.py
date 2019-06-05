# /usr/bin/env python3
# -*-coding:UTF-8-*-
# Author:DongJie.Han

import os;

'''
获取当前的工作目录
'''
class GetCurrentWorkDir:
    command = None;
    env = None;
    
    workDirs = {
        'local' : '/data/www/cs_out_site',
        'production' : '/export/data/tomcatRoot/customer.orderplus.com'
    };
    
    def __init__(self):
        self.env = os.getenv( 'APP_ENV' );
        self.command = 'GET_CURRENT_WORK_DIR';
        
    def getDir(self):
        return self.workDirs[ self.env ];