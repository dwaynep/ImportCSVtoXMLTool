#ABOUT###########################################
#Import CSV to XML Tool
#Created: by Dwayne P. (dwaynepindling@gmail.com)
#Date: April 24th 2015
#Version 1.0
#################################################

#INSTALLATION##########################################################
#In order to run this script, user must have Python 3.0 installed.
#Files will be created in the following folder where script is located.
#Sample files included in Github repository.
#######################################################################

#FUNCTIONALITY####################################################################
#The following script will allow user to create xml files based on a
#imported .xml file. Futhermore, user can use information from an
#independant CSV file to populated XML files.
##################################################################################



import xml.etree.ElementTree as etree #Module imported to allow the ability to parse XML template
import csv #Module imported to allow the use of CSV files
import datetime #Module imported to allow the creation of filename with date/time


num = int(input ("Please the mount of users you would like to process from file: ")) #Prompt to enter the amount of users to be processed
with open('datanames2.csv') as csvfile: #Opening of the specific CSV file. File should be placed in same folder as script
    reader = csv.reader(csvfile) #Grab the file and assign it to reader
    x=0 #Initialization of the counter variable
    line = next(reader) #Code to advance to the next line in reader
    line = next(reader) #Code to advance to the next line in reader
    while x<num: #Value entered will determine how many files are created 
        filename = "RegistrationApplication_"+datetime.datetime.now().strftime("%Y%m%d%H%M%S")+str(x)+".xml" #New application will be created with current date/time and .xml format
        [registrationId,requestDate,registerId,lastName,firstName,middleName,maidenName,alias,idCardNumber,idCardType,birthdate,streetAddress,
        city,state,zipCode,country,emailAddress,phoneNumber,phoneType] = line  #Line will consist of all the fields that are to be updated from CSV file.
        tree = etree.parse('TestFile.xml') #Imported XML file that will be used as a template. File should be placed in same folder as script
        registration_Id = tree.find('registrationId') #Finding of the Registration ID element
        registration_Id.text = (line[0]) #updating of the Registration ID element
        request_Date = tree.find('requestDate') #Finding of the Request Date element
        request_Date.text = (line[1]) #updating of the Request Date element
        register_Id = tree.find('Register/registerId') #Finding of the Register ID element
        register_Id.text =(line[2]) #Updating of the Register ID element
        last_Name = tree.find('Register/lastName') #Finding of the Last Name element
        last_Name.text =(line[3]) #Updating of the Last Name element
        first_Name = tree.find('Register/firstName') #Finding of the First Name element
        first_Name.text = (line[4]) #updating of the First Name element  
        middle_Name = tree.find('Register/middleName') #Finding of the Middle Name element
        middle_Name.text = (line[5]) #updating of the Middle Name element
        maiden_Name = tree.find('Register/maidenName') #Finding of the Maiden Name element
        maiden_Name.text =(line[6]) #Updating of the Maiden Name element
        alias = tree.find('Register/alias') #Finding of the Alias element
        alias.text = (line[7]) #Updating of the Alias element
        id_Card_Number = tree.find('Register/idCardNumber') #Finding of the ID Card Number element
        id_Card_Number.text = (line[8]) #Updating of the ID Card Number element
        id_Card_Type = tree.find('Register/idCardType') #Finding of the ID Card Type element
        id_Card_Type.text = (line[9]) #Updating of the ID Card Type element
        birth_Date= tree.find('Register/birthDate') #Finding of the Birth Date element
        birth_Date.text = (line[10]) #Updating of the Birth Date element
        street_Address= tree.find('Register/streetAddress') #Finding of the Street Address element
        street_Address.text = (line[11]) #Updating of the Street Address element
        city= tree.find('Register/city') #Finding of the City element
        city.text = (line[12]) #Updating of the City element
        state= tree.find('Register/state') #Finding of the State element
        state.text = (line[13]) #Updating of the State element
        zip_Code= tree.find('Register/zipCode') #Finding of the Zip Code element
        zip_Code.text = (line[14]) #Updating of the Zip Code element
        country= tree.find('Register/country') #Finding of the Country element
        country.text = (line[15]) #Updating of the Country element
        email_address = tree.find('Register/emailAddress') #Finding of the Email Address element
        email_address.text = (line[16]) #Updating of the Email Address element
        phone_number = tree.find('Register/phoneNumber') #Finding of the Phone Number element
        phone_number.text = (line[17]) #Updating of the Phone Number element
        phone_type = tree.find('Register/phoneType') #Finding of the Phone Type element
        phone_type.text = (line[18]) #Updating of the Phone Type element
        FirstN = str(line[4]) #Updating of the line to a message
        LastN = str(line[3]) #
        print("The record of " +FirstN+ " "+LastN+ " has been updated") #Displaying message to console that updated have been made.
        line = next(reader) #Code to advance to the next line in reader
        tree.write(filename)  #Write new file
        x=x+1
