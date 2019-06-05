# /usr/bin/env python3
# -*- coding:UTF-8 -*-
# Auther DongJie.Han

import sys,os;
import threading;
import pymysql;
from DB import RedisConnect;
from DB import SqlCons;
from GetWorkDir import GetCurrentWorkDir;
import time;
import pytz;
import datetime;
from time import sleep
from math import ceil

'''
开始执行线程相关任务
'''


class GetDisputesTask(threading.Thread):
    threadId = None;
    threadName = None;
    workDir = None;
    siteId = None;

    def __init__(self, threadId, threadName, iSiteId=None):
        threading.Thread.__init__(self);  # 初始化父线程
        self.threadId = threadId;
        self.threadName = threadName;
        self.siteId = str(iSiteId);

    def run(self):
        os.chdir(GetCurrentWorkDir().getDir());
        strCmd = "php artisan disputes start_dispute_service ";

        if self.siteId is not None:
            strCmd += self.siteId;

        os.system( strCmd );


'''
异步多线程将dispute数据从redis中写入到mysql数据库
'''


class SaveDisputesTask(threading.Thread):
    threadId = None;
    threadName = None;
    siteId = None;

    def __init__(self, threadId, threadName, iSiteId=None):
        threading.Thread.__init__(self);  # 初始化父线程
        self.threadId = threadId;
        self.threadName = threadName;
        self.siteId = iSiteId;

    def run(self):
        os.chdir(GetCurrentWorkDir().getDir());
        strCmd = "php artisan disputes save_dispute_service";

        if self.siteId is not None:
            strCmd += " " + self.siteId;

        '''    
        strDate = str( time.strftime("%Y%m%d") );
        strLogFile = "/tmp/save_disputes_to_mysql_db_" + strDate + ".log";
        
        if os.path.exists( strLogFile ):
            open( strLogFile, 'w+' );
        
        strCmd += " >> " + strLogFile + " &";
        '''

        os.system( strCmd );

'''
异步多线程将dispute第一次更新失败的数据从redis中写入到mysql数据库
'''


class UpdateFailedCaseTask(threading.Thread):
    threadId = None;
    threadName = None;

    def __init__(self, threadId, threadName):
        threading.Thread.__init__(self);  # 初始化父线程
        self.threadId = threadId;
        self.threadName = threadName;

    def run(self):
        os.chdir(GetCurrentWorkDir().getDir());
        strDate = str(time.strftime("%Y%m%d"));
        strLogFile = "/tmp/update_failed_case_" + strDate + ".log";

        if os.path.exists(strLogFile):
            open(strLogFile, 'w+');

        strCmd = "php artisan disputes update_failed_case >> " + strLogFile + " &";
        os.system( strCmd );

'''
开始拉取列表相关数据
'''


class GetDisputesList:
    command = None;

    def __init__(self):
        self.command = 'GET_DISPUTES_LIST';

    def getPrefix(self):
        return 'bt_';

    def getCfgPaypalSites(self):
        strSql = "SELECT site_id FROM " + self.getPrefix() + " paypal_account WHERE pp_dispute_status = %s AND ";
        strSql += "pp_client_id <> %s AND pp_secret <> %s";
        # strSql += " AND pp_merchant_id = %s";

        # todo  既然是常亮为什么不直接写入sql语句中，
        tupleParam = (1, '0', '0');
        dbData = SqlCons().fetchSqlData(strSql, tupleParam);

        return dbData;

    def execGetDisputes(self, iSiteId=None):
        get_disputes = {};

        if iSiteId is not None:
            arrSites = [{'site_id': int(iSiteId)}];
        elif len(sys.argv) > 1 and sys.argv[1] is not None and int(sys.argv[1]) > 0:
            arrSites = [{'site_id': int(sys.argv[1])}];
        else:
            arrSites = self.getCfgPaypalSites()

        # arrSites = [{'site_id': 1},
        #             {'site_id': 2},
        #             {'site_id': 3},
        #             {'site_id': 4},
        #             {'site_id': 5},
        #             {'site_id': 6},
        #             {'site_id': 7},
        #             {'site_id': 8},
        #             {'site_id': 9},
        #             {'site_id': 10},
        #             {'site_id': 11},
        #             {'site_id': 12},
        #             {'site_id': 13},
        #             {'site_id': 14},
        #             {'site_id': 15},
        #             {'site_id': 16},
        #             {'site_id': 17},
        #             {'site_id': 18},
        #             {'site_id': 19},
        #             {'site_id': 20},
        #             {'site_id': 21},
        #             {'site_id': 22},
        #             {'site_id': 23},
        #             {'site_id': 24},
        #             {'site_id': 25},
        #             {'site_id': 26},
        #             {'site_id': 27},
        #             {'site_id': 28},
        #             {'site_id': 29},
        #             {'site_id': 30},
        #             {'site_id': 31},
        #             {'site_id': 32},
        #             {'site_id': 33},
        #             {'site_id': 34},
        #             {'site_id': 35},
        #             {'site_id': 36},
        #             {'site_id': 37},
        #             {'site_id': 38},
        #             {'site_id': 39},
        #             {'site_id': 40},
        #             {'site_id': 41},
        #             {'site_id': 42},
        #             {'site_id': 43},
        #             {'site_id': 44},
        #             {'site_id': 45},
        #             {'site_id': 46},
        #             {'site_id': 47},
        #             {'site_id': 48},
        #             {'site_id': 49},
        #             {'site_id': 50},
        #             {'site_id': 51},
        #             {'site_id': 52},
        #             {'site_id': 53},
        #             {'site_id': 54},
        #             {'site_id': 55},
        #             {'site_id': 56},
        #             {'site_id': 57},
        #             {'site_id': 59},
        #             {'site_id': 60},
        #             {'site_id': 61},
        #             {'site_id': 62},
        #             {'site_id': 63},
        #             {'site_id': 64},
        #             {'site_id': 65},
        #             {'site_id': 66},
        #             {'site_id': 67},
        #             {'site_id': 68},
        #             {'site_id': 69},
        #             {'site_id': 70},
        #             {'site_id': 71},
        #             {'site_id': 72},
        #             {'site_id': 73},
        #             {'site_id': 74},
        #             {'site_id': 75},
        #             {'site_id': 76},
        #             {'site_id': 77},
        #             {'site_id': 78},
        #             {'site_id': 79},
        #             {'site_id': 80},
        #             {'site_id': 81},
        #             {'site_id': 82},
        #             {'site_id': 83},
        #             {'site_id': 84},
        #             {'site_id': 85},
        #             {'site_id': 86},
        #             {'site_id': 87},
        #             {'site_id': 88},
        #             {'site_id': 89},
        #             {'site_id': 90},
        #             {'site_id': 91},
        #             {'site_id': 92}
        #             ]

        # 获取redise 链接
        redisConn = RedisConnect().getConn();

        redisConn.delete('pf_already_insert_to_redis_disputes');

        ## todo 研究这个##############################################################################################################################

        iMaxNum = 30;  # 一次启动的最大线程数

        # todo 核对是否启动的最大线程数是30

        temp_alives = []

        for i in range(len(arrSites)):
            # less 30 inert into temp_alives
            if (len(temp_alives) < iMaxNum):
                t = GetDisputesTask((i + 1), "get_disputes_thread_" + str(i + 1), arrSites[i]['site_id'])
                get_disputes['get_disputes_thread_' + str(i + 1)] = t
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
                            t = GetDisputesTask((i + 1), "get_disputes_thread_" + str(i + 1),
                                                arrSites[i]['site_id'])
                            get_disputes['get_disputes_thread_' + str(i + 1)] = t
                            t.start()
                            temp_alives.append(t)
                            temwhile = False
                            break
        # print("all thread",len(get_disputes))

        for i in range(len(get_disputes)):
            # print("join")
            get_disputes['get_disputes_thread_' + str(i + 1)].join()

        print("pull disputes list .....主线程退出")

