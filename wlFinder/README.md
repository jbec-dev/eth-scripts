# wlFinder
wlFinder is a simple offline tool for Linux to check a password against various public wordlists.
The main tool is called "wlfinder.py".

## How it works:
wlFinder groups wordlists into thematic categories (e.g. common passwords, time-related terms).
During a check, categories are processed sequentially, allowing early detection of weak passwords while keeping runtime low.

### Side Note
The program uses the SecLists wordlists for Linux, which have to be installed manually at /usr/share/seclists by the user.
> Make sure you have Python3.x installed, as the software is based on the Python programming language.


## License
Please view the LICENSE.txt file for additional Information
