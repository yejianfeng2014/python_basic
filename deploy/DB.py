# /usr/bin/env python3
# -*= coding:UTF-8 -*-
# Author:DongJie.Han
import sys,os;
# import pymysql;
import redis;

'''
Redis相关操作
'''
class RedisConnect:
    redisConn = None;
    env = None;
    
    redisConf = {
        'production' : {
            'host' : 'r-rj920afd62762f74.redis.rds.aliyuncs.com',
            'port' : '6379',
            'passwd' : 'Kfwx5uGVkv',
            'db' : 1,
        },
        
        'local' : {
            'host' : '82e36baa51ae',
            'port' : '6379',
            'passwd' : None,
            'db' : 1,
        }
    };
    
    def __init__(self):
        self.env = os.getenv( 'APP_ENV' );
        
        self.redisConn = redis.Redis( 
            self.redisConf[ self.env ][ 'host' ],
            self.redisConf[ self.env ][ 'port' ],
            self.redisConf[ self.env ][ 'db' ],
            self.redisConf[ self.env ][ 'passwd' ]
        );
        
    def getConn(self):
        return self.redisConn;

'''
数据库相关连接以及配置
'''
class SqlCons:
    sqlConn = None;
    sqlCursor = None;
    env = None;

    sqlDBCfg = {
        'production' : {
            'host' : 'rm-rj98c71x17f6e2rw2.mysql.rds.aliyuncs.com',
            'username' : 'orderplus',
            'passwd' : 'qjuTh9YIvaemnbd3',
            'db' : 'email_webmail_one',
            'port' : 3306,
        },
        
        'local' : {
            'host' : '172.21.1.31',
            'username' : 'root',
            'passwd' : '12354',
            'db' : 'email_webmail_one',
            'port' : 3306,
        }
    };
    
    def __init__(self):
        self.env = os.getenv( 'APP_ENV' );

        self.sqlConn = pymysql.connect( 
            host = self.sqlDBCfg[ self.env ][ 'host' ], 
            user = self.sqlDBCfg[ self.env ][ 'username' ], 
            passwd = self.sqlDBCfg[ self.env ][ 'passwd' ], 
            db = self.sqlDBCfg[ self.env ][ 'db' ], 
            port = self.sqlDBCfg[ self.env ][ 'port' ],
            charset = "utf8",
            cursorclass = pymysql.cursors.DictCursor
        );
        
        self.sqlCursor = self.sqlConn.cursor();
    
    def getPrefix(self):
        return 'bt_';

    def executeSql(self, strSql):
        return self.sqlCursor.execute( strSql );
    
    def getCnt(self,strSql):
        cntData = self.fetchSqlData(strSql);
        return cntData[0][0];
    
    def fetchSqlData(self, strSql, tupleParam):
        self.sqlCursor.execute( strSql, tupleParam );
        return self.sqlCursor.fetchall();
    
    def __del__(self):
        self.sqlCursor.close();
        self.sqlConn.commit();
        self.sqlConn.close();
