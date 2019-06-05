#! /bin/bash
# cron execute update recently dispute
# Author handongjie

set -i
source ~/.bashrc
source /etc/profile

case $APP_ENV in
	"production" )
		CMDS_DIR=/export/data/tomcatRoot/customer.orderplus.com/deploy
		;;
	"testing" )
		CMDS_DIR=/export/data/tomcatRoot/customer.orderplus.com/deploy
		;;
	"local" )
		CMDS_DIR=/data/www/cs_out_site/deploy
		;;
	* )
		echo 'Environment Error!!!'
		exit
		;;
esac

pidFile=/tmp/daemon_class.pid

if [[ ! -f $pidFile ]]; then
	python3 $CMDS_DIR/Deamon.py restart
else
	pid=$(cat $pidFile)

	if [[ $pid > 0 ]]; then
		kill -0 $pid

		if [[ $? != 0 ]]; then
			python3 $CMDS_DIR/Deamon.py restart
		fi
	else
		python3 $CMDS_DIR/Deamon.py restart
	fi
fi




