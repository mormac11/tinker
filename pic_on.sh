/usr/bin/pkill fbi
#/usr/bin/fbi -T 4 -noverbose /home/linaro/pictures/2016_05_21_9999_127.JPG
hour=$(date +%H)
#hour=16
echo $hour




if [ $hour -gt 16 ] && [ $hour -lt 24 ]
	then
	#/usr/bin/fbi -T 4 -noverbose /home/linaro/pictures/2016_05_21_9999_127.JPG	
	/usr/bin/fbi -T 4 -noverbose -a -fitwidth /home/sean/pictures/2016_05_21_9999_139.JPG
	echo "1"
	else
	/usr/bin/fbi -T 4 -noverbose -a -fitwidth  /home/sean/pictures/2017_05_27_3569.JPG
	echo "2"
fi
