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
        self.command = 'DISPUTE_TO_MYSQL_DB';
    
    '''
    删除指定的数据
    '''
    def cleanKey(self):
        if len( sys.argv ) > 1 and sys.argv[1] is not None:
            iSiteId = str( sys.argv[ 1 ] );
        else:
            print( "Site id must be required and must int not empty!!!" );
            sys.exit();
            
        redisConn = RedisConnect().getConn();
        
        #清除从paypal拉到redis中的dispute键
        if redisConn.delete( "pf_already_insert_to_redis_disputes_" + iSiteId ):
            print( "删除成功 键名为 pf_already_insert_to_redis_disputes_" + iSiteId );
        else:
            print( "删除失败 键名为 pf_already_insert_to_redis_disputes_" + iSiteId );
        
        if redisConn.delete( "pf_already_update_to_db_disputes_" + iSiteId ):
            print( "删除成功 键名为 pf_already_update_to_db_disputes_" + iSiteId );
        else:
            print( "删除失败 键名为 pf_already_update_to_db_disputes_" + iSiteId );
        
        if redisConn.delete( "h_paypal_account_" + iSiteId ):
            print( "删除成功 键名为 h_paypal_account_" + iSiteId );
        else:
            print( "删除失败 键名为 h_paypal_account_" + iSiteId );
        
        if redisConn.delete( "h_paypal_access_token_" + iSiteId ):
            print( "删除成功 键名为 h_paypal_access_token_" + iSiteId );
        else:
            print( "删除失败 键名为 h_paypal_access_token_" + iSiteId );
        
        if redisConn.srem( "s_site_accounts_set", "h_paypal_account_" + iSiteId ):
            print( "从站点集合移除成功 键名为 h_paypal_account_" + iSiteId );
        else:
            print( "从站点集合移除失败 键名为 h_paypal_account_" + iSiteId );
        
        #拉取dispute list的数据
        arrKeys = redisConn.keys("h_disputes_list_" + iSiteId + "_*");
        iLen = len( arrKeys );
        
        if iLen > 0:
            for i in range( iLen ):
                strKey = arrKeys[ i ].strip().decode();
                bRes = redisConn.delete( strKey );
                
                if bRes and bRes is not None:
                    print( "删除dispute列表数据 第 " + str( i + 1 ) + " 条 删除成功 键名为 " + strKey );
                else:
                    print( "删除dispute列表数据 第 " + str( i + 1 ) + " 条 删除失败 键名为 " + strKey );
        else:
             print( "没有该键在redis中的相关数据" );
             
        
#将redis中的列表数据取出写入到mysqlDB
CleanRedisKey().cleanKey();