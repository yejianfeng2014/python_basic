# /usr/bin/env python3
# -*- coding:UTF-8 -*-
# Author DongJie.Han

import sys,os;
from DB import RedisConnect;
from DB import SqlCons;
from GetWorkDir import GetCurrentWorkDir;

'''
保存指定的dispute id数据到mysql中
'''
class SaveOneDispute:
    def __init__(self):
        self.command = 'SAVE_ONE_DISPUTE';
    
    '''
    删除指定的数据
    '''
    def updateOne(self):
        if len( sys.argv ) > 2 and sys.argv[1] is not None and sys.argv[2] is not None:
            iSiteId = str( sys.argv[ 1 ] );
            strDisputeId = str( sys.argv[ 2 ] );
            
            os.chdir( GetCurrentWorkDir().getDir() );
            strCmd = "php artisan disputes update_one_dispute " + iSiteId + " " + strDisputeId;
            
            os.system( strCmd );
        else:
            print( "Site id and dispute id must be required not empty!!!" );
            sys.exit();

#将redis中的列表数据取出写入到mysqlDB
SaveOneDispute().updateOne();