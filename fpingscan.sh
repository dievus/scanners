#!/bin/bash

#Greeting#

greeting() {
	
	tput setaf 2; tput bold;
	echo -e
	echo -e 	"--------------------"
	echo -e 	"-    Super Duper   -"
	echo -e     	"- Fping Sweep Tool -"
	echo -e 	"--------------------"
	echo -e
	echo -e		"When you want to F things a bit"	
	echo -e		  "by The Mayor/Dievus"; tput sgr0;
	echo -e
}

info(){
tput bold; echo -en "Please Enter an IP Range to Scan."; tput sgr0;
	echo -e
	read name
	if [ "$name" == "" ]
		then
		tput setaf 1; tput bold; echo -e "You forgot to enter a target range!"; tput sgr0;
		tput setaf 1; tput bold; echo -e "Example - 192.168.1.0/24"; tput sgr0;
	exit 0
fi	
}
fping_scan(){
fping -a -g -q $name
}
greeting
info
fping_scan
exit 0