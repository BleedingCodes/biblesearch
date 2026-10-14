# biblesearch
Want to know a specific verse, chapter to a book or a book. All you need is the name of the book and verse. Good way t test if you know the works to each verse.  

# This is my way of Sharing Gods word from the WEB Bible

# (🤮Windows🤮):

1. Download BibleSearch-Windows.zip 
2. right-click it, and choose Extract All. Don’t run it from inside the zip.
3. Open the extracted folder, then BibleSearch, and double-click the exe.
4. If Windows says “Windows protected your PC”, click More info, then Run anyway.
5. He types a verse, chapter, or book, such as john 3:16, and presses Enter.

# (🤘Linux🤘):

1. Download BibleSearch-Linux.tar.gz.
2. Run ```tar -xzf BibleSearch-Linux.tar.gz```, then ```cd BibleSearch```.
3. Run ```./bible_script_win john 3:16```, or just ```./bible_script_win``` for the prompt.


# USE ON ANDROID
** Option A: Pydroid 3 (easiest) **
On the Android phone, open the Play Store, search Pydroid 3 - IDE for Python 3, and install it (free).
Get your script and Bible file onto the phone, in one folder. Easiest: upload both to Google Drive from your Linux machine, open Drive on the phone, and download each. They land in the Download folder.
In the phone’s Files app, create a folder called BibleSearch and move both files into it.
Open Pydroid 3 and tap the folder icon, then Open, then browse to BibleSearch and select your script.
Tap the yellow play button. When it asks for a verse, type john 3:16 and press Enter.
The script’s last line (Press Enter to close...) is harmless here, so no edit is needed.
Option B: Termux (terminal, more control)
Do not install Termux from the Play Store (that version is outdated). Go to f-droid.org, install the F-Droid app, then search for and install Termux inside it.
Open Termux and run: pkg update (answer y if asked).
Run: pkg install python
Run: termux-setup-storage and tap Allow on the popup.
Put your script and Bible file in a BibleSearch folder in the phone’s Download folder (same method as Option A, step 2).
Run: cd ~/storage/downloads/BibleSearch
Run: python yourscript.py john 3:16 (replace with your real file name), or leave off the verse to get the prompt.
