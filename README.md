# Wifi_locationing
Evaluate Techniques for Indoor Locationing 
Guessing indoor location, using the strength of WiFi signal. 

1. WiFi_00_EDA   
	>  a simple Exploration Data Analysis

2. WiFi_0_testData & WiFi_0_trainingData   
	> Some general Preprocessing of data

3. WiFi_1_Building  
	> Input: WAP // Output: Building_ID.
	> Some more preprocessing to guess Building_ID
	> Model training. And then save those models for further use. 

	WiFi_1_Building_models	  	  >> this loads the models and makes predictions with the training set	  
  
    WiFi_1_Building_TestData 		>> Makes predictions with unseen data to validate the models. 

4. WiFi_2_Floor  
	> Input: WAP // Output: Floor_ID.
	> Some more preprocessing to guess Floor_ID
	> Model training. And then save those models for further use. 

	WiFi_2_Floor_models		  >> this loads the models and makes predictions with the training set
  
  	WiFi_2_Floor_TestData 	>> Makes predictions with unseen data to validate the models. 

5. WiFi_3_Latitude  
	> Input: WAP // Output: Latitude.
	> Some more preprocessing to guess Latitude
	> Model training. And then save those models for further use. 

	WiFi_3_Latitude_models	  	>> this loads the models and makes predictions with the training set
  
	WiFi_3_Latitude_TestData	 	>> Makes predictions with unseen data to validate the models. 

6. WiFi_3_Longitude  
	> Input: WAP // Output: Longitude.
	> Some more preprocessing to guess Longitude
	> Model training. And then save those models for further use. 

	WiFi_3_Longitude_models		  >> this loads the models and makes predictions with the training set
  
	WiFi_3_Longitude_TestData	 	>> Makes predictions with unseen data to validate the models. 
