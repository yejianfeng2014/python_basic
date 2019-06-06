# /usr/bin/env python3
# -*- coding:UTF-8 -*-
# Author DongJie.Han

import sys,os;
import threading;
from DB import RedisConnect;
from DB import SqlCons;
from GetWorkDir import GetCurrentWorkDir;

'''
异步拉取多线程
'''
class SaveDisputesTask(threading.Thread):
    threadId = None;
    threadName = None;
    siteId = None;
    
    def __init__(self, threadId, threadName, iSiteId = None):
        threading.Thread.__init__(self); #初始化父线程
        self.env = os.getenv( 'APP_ENV' );
        self.threadId = threadId;
        self.threadName = threadName;
        self.siteId = iSiteId;
        
    def run(self):
        os.chdir( GetCurrentWorkDir().getDir() );
        strCmd = "php artisan disputes save_dispute_service ";
        
        if self.siteId is not None:
            strCmd += self.siteId;
        
        os.system( strCmd );

'''
执行从redis写入到mysql数据库
'''
class DisputeToDB:
    def __init__(self):
        self.command = 'DISPUTE_TO_MYSQL_DB';
    
    '''
    执行拉取数据写入MYSQLDB
    '''
    def execDisputeToDB(self):
        get_disputes = {};
        redisConn = RedisConnect().getConn();
        lKeys = redisConn.keys("h_paypal_account_*");
        
        if len( sys.argv ) > 2 and sys.argv[2] is not None and int( sys.argv[2] ) > 0:
            iLen = int( sys.argv[ 2 ] );
        else:
            iLen = len( lKeys );
            
        iSiteId = None if len( sys.argv ) < 3 else sys.argv[1];
        redisConn.delete( 'pf_already_update_to_db_disputes' );
        #
        # if len( lKeys ) > 0:
        #     for i in range( iLen ):
        #         get_disputes[ 'get_disputes_thread_' + str( i + 1 ) ] = SaveDisputesTask( ( i + 1 ), "get_disputes_thread_" + str( i + 1 ), iSiteId );
        #         get_disputes[ 'get_disputes_thread_' + str( i + 1 ) ].start();


        iMaxNum = 30;  # 一次启动的最大线程数
        temp_alives = []

        if len(lKeys) > 0:

            for i in range(iLen):
                # less 30 inert into temp_alives
                if (len(temp_alives) < iMaxNum):
                    t = SaveDisputesTask( ( i + 1 ), "get_disputes_thread_" + str( i + 1 ), iSiteId )
                    get_disputes[ 'get_disputes_thread_' + str( i + 1 ) ] = t
                    t.start()
                    # alive = t.is_alive()
                    temp_alives.append(t)
                else:
                    temwhile = True
                    while True:
                        # sleep(1)  # sleep 1s

                        if temwhile is False:
                            break;

                        for temp in range(len(temp_alives)):
                            if temp_alives[temp].is_alive() is False:
                                temp_alives.pop(temp)
                                t = SaveDisputesTask((i + 1), "get_disputes_thread_" + str(i + 1), iSiteId)
                                get_disputes['get_disputes_thread_' + str(i + 1)] = t
                                t.start()
                                temp_alives.append(t)
                                temwhile = False
                                break

            for i in range( iLen ):
                get_disputes[ 'get_disputes_thread_' + str( i + 1 ) ].join();
                
        print( "主线程退出" );


#将redis中的列表数据取出写入到mysqlDB
DisputeToDB().execDisputeToDB();