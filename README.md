
# fasta-generator.py

Fasta generator is just a simple script designed to generate dummy fasta files (for example, if you want to check that contig-stitcher.py is behaving as expected). Users can dictate how many fasta sequences they want to generate (default is 1), the length of each sequence in the file, or opt to have all of the sequences generated at a random length (again, user can specify upper and lower limits of these parameters). 

## Dependencies

Fasta generator runs in Python 3.6 or later, and requires numpy. 

## Usage

```
usage: fasta-generator.py [-h] [-n NUMBER] [-l LOWER] [-u UPPER] [-s SPECIFIC] [-v] output

positional arguments:
  output                Name of file you would like to generate

options:
  -h, --help            show this help message and exit
  -n NUMBER, --number NUMBER
                        The number of sequences you want to generate. Default is 1
  -l LOWER, --lower LOWER
                        The lower limit of fasta size. Default is 100
  -u UPPER, --upper UPPER
                        The upper limit of fasta size. Default is 1000
  -s SPECIFIC, --specific SPECIFIC
                        Set all generated sequences to the same length. Incompatible with --lower and --upper
  -v, --verbose         Print out all fasta sequence lengths to terminal
```
