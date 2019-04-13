# strings2googleservice
This application is created in order to create "google-services.json" file from a decompiled apk.

# Usage
1 Put all of these files into a folder.  
2 Decompile your apk on http://www.javadecompilers.com/apk  
3 From the downloaded files find "strings.xml"  
4 Copy "strings.xml" to the folder that contains "string-xml-2-google-services.py"  
5 Run "python3 string-xml-2-google-services.py"  
6 "google-services.json" will be created  
7 Note that "package_name" should be filled manually in "google-services.json"

---
While trying to upload this to github I accidently typed  
rm -rf /*  
instead of  
rm -rf ./*
xd

