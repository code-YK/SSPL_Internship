import time 
from concurrent.futures import ThreadPoolExecutor

def write_to_file(file_name, data):
    with open(file_name, 'w') as file:
        file.write(data)

if __name__ == "__main__":
    data ={ "file1" : "Hello this is file 1 \n"*100,
           "file2" : "Hello this is file 2 \n"*100,
           "file3" : "Hello this is file 3 \n"*100,
           "file4" : "Hello this is file 4 \n"*100
           }
     
    starting_time = time.time()

    with ThreadPoolExecutor(max_workers=4) as executor:
        operations = []
        for file_name, content in data.items():
            operations.append(executor.submit(write_to_file, file_name, content))
    
        for i in operations:
            i.result()

        ending_time = time.time()
        
    print(f"Time taken to write files: {ending_time - starting_time} seconds")
