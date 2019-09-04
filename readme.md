The **runner.py** script create Board With Letters and 
searches on it all possible words from the file which passed in the parameters to this script.
The script outputs the Board With Letters and all found words to the console.

## Settings
Add 'src' to the PYTHONPATH.
For this go to the project directory:
```bash
cd /path/to/the/project/directory/
```
And run the next command, please:
```bash
export PYTHONPATH=`pwd`/src:
```
## Script running
Go to the project directory:
```bash
cd /path/to/the_project_directory/
```
Run the script using command:
```bash
python3 src/runner.py --words_dict /media/sf_Shared/words.txt --rows 15 --columns 15
```
##### Where:
* **words_dict** - (required) path to the file of the words which should be searched on the board
* **rows** - (optional, by default 15) the number of the rows on the board 
* **columns** - (optional, by default 15) the number of the columns on the board 


## Unit tests
Go to the project directory:
```bash
cd /path/to/the_project_directory/
```
Run the test using command:
```bash
python3 -m unittest src/unit_tests.py --v
```