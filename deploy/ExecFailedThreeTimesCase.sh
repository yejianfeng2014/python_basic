#! /bin/bash
# cron execute update recently dispute
# Author handongjie

set -i
source ~/.bashrc
source /etc/profile

case $APP_ENV in
	"production" )
		ArtisanDir=/export/data/tomcatRoot/customer.orderplus.com/artisan
		;;
	"testing" )
		ArtisanDir=/export/data/tomcatRoot/customer.orderplus.com/artisan
		;;
	"local" )
		ArtisanDir=/data/www/cs_out_site/artisan
		;;
	* )
		echo 'Environment Error!!!'
		exit
		;;
esac

Today=`date -d '0 day' +%Y%m%d`
Log=/tmp/update_three_failed_case_$Today.log

php $ArtisanDir updateThreeFailedCase >> $Log &