#!/bin/sh

cd ~/Desktop/Cu/
for dir in *
do
	cd ~/Desktop/Cu/$dir
	for item in *
	do
		cd ~/Desktop/Cu/$dir/$item
		for thing in *
		do
			cp -a ~/Desktop/JFEFF/CloudComputing ~/Desktop/Cu/$dir/$item
			cp -a ~/Desktop/JFEFF/feff84 ~/Desktop/Cu/$dir/$item
			cp -a ~/Desktop/JFEFF/feff90 ~/Desktop/Cu/$dir/$item
			cp -a ~/Desktop/JFEFF/icons ~/Desktop/Cu/$dir/$item
			cp -a ~/Desktop/JFEFF/lib ~/Desktop/Cu/$dir/$item
			cp ~/Desktop/JFEFF/feff ~/Desktop/Cu/$dir/$item
			cp ~/Desktop/JFEFF/feff.BAT ~/Desktop/Cu/$dir/$item
			cp ~/Desktop/JFEFF/jfeff.command ~/Desktop/Cu/$dir/$item
			cp ~/Desktop/JFEFF/jfeff.jar ~/Desktop/Cu/$dir/$item
			cp ~/Desktop/JFEFF/license.txt ~/Desktop/Cu/$dir/$item
			start_time="$(date -u +%s)"
			. feff
			end_time="$(date -u +%s)"
			elapsed="$(($end_time-$start_time))"
			rm ~/Desktop/Cu/$dir/$item/feff
			rm ~/Desktop/Cu/$dir/$item/feff.BAT
			rm ~/Desktop/Cu/$dir/$item/jfeff.command
			rm ~/Desktop/Cu/$dir/$item/jfeff.jar
			rm ~/Desktop/Cu/$dir/$item/license.txt
			rm -r ~/Desktop/Cu/$dir/$item/CloudComputing
			rm -r ~/Desktop/Cu/$dir/$item/feff84
			rm -r ~/Desktop/Cu/$dir/$item/feff90
			rm -r ~/Desktop/Cu/$dir/$item/icons
			rm -r ~/Desktop/Cu/$dir/$item/lib
			cd ~/Desktop/Completed/Cu/
			mkdir ~/Desktop/Completed/Cu/$dir
			cp -a ~/Desktop/Cu/$dir/$item ~/Desktop/Completed/Cu/$dir/$item
			cd ~/Desktop/Completed/Cu/$dir/$item
			echo "Time: $elapsed" > elapsed.txt
		done
	done
done