'''
执行从redis写入到mysql数据库
'''


class DisputeToDB:
    redisConn = None;
    siteUpdateQueue = 's_site_update_queue';

    def __init__(self):
        self.command = 'DISPUTE_TO_MYSQL_DB';
        self.redisConn = RedisConnect().getConn();

    def fillUpdateTime(self, iSiteId):
        # if len( sys.argv ) > 1 and sys.argv[1] is not None and int( sys.argv[1] ) > 0:
        self.redisConn.srem(self.siteUpdateQueue, iSiteId);
        strKey = 'h_paypal_account_' + str(iSiteId);

        current_update_time = datetime.datetime.now(pytz.timezone('Asia/Shanghai')).strftime("%Y-%m-%d %H:%M:%S");
        # redisConn.hset( strKey, 'update_time', time.strftime("%Y-%m-%d %H:%M:%S", time.localtime() ) );
        self.redisConn.hset(strKey, 'update_time', current_update_time);

    '''
    执行失败的数据拉取数据写入MYSQLDB
    '''

    def updateFailedCaseToMDB(self, iTNums):
        update_failed_case = {};
        self.redisConn.delete('pf_failed_dispute_cnt');

        for i in range(iTNums):
            update_failed_case['update_failed_case_thread_' + str(i + 1)] = UpdateFailedCaseTask((i + 1),
                                                                                                 "update_failed_case_thread_" + str(
                                                                                                     i + 1));
            update_failed_case['update_failed_case_thread_' + str(i + 1)].start();
            time.sleep(3);

        for i in range(iTNums):
            update_failed_case['update_failed_case_thread_' + str(i + 1)].join();
            time.sleep(3);

        print("Update failed case to mysql database 主线程退出");

    '''
    执行拉取数据写入MYSQLDB
    '''

    def execDisputeToDB(self, sid=None, iTNums=None):
        save_disputes = {};
        lKeys = self.redisConn.keys("h_paypal_account_*");

        # todo 这儿接受第二个参数

        if iTNums is not None:
            iThreadNums = iTNums;
        elif len(sys.argv) > 2 and sys.argv[2] is not None and int(sys.argv[2]) > 0:
            iThreadNums = int(sys.argv[2]);
        else:
            iThreadNums = len(lKeys);

        # todo 检测 iThreadNums 的大小

        if sid is not None:
            iSiteId = str(sid);
        elif len(sys.argv) > 1 and sys.argv[1] is not None and int(sys.argv[1]) > 0:
            iSiteId = str(sys.argv[1]);
        else:
            iSiteId = None;

        self.redisConn.delete('pf_already_update_to_db_disputes');

        # todo fix 这儿会起来非常多的线程

        if iThreadNums > 0:
            for i in range(iThreadNums):
                save_disputes['save_disputes_thread_' + str(i + 1)] = SaveDisputesTask((i + 1),
                                                                                       "save_disputes_thread_" + str(
                                                                                           i + 1), iSiteId);
                save_disputes['save_disputes_thread_' + str(i + 1)].start();

            for i in range(iThreadNums):
                save_disputes['save_disputes_thread_' + str(i + 1)].join();

        # The latest update time
        self.fillUpdateTime(sid);

        if sid is None and iTNums is None:
            print("Redis to mysql database 主线程退出");


if __name__ == '__main__':
    # 执行拉取列表的任务
    GetDisputesList().execGetDisputes();
    # 将redis中的列表数据取出写入到mysqlDB
    DisputeToDB().execDisputeToDB();
