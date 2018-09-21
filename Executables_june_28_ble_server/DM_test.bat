echo ...........Start Automation on...........................
date
touch pass_test.log fail_test.log 
rm DM_logs/Pass/*.log
rm DM_logs/Fail/*.log
echo ...................Level 1.............................

python run.py init 1 1> DM_logs/Pass/DM_Test_1.log 2> DM_logs/Fail/DM_Test_1.log  

python run.py init 1 discover 1 1> DM_logs/Pass/DM_Test_2.log 2> DM_logs/Fail/DM_Test_2.log  
python run.py init 1 discover 1 get 1 1> DM_logs/Pass/DM_Test_3.log 2> DM_logs/Fail/DM_Test_3.log  
python run.py init 1 discover 1  put 1 1> DM_logs/Pass/DM_Test_4.log 2> DM_logs/Fail/DM_Test_4.log
python run.py init 1 discover 1  observe 1 1> DM_logs/Pass/DM_Test_4.log 2> DM_logs/Fail/DM_Test_4.log
python run.py init 1 discover 1  delete 1 1> DM_logs/Pass/DM_Test_5.log 2> DM_logs/Fail/DM_Test_5.log

  
 

echo ...................End Automation on.....................
date
