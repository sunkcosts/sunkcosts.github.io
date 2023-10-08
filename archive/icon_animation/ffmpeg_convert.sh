# converts mp4 to gif and applies boomerang loop effect
ffmpeg -i "data/02.runwayml_output.mp4" -filter_complex "[0]reverse[r];[0][r]concat=n=2:v=1:a=0" -o "03.unoptimized_output.gif"