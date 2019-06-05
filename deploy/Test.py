# /usr/bin/env python3
# -*-coding:UTF-8-*-
# Author:DongJie.Han

from DB import RedisConnect;
from DB import RedisConnect;
from GetWorkDir import GetCurrentWorkDir;

redisConn = RedisConnect().getConn();
print( redisConn.get( 'stu_name' ).strip().decode() );
print( GetCurrentWorkDir().getDir() );