# Download-folder-manager
The main.py script will create separate folders in your desktop for different types of media, and sort them based on their extensions, so putting images with images, pdfs with pdfs and so on. The file sorting is done checking the extension of each file and then moving it to the corresponding folder. More folders and different grouping can be done by adding the extension accepted in each category. The script will run infinitely until the terminal from which it is launched is still open. <br>
To run the script on your machine:
1. Change the *download_path* and *desktop_path* according to the location of the folders on your machine
If you want to run it as a background process:
2. To run the script even without the terminal, run the *run_script.bat* file. The python script will then run every 5 seconds
3. To stop the script, run the *stop_scrit.bat* file. **ATTENTION**: this process will kill all python.exe processes running on your pc 
