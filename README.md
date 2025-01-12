# File Processor
The aim of this project is to create a certain amount of daily data and to search effectively through this data. Python's own libraries were used for this, 3rd party library wasn't used. Multithreading and multiprocessing were used to perform operations efficiently and quickly.
### Features
- Creating the desired number of daily data
- Searching through data generated over the last 10 days
- Using multi-threaded architecture for fast data creation and scanning

### Structure 
- The project was written in python3
- Written as function based
- Wrote unit tests for functions
- During the file creation process, each file.txt file gets its own ID and is created in a different thread. Thus, 40 files are created in parallel quickly.
- After a list of all files to be searched during data search is obtained, each one is subjected to a search process in a different thread. Then, the result data from each file is taken and added to the output file all at once.

### Setup
- The project works with python3. It was developed with Python 3.13.1 version.
- There is no extra library that needs to be installed.

### Usage
- First of all, new data needs to be created to perform the search.
- The following command can be used for this
```bash
python3 main_generator.py
```
- With this command, a folder in YYmmdd format is created under days for that day. 40 file.txt files are created for 25 lines of data each.
- If you want to create data for a different day, you can run the following command using the YYmmdd format.
```bash
python3 main_generator.py -d 250110
```
- In the default command, a total of 1000 lines of data are created by distributing them equally to 40 files. Here, the total number of data can be entered as desired. The new number entered is created by distributing it to 40 files.
```bash
python3 main_generator.py -n 100000
```
- The created data is added to the project folder under days. The following command can be used to add it to a different folder.
```bash
python3 main_generator.py -dd /path/sub_path
```
- We created our data with the above commands. Now let's search in the files we created.
- For this, we will use the main_searcher.py file. The command will search the data created in the last 10 days using the desired conditions.
- As a condition, the search can be made with the ID numbers of the data or with the key value values found in the attributes values of the data.
- If any of these conditions are matched, the path of the relevant file, the line number where the data is located in the file, the match with which the data was found, and all the data in the relevant line are added to a report.
- The generated report is saved under the output file with the report_file_yymmddHHMMSSfff.txt format.
- The following command can be taken as an example for a search made only by id name. A maximum of 10 id's can be searched at a time. When searching with more than one ID, a space must be placed between each ID.
```bash
python3 main_searcher.py -i f05c 0fa4 73b7 418c
```
- The following command can be taken as an example for a search made only by key value. A maximum of 5 key value's can be searched at a time. The = sign must be placed between the key value values. When searching with more than one key value, a space must be placed between each key value.
```bash
python3 main_searcher.py  -a val_0=J75CY3 val_2=12s2 val_3=rwer
```
- In addition, since a multithreaded structure is used, the number of processors to be used during the search can be selected. For this, the number of processors can be added to the command with -p. 1 is selected by default.
- If the data files are in a path selected by the user, the relevant path can be added to the command with -dd.
- When the search process is completed, the path of the created report file is written to the screen as output.
- Finally, to run the unit tests, simply enter the following command.
 ```bash
python3 -m unittest
```
