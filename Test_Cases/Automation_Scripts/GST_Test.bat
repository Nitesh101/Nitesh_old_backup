echo ***********************Start Automation on***********************
date
echo
if [ -f dashboard.xlsx ]
then
	rm dashboard.xlsx
fi

python GST_Install.py > result.txt 
python Ex_Result.py result.txt GST_TC_01 Pass 

python Gst_Src.py > result.txt  
python Ex_Result.py result.txt GST_TC_05 Pass

python Gst_Sink.py > result.txt  
python Ex_Result.py result.txt GST_TC_06 Pass

python Gst_Encoder_Decoder.py > result.txt  
python Ex_Result.py result.txt GST_TC_07 Pass

python Gst_demuxer.py > result.txt  
python Ex_Result.py result.txt GST_TC_08 Pass

python Gst_Play_audio.py > result.txt  
python Ex_Result.py result.txt GST_TC_09 Pass

python Gst_Play_video.py > result.txt  
python Ex_Result.py result.txt GST_TC_10 Pass

echo
echo ***********************End Automation on***********************
date
