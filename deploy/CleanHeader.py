# /usr/bin/env python3
# -*- coding:UTF-8 -*-
# Author DongJie.Han

import sys,os;
from DB import RedisConnect;
from DB import SqlCons;
from GetWorkDir import GetCurrentWorkDir;

'''
删除指定的REDIS数据
'''
class CleanRedisKey:
    def __init__(self):
        self.command = 'CLEAN_REDIS_HEADER_KEY';
    
    '''
    删除指定的数据
    '''
    def cleanKey(self):
        if len( sys.argv ) > 1 and sys.argv[1] is not None:
            strKeyHeader = str( sys.argv[ 1 ] );
        else:
            print( "The first param is required not empty!!!" );
            sys.exit();
            
        redisConn = RedisConnect().getConn();
        
        #拉取dispute list的数据
        arrKeys = redisConn.keys( strKeyHeader + "*" );
        iLen = len( arrKeys );
        
        if iLen > 0:
            for i in range( iLen ):
                strKey = arrKeys[ i ].strip().decode();
                bRes = redisConn.delete( strKey );
                
                if bRes and bRes is not None:
                    print( "第 " + str( i + 1 ) + " 条 删除成功 键名为 " + strKey );
                else:
                    print( "第 " + str( i + 1 ) + " 条 删除失败 键名为 " + strKey );
        else:
             print( "没有该键在redis中的相关数据" );
             
        
#将redis中的列表数据取出写入到mysqlDB
CleanRedisKey().cleanKey();