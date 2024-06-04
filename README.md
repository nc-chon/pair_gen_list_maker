# Pair Generator Cohort List

## Who is this for?

- Starting a new cohort?
- Setting up the pair generator cohort?
- Hate having to seperate the student names with their locations from the raw data?

Then this is the place for you!
(*developers hate this one trick!*)

*Is there not a excel/google sheet solution?* 

Probably, but who has time to pick up a new skill, when you can bruteforce a code solution instead, like a true stubborn developer.

<br> 

*Disclaimer: No chatPDTs were used/harmed in the making of this repo.*

<br>

## How do I use this?

The functions are written in Python, so if you're not a current snakecharmer then this is the perfect chance to update your CPD.

Starting Checklist:
- Current cohort student tracker (Google Sheet)
- A new blank Google Sheet
- VSCode with Python

### Step 1 - Copy Student Data From Tracker

In the cohort student tracker, navigate to the `RawStudents` page and copy the two columns that contain all of the student names and locations present.

Then paste this in your new blank google sheet, which should look like this (you dont need any column names/headers):

```
---------------+-----------
Nigel Dataman  | Remote
John Appleseed | Manchester
Maximus Mac    | Leeds
Wendy Windows  | Remote
```

Going back to the student tracker, navigate to the `MentorGroups` page and copy all the student names from your specific seminar's mentor groups. Again let's paste this `seminar student data` into your previously open google sheet in a seperate column from the `raw student data` before. You should have something like this:

```
---------------+------------+-----+--------------
Nigel Dataman  | Remote     |     | Nigel Dataman
John Appleseed | Manchester |     | Wendy Windows
Maximus Mac    | Leeds      |     |
Wendy Windows  | Remote     |     |
```

<br>

### Step 2 - Format Data on Google Sheets

Now that we have the student data copied over, we just need to add a little formatting before it's ready to be used. 

On your new Google Sheet, highlight the entire first column (student name) of the `raw student data` section and right click to open the pop up window, then click  `+ Insert 1 column right`. In this new blank column, you will need to insert a comma to fill the space. Simply input a comma in the first cell and just use the drag to auto fill from the bottom right of a cell. Your sheet should now look like this:

```
---------------+---+------------+-----+--------------
Nigel Dataman  | , | Remote     |     | Nigel Dataman
John Appleseed | , | Manchester |     | Wendy Windows
Maximus Mac    | , | Leeds      |     |
Wendy Windows  | , | Remote     |     |
```

Next we just want to organise the data to be alphabetical (OFSTED compliant), let's highlight the 3 columns of the `raw student data` (student name, comma, location) and follow the below:
- navigate to `Data` at the top
- hover to `Sort range`
- click `Sort range by column {student name column} (A to Z)`

Let's do the same for the `seminar student data` and sort alphabetically.

### Step 3 - Copy Data into the CSV Files

Now we're ready to use the Python code! Copy the full 3 columns of the `raw student data` from the Google Sheets. In VSCode navigate to the `./data` directory and open `raw_student_data.csv`. Paste the `raw student data` into this file, which should look like this:

```
Nigel Dataman	,	Remote
John Appleseed	,	Manchester
Maximus Mac	,	Leeds
Wendy Windows	,	Remote
```

Don't worry about the formatting with the extra spaces, the Python code will deal with this! 

Next, copy the `seminar student data` (the single column) from your Google Sheets and paste this into the `seminar_student_data.csv` file, in the same `./data` directory.

### Step 4 - Execute the Python file

Normally with best practice, we would set up a virtual environment before running any Python code, but as this is a simple function that doesn't require installing any external packages, we can skip that part. You will however need to run the following command first:

```sh
export PYTHONPATH=$(pwd)
```

Next let's run the following command to execute the Python code:

```sh
python src/pair_list_generator.py
```

This should create a new file `student_pair_data.csv` inside the `./output` directory. Open this file and you'll now see the formatted and filtered list of student names and their locations for your seminar! Assuming you have created the new cohort on the `pair generator tool/browser`, select your cohort/seminar, click `add students` and simply copy the data from your new `student_pair_data.csv` and paste it.