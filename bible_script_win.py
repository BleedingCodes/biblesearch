#! /usr/bin/env python3
import argparse, re
import sys, os
BASE = os.path.dirname(sys.executable) if getattr(sys, "frozen", False) else os.path.dirname(os.path.abspath(__file__))
bible_path = os.path.join(BASE, "Bible WEB version")


############################################################################################################
# argparse variable (args.verse) so you can bypass the interactive input prompt
############################################################################################################

parser = argparse.ArgumentParser(description="Script that returns a verse, chapter, or book from the WEB Bible")
parser.add_argument('verse', nargs='*', help="The verse sequence you want to search")
# Changing nargs to '*' collects all arguments into a list
args = parser.parse_args()

############################################################################################################
# class BibleStudy
############################################################################################################

class BibleStudy:
	def __init__(self, requesting_list=None):
		if requesting_list:
			# Join list elements with a space if passed from terminal, otherwise leave empty
			self.requesting = " ".join(requesting_list).strip()
		else:
			self.requesting = ""

	def user_request(self):
		if not self.requesting:
			print("Hold on to Faith.\n")
			self.requesting = input("Enter A Verse, Chapter, or a Book, Please\n").strip()
			return self.requesting
			# Only prompt the user if they didn't provide a terminal argument
		
	def find_request(self):
		# Guard clause: if still empty, don't read the file to avoid dumping the whole book
		if not self.requesting:
			return []
	
		user_input = self.requesting.strip()
		
		# 1. Handle numbered books tightly packed or spaced (e.g., "1john1:9", "1john1", "1 john 1")
		numbered_book_match = re.match(r'^([1-3])\s*([A-Za-z\s]+?)\s*([0-9]+)?(:[0-9]+)?$', user_input)
		
		# 2. Handle standard books (e.g., "genesis37:3", "james1", "james")
		standard_book_match = re.match(r'^([A-Za-z\s]+?)\s*([0-9]+)?(:[0-9]+)?$', user_input)

		if numbered_book_match:
			prefix = numbered_book_match.group(1)
			book_name = numbered_book_match.group(2).strip()
			chapter = numbered_book_match.group(3)
			verse = numbered_book_match.group(4)
			
			book = f"{prefix} {book_name}"
			
			if chapter and verse:
				# e.g., "1 John 1:9"
				search_regex = re.compile(rf'^{re.escape(book)}[\s\t]*{re.escape(chapter)}{re.escape(verse)}', re.IGNORECASE)
			elif chapter:
				# e.g., "1john1" matches "1 John 1:" at the start of a verse line
				search_regex = re.compile(rf'^{re.escape(book)}[\s\t]*{re.escape(chapter)}:', re.IGNORECASE)
			else:
				# e.g., "1john" matches the whole book
				search_regex = re.compile(rf'^{re.escape(book)}[\s\t]*', re.IGNORECASE)
				
		elif standard_book_match:
			book = standard_book_match.group(1).strip()
			chapter = standard_book_match.group(2)
			verse = standard_book_match.group(3)
			
			if chapter and verse:
				search_regex = re.compile(rf'^{re.escape(book)}[\s\t]*{re.escape(chapter)}{re.escape(verse)}', re.IGNORECASE)
			elif chapter:
				search_regex = re.compile(rf'^{re.escape(book)}[\s\t]*{re.escape(chapter)}:', re.IGNORECASE)
			else:
				search_regex = re.compile(rf'^{re.escape(book)}[\s\t]*', re.IGNORECASE)
		else:
			# Absolute fallback
			search_regex = re.compile(rf'^{re.escape(user_input)}', re.IGNORECASE)
   
		# Stop pattern flags when a fresh verse index sequence begins
		stop_pattern = re.compile(r'^([1-3]\s+)?[A-Za-z]+[\s\t]+[0-9]+:[0-9]+')
		flag = False
		sendout = []

		with open(bible_path, "r", encoding="utf-8") as f:
			for lines in f:
				# Use regex match to accept variable white space/tabs at the beginning
				if search_regex.match(lines):
					flag = True
					sendout.append(lines)
					continue 

				if stop_pattern.match(lines):
					if flag:
						# Continue collecting if the next verse line still belongs to our requested target
						if not search_regex.match(lines):
							break 

				if flag:
					sendout.append(lines)

		return sendout



############################################################################################################
# Execution
############################################################################################################

# 1. Pass the argparse terminal list into the class
test = BibleStudy(requesting_list=args.verse)

# 2. This will only ask via input() if no terminal argument was provided
test.user_request()

# 3. Retrieve, clean up tabs/brackets, and print
result = test.find_request()
if result:
	clean_output = "".join(result).replace("\t", " ")
	print(clean_output)
else:
	print("Verse or text not found.")


input("\nPress Enter to close...")
