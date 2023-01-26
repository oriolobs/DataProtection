#!/bin/bash
n=255
k=$(openssl rand -hex 13)	#generate the random key
m=$(openssl rand -hex 1)	#generate the message
me=$(echo "$m"| xxd -r -p) #invert message to binary in order to encrypt it
echo "$m" >> message2
echo "$me" >> message
z=0
p=ff
w=xx
l=15

counter=0
for v in {01,03,04,05,06,07,08,09,0a,0b,0c,0d,0e,0f};
do
	for ((i=0; i<=$n; i++)); #set the counter of the iv value 
	do
		myvar=$v$p
		echo "$myvar"
		printf -v x %x $(($counter)) #count in hex
		if (($i<=$l))
		then
			key=$myvar$z$x #create value V with the corresponding counter value to create the iv, here it needs to be padding with zeros
		else
			key=$myvar$x 
		fi
		echo "$key"

		keystream=$key$k #concatenate the iv with the random key
		echo "$keystream" > key 
		cipher=$(echo -n "$me"| openssl enc -K "$keystream" -nosalt -rc4| xxd -p)
		myvarca=$(echo "$myvar"| tr '[a-z]' '[A-Z]') 
        	echo "0X$cipher" |tr '[a-z]' '[A-Z]' >> /home/ubuntu/dp/ciphers$myvarca 
		echo "0X$key" |tr '[a-z]' '[A-Z]'>> /home/ubuntu/dp/ivs$myvarca
		let counter++
	done
counter=0
paste -d ' ' /home/ubuntu/dp/ivs$myvarca /home/ubuntu/dp/ciphers$myvarca > /home/ubuntu/dp/bytes_$myvarca$w.dat
done
