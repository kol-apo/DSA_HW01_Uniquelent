import os, time, tracemalloc
from unique_set import Set
from docx import Document

# Gets the current working directory
directory = os.getcwd()

# Gets all files in the sample input directory and removes all possible hidden files in the directory
files = [f for f in os.listdir(f'{directory}/sample_input_for_students') if os.path.isfile(os.path.join(f'{directory}/sample_input_for_students', f)) and not f.startswith('.')]

# Creates the result directory if it does not exist
os.makedirs(f'{directory}/sample_results', exist_ok=True)

valid_characters = '1234567890.-'

def is_number(str: str):
    if str == '':
        return False
        
    for char in list(str):
        if char not in valid_characters:
            return False
        
    return True

def read_next_item_from_file(input_path: str):
    unique_numbers = Set()
    
    if input_path.endswith('.txt'):
        file_info = open(input_path, 'r')

        for line in file_info:
            try:
                if len(line.split(' ')) > 1:
                    continue
                
                if not is_number(line.strip()):
                    continue
                
                number = float(line.strip())
                
                unique_numbers.add(number)
            except ValueError:
                # Line is an empty space
                continue

    elif input_path.endswith('.docx'):
        doc = Document(input_path)
        for paragraph in doc.paragraphs:
            for line in paragraph.text.splitlines():
                try:
                    if len(line.split(' ')) > 1:
                        continue
                
                    if not is_number(line.strip()):
                        continue
                
                    number = int(line.strip())
                    
                    unique_numbers.add(number)
                except ValueError:
                    # Line is an empty space
                    continue
    
    return unique_numbers

# The process_file function takes in the input & output paths to remove all the duplicates
def process_file(input_path, output_path):    
    start_time = time.time()
    
    tracemalloc.start()
    
    unique_numbers = read_next_item_from_file(input_path)
            
    output = open(output_path, 'w')
    
    for number in sorted(unique_numbers):
        output.write(f'{number}\n')
    
    current, peak = tracemalloc.get_traced_memory()
    
    tracemalloc.stop()

    submitted_time = time.time() - start_time

    print(f"Processed File {output_path} in {submitted_time:.4f} seconds")
    
    print(f"Current memory usage: {current / 1024:.2f} KB; Peak: {peak / 1024:.2f} KB")

def UniqueInt():
    for file in files:
        process_file(f'{directory}/sample_input_for_students/{file}', f'{directory}/sample_results/{file}_results.txt')
        
UniqueInt()