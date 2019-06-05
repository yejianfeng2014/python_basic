#! /bin/bash
# cron execute update recently dispute
# Author handongjie

set -i
source ~/.bashrc
source /etc/profile

#if [[ $APP_ENV = "production" ]]; then
#	CMDS_DIR=/export/data/tomcatRoot/customer.orderplus.com/deploy
#elif [[ $APP_ENV = "testing" ]]; then
#	CMDS_DIR=/export/data/tomcatRoot/customer.orderplus.com/deploy
#elif [[ $APP_ENV = "local" ]]; then
#	CMDS_DIR=/data/www/cs_out_site/deploy
#else
#	echo 'Environment Error!!!'
#	exit
#fi

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

PullDisputes=$CMDS_DIR/PullDispute.py

Today=`date -d '0 day' +%Y%m%d`
PullDisputesLog=/tmp/pull_disputes_$Today.log

if [[ ! -d /tmp ]]; then
	mkdir -p /tmp
fi

if [[ -d $CMDS_DIR && -f $PullDisputes ]]; then
	if [[ ! -x $PullDisputes ]]; then
		chmod +x $PullDisputes
	fi

	if [[ ! -f $PullDisputesLog ]]; then
		touch $PullDisputesLog
		chmod +w $PullDisputesLog
	fi

	#python3 $GetDisputes >> $GetDisputesLog &
	python3 $PullDisputes 0 15 >> $PullDisputesLog &

	if [[ $? -eq 0 ]]; then
		echo 'Pull disputes list success!!!'
	else
		echo 'Pull disputes list fail!!!'
	fi
fi

