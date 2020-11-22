for i in Test/*.wav;
  do name=`echo $i | cut -d'.' -f1`;
  echo $name;
  ffmpeg -i "$i" -ar 16000 "${name}_1.wav" && rm "$i";
done

