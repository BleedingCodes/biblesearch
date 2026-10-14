# biblesearch
Want to know a specific verse, chapter to a book or a book. All you need is the name of the book and verse. Good way t test if you know the works to each verse.  

# This is my way of Sharing Gods word from the WEB Bible

### (🤮Windows🤮):

1. Download BibleSearch-Windows.zip 
2. right-click it, and choose Extract All. Don’t run it from inside the zip.
3. Open the extracted folder, then BibleSearch, and double-click the exe.
4. If Windows says “Windows protected your PC”, click More info, then Run anyway.
5. He types a verse, chapter, or book, such as john 3:16, and presses Enter.

### (🤘Linux🤘):

1. Download BibleSearch-Linux.tar.gz.
2. Run ```tar -xzf BibleSearch-Linux.tar.gz```, then ```cd BibleSearch```.
3. Run ```./bible_script_win john 3:16```, or just ```./bible_script_win``` for the prompt.


## Use on Android

### Option A: Pydroid 3 (easiest)

1. Open the Play Store, search **Pydroid 3 - IDE for Python 3**, and install it (free).
2. Download the script and the Bible file from this repo onto your phone. They land in the **Download** folder.
3. In your Files app, create a folder called `BibleSearch` and move both files into it.
4. Open Pydroid 3, tap the **folder icon**, then **Open**, then browse to `BibleSearch` and select the script.
5. Tap the yellow **play button**. When it asks for a verse, type `john 3:16` and press Enter.

### Option B: Termux (terminal, more control)

1. Do **not** install Termux from the Play Store (that version is outdated). Go to f-droid.org, install the F-Droid app, then search for and install **Termux** inside it.
2. Open Termux and run: `pkg update` (answer `y` if asked).
3. Run: `pkg install python`
4. Run: `termux-setup-storage` and tap **Allow** on the popup.
5. Download the script and the Bible file from this repo, create a `BibleSearch` folder inside your phone's **Download** folder, and move both files into it.
6. Run: `cd ~/storage/downloads/BibleSearch`
7. Run: `python yourscript.py john 3:16`, or leave off the verse to get the prompt.
