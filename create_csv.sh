#touch submission.csv
#echo "Hello World" >> submission.csv
#echo "Hi" >> submission.csv

touch train.csv
for i in Dataset/*
do
    emotion=`echo $i | cut -d'/' -f2`;
    for j in $i/*.wav
    do
        echo "$j,$emotion,1" >> train.csv;
    done
done
