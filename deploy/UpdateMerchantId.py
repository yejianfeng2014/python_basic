# /usr/bin/env python3
# -*- coding:UTF-8 -*-
# Auther DongJie.Han

import sys,os;
import threading;
from DB import RedisConnect;
from DB import SqlCons;
from GetWorkDir import GetCurrentWorkDir;

'''
开始执行线程相关任务
'''
class UpdateMerchantTask(threading.Thread):
    threadId = None;
    threadName = None;
    workDir = None;
    siteId = None;
    env = None;
    workDirs = {
        'local' : '/data/www/cs_out_site',
        'production' : '/export/data/tomcatRoot/customer.orderplus.com'
    };
    
    def __init__(self, threadId, threadName, iSiteId = None):
        self.env = os.getenv( 'APP_ENV' );
        threading.Thread.__init__(self); #初始化父线程
        self.threadId = threadId;
        self.threadName = threadName;
        self.siteId = str(iSiteId);
        
    def run(self):
        os.chdir( self.workDirs[ self.env ] );
        strCmd = "php artisan disputes update_merchant_id ";
        
        if self.siteId is not None:
            strCmd += self.siteId;
        
        os.system( strCmd );

'''
开始拉取列表相关数据
'''
class UpdateMerchantNO:
    command = None;

    def __init__(self):
        self.command = 'UPDATE_MERCHANT_IDS';

    def getPrefix(self):
        return 'bt_';
    
    def getCfgPaypalSites(self):
        strSql = "SELECT site_id FROM " + self.getPrefix() + "paypal_account WHERE pp_dispute_status = %s AND ";
        strSql += "pp_client_id <> %s AND pp_secret <> %s";
        #strSql += " AND pp_merchant_id = %s";
        tupleParam = ( 1, '0', '0' );
        dbData = SqlCons().fetchSqlData(strSql,tupleParam);
        
        return dbData;

    def execUpdateMerechantId(self):
        updateMerchantIds = {};
        arrSites = self.getCfgPaypalSites();

        if len( sys.argv ) > 1 and sys.argv[1] is not None:
            arrSites = [ { 'site_id': int( sys.argv[ 1 ] ) } ];

        if len( arrSites ) > 0:
            for i in range( len( arrSites ) ):
                updateMerchantIds[ 'update_merchant_' + str( i + 1 ) ] = UpdateMerchantTask( ( i + 1 ), "update_merchant_thread_" + str( i + 1 ), arrSites[i]['site_id'] );
                updateMerchantIds[ 'update_merchant_' + str( i + 1 ) ].start();
            
            for i in range( len( arrSites ) ):
                updateMerchantIds[ 'update_merchant_' + str( i + 1 ) ].join();

        print( "主线程退出" );

#执行拉取的任务
UpdateMerchantNO().execUpdateMerechantId();