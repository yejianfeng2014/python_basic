# /usr/bin/env python3
# -*- coding:UTF-8 -*-
# Auther DongJie.Han

import sys, os;
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

        os.system(strCmd);


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

        # os.system( strCmd );

        print("php run")


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
        os.system(strCmd);


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

        # 获取redise 链接
        redisConn = RedisConnect().getConn();

        redisConn.delete('pf_already_insert_to_redis_disputes');

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

        # for i in range(iTNums):
        #     update_failed_case['update_failed_case_thread_' + str(i + 1)] = UpdateFailedCaseTask((i + 1),
        #                                                                                          "update_failed_case_thread_" + str(
        #                                                                                              i + 1));
        #     update_failed_case['update_failed_case_thread_' + str(i + 1)].start();
        #     time.sleep(3);
        iMaxNum = 30  # 一次启动的最大线程数

        # todo 核对是否启动的最大线程数是30

        temp_alives = []

        for i in range(iTNums):
            # less 30 inert into temp_alives
            if (len(temp_alives) < iMaxNum):

                t = UpdateFailedCaseTask((i + 1),
                                         "update_failed_case_thread_" + str(
                                             i + 1));

                update_failed_case['update_failed_case_thread_' + str(i + 1)] = t
                t.start()

                time.sleep(3)
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
                            t = UpdateFailedCaseTask((i + 1),
                                                     "update_failed_case_thread_" + str(
                                                         i + 1));

                            update_failed_case['update_failed_case_thread_' + str(i + 1)] = t
                            t.start()
                            temp_alives.append(t)
                            temwhile = False
                            break

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
        iMaxNum = 30
        temp_alives = []
        if iThreadNums > 0:
            for i in range(iThreadNums):
                # less 30 inert into temp_alives
                if len(temp_alives) < iMaxNum:
                    t = SaveDisputesTask((i + 1), "save_disputes_thread_" + str(i + 1), iSiteId)
                    save_disputes['save_disputes_thread_' + str(i + 1)] = t
                    t.start()
                    temp_alives.append(t)
                else:
                    temwhile = True
                    while True:
                        if temwhile is False:
                            break
                        for temp in range(len(temp_alives)):
                            if temp_alives[temp].is_alive() is False:
                                temp_alives.pop(temp)
                                t = SaveDisputesTask((i + 1), "save_disputes_thread_" + str(i + 1), iSiteId)
                                save_disputes['save_disputes_thread_' + str(i + 1)] = t
                                t.start()
                                temp_alives.append(t)
                                temwhile = False
                                break
            # print("all thread",len(get_disputes))

            for i in range(iThreadNums):
                save_disputes['save_disputes_thread_' + str(i + 1)].join()

        # The latest update time
        self.fillUpdateTime(sid);

        if sid is None and iTNums is None:
            print("Redis to mysql database 主线程退出");


if __name__ == '__main__':
    # 执行拉取列表的任务
    GetDisputesList().execGetDisputes();
    # 将redis中的列表数据取出写入到mysqlDB
    DisputeToDB().execDisputeToDB();
