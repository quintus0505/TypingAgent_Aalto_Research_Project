import csv
import os
import argparse
import subprocess
import re
import pandas as pd

# Input file must be stored in the same folder
filepath = 'sentences.csv'
# Number of input sentences to type
number_sentences = 15
# Output as a directory in the same folder
o_path = 'typefromcsvres'
o_filepath = 'typefromcsvres/results.csv'
o_fields = [
    'sentence.text',
    'sentence.id',
    'agent.id',
    'target.sentence',
    'wpm',
    'lev.distance',
    'gaze.shift',
    'bs',
    'immediate.bs',
    'delayed.bs',
    'gaze.keyboard.ratio',
    'fix.count',
    'finger.travel',
    'iki',
    'correct.error',
    'uncorrected.error',
    'fix.duration',
    'chunk.length'
]
# Supervisor files
o_supervisorAgentTest = 'data/output/SupervisorAgent_sentence_test.csv'

# List of keyboards to evaluate param --kbd
keyboards = ['Gboard', 'SwiftKey', 'Go']
# List of keyheights to evaluate param --key_height
keyheights = ['small', 'medium', 'large']

#TESTING# Remove when release
keyboards = ['Gboard']
keyheights = ['small']
number_sentences = 2

# Command to run evaluation
TASK_EVALUATION = 'python main.py --all --config config.yml --type "{0}" --kbd {1} --key_height {2}'

# ARGUMENTS
parser = argparse.ArgumentParser()
parser.add_argument('--ns', default='15', help='number of sentences to types from the beginning of the sentences.csv')
# get user command line arguments.
args = parser.parse_args()

# Run an evaluation test on Supervisor Agent with the following input parameters
# Parameters:
# @ns: number of sentences
# @kbs: array of keyboards
# @khs: array of keyheights
# @o: path to output file
def runevaluate(ns,kbs,khs,o):
    for s in ns:
        for kb in kbs:
            for kh in khs:
                print("Started running evaluation on {0}-{1} : sentence {2}".format(kb, kh, s['text']))
                print("python cmd: ",TASK_EVALUATION.format(s['text'],kb,kh))
                # Run evaluation process under a subprocess to wait for result
                subprocess.Popen(TASK_EVALUATION.format(s,kb,kh),shell=True).wait()
                print("{0}-{1}-s{2} complete!".format(kb,kh,s['id']))

                # EXPORT result to output folder
                print("Copy res from `data/output/SupervisorAgent_sentence_test.csv` to {1}".format(o_path, o_filepath))
                res = []
                # Open `SupervisorAgent_sentence_test.csv`
                with open(o_supervisorAgentTest, 'r') as f:
                    # Skip the first row - Fields
                    next(f)
                    # Start reading from the second row - data
                    reader = csv.reader(f)
                    print("Read SupervisorAgent_sentence_test.csv")
                    # Marked which row I am to filter only first data row
                    currentrow = 0
                    for row in reader:
                        # Stop after fetching the first row data
                        if currentrow > 0: break
                        # Insert the sentence text to the beginning of each row
                        row.insert(0, s)
                        res = []
                        # Increasement
                        currentrow += 1
                f.close()
                # Write row to results.csv
                print("Add a new row to {0}",o_file)
                o.writerow(res)

# Run final test to verify that the number of rows == the number of sentences (ns*nkb*nkh)
# Parameters:
# @ns: number of sentences
# @kbs: number of keyboards
# @khs: number of keyheights
# @o: path to output file
def runtest(ns,nkb,nkh,o):
    df = pd.read_csv(o)
    n_rows = df.shape[0]
    print("Total input sentences: ", ns*nkb*nkh)
    print("Total output rows in {0}: {1}".format(o, n_rows))

# READ INPUT DATA
# Store data as a list of Python dictionaries
sentences = []
# Read and export data as a list
with open(filepath, 'r') as f:
    reader = csv.reader(f)
    print("Read input file: {0}".format(filepath))
    for row in reader:
        id = row[0]
        # Clean up text: covert to lower case and remove punctuation
        text = re.sub(r'[^\w\s]', '', row[1].lower())
        # Stop after fetching a certain amount of sentences param number_sentences
        if int(id) > number_sentences: break
        sentences.append({
            'id': id,
            'text': text,
            'type': row[2]
        })
    print("Export input file to a list of {0} sentences".format(number_sentences))
# Close the file
f.close()
#print("read object ", sentences)

# Verify whether output folder exist
if not os.path.exists(o_path):
    # Create a new directory when none exists
    os.makedirs(o_path)
    print("Create output folder {0}".format(o_path))

# Create output results.csv if none exist
with open(o_filepath, 'w+', newline='') as file:
    o_file = csv.writer(file)
    # Add first row <fields> if o_file is empty
    if os.stat(o_filepath).st_size == 0:
        print("Add results.csv with the first row - fields: ", o_fields)
        o_file.writerow(o_fields)
    print("Crease resultse file {0}".format(o_filepath))

    # EVALUATION START
    print("---EVALUATION START")
    runevaluate(sentences,keyboards,keyheights,o_file)
f.close()

# FINAL TEST
print("---FINAL TEST")
runtest(number_sentences, len(keyboards), len(keyheights) ,o_filepath)