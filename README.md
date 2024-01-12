# PROJECT COMPONENT
   ===>> database : postgres.<br>
   ===>> backend : fastapi. <br>
   ====> frontend : nextjs. 
# NOTE THAT YOU ARE IN FOLDER DATABASELAB
# How to setting database
  ===> The first method : use backup file to restore data, this backup file contain simulation data .<br>
  ===> the second method : <br>
         => create the database in pgadmin4.<br>
         => create the table and these relation using data/SQL_create/Create_Table_Querry.txt.<br>
         => run the data/TRIGGER AND INDEX/ for create the trigger and index.<br>
         => run the all file in folder "data/data generation" for creating similation data.
# How to run the backend server
    => run the cmd "pip install requirement.txt" to install neccessary library.<br>
    => in file "backend/app/lib/database/config.py" replace "SQLALCHEMY_DATABASE_URL" by your database link to connect to your database.<br>
    => run backend/run.sh to run server.<br>
    => go to the localhost:8000/docs to check whether your backend has been success running (NOTE : you will see the backend-api testing interface - you can testing your apis using this UI) 

# How to run front-end server
   ==> ensure that you have nodejs verson >= 18.<br>
   ==> run the cmd "cd front-end/nextjs-dashboard/".<br>
   ==> now you are in folder nextjs-dashboard/.<br>
   ==> run the command npm i ( it automatically install all the neccessary library in package.json).<br>
   ==> run " npm dev run" to start your front-end server.<br>
   ==> go to localhost:3000 to check if you run successfully.<br>
