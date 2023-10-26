import re

class ChangeManager:
    
    def __init__(self):
        pass

    def check_and_update(self, filtered_data):
        try:
            # Read the contents of filtered_results.txt
            with open("filtered_results.txt", "r", encoding="utf-8") as filtered_file:
                current_filtered_data = filtered_file.read()
        except FileNotFoundError:
            # Handle the case when the file doesn't exist
            current_filtered_data = ""

        # Check if the filtered_data is different from the current_filtered_data
        if "\n".join(filtered_data) != current_filtered_data:
            # Update previous_results.txt with the content of filtered_results.txt
            with open("previous_results.txt", "w", encoding="utf-8") as previous_file:
                previous_file.write(current_filtered_data)

            # Update filtered_results.txt with the new filtered_data
            with open("filtered_results.txt", "w", encoding="utf-8") as filtered_file:
                filtered_file.write("\n".join(filtered_data))

            print("Changes found and updated")
        else:
            print("No changes found")
            
    def find_changes(self):
        try:
            # Read the contents of filtered_results.txt
            with open("filtered_results.txt", "r", encoding="utf-8") as filtered_file:
                filtered_data = filtered_file.read()
        except FileNotFoundError:
            # Handle the case when the file doesn't exist
            filtered_data = ""

        try:
            # Read the contents of previous_results.txt
            with open("previous_results.txt", "r", encoding="utf-8") as previous_file:
                previous_data = previous_file.read()
        except FileNotFoundError:
            # Handle the case when the file doesn't exist
            previous_data = ""

        # Split the data by lines
        filtered_lines = filtered_data.splitlines()
        previous_lines = previous_data.splitlines()

        # Remove lines with "전자출판물 (6,595)" and "종이책 (842)" from the lists
        filtered_lines = [line for line in filtered_lines if line not in ["전자출판물 (6,595)", "종이책 (842)"]]
        previous_lines = [line for line in previous_lines if line not in ["전자출판물 (6,595)", "종이책 (842)"]]

        # Filter out lines that start with numbers and are identical between the two files
        filtered_lines = [line for line in filtered_lines if not line.startswith("[") and line not in previous_lines]

        # Print the parsed changes
        for change in filtered_lines:
            print(change)
            
    def extract_title(line):
        match = re.search(r'\d+\.\s+(.+)', line)
        if match:
            return match.group(1)
        else:
            return None
            
        
    def compare_files(self,file1, file2):
        with open('filtered_results.txt', 'r', encoding='utf-8') as file1, open('previous_results.txt', 'r', encoding='utf-8') as file2:
            lines1 = file1.readlines()
            lines2 = file2.readlines()

        # Create sets of titles from both files
        titles1 = set(filter(None, [ChangeManager.extract_title(line) for line in lines1]))
        titles2 = set(filter(None, [ChangeManager.extract_title(line) for line in lines2]))

        # Find the differences
        new_titles = titles1 - titles2
        removed_titles = titles2 - titles1

        # Print the differences
        print("New Titles:")
        for title in new_titles:
            print(title)

        print("\nRemoved Titles:")
        for title in removed_titles:
            print(title)

        
    