import os

BASE_DIR = 'assets/tests/test_configs'
ABS_PATH = os.path.join(os.getcwd(),BASE_DIR)
FILES    = [os.path.join(os.getcwd(),f"{BASE_DIR}/{f}") for f in os.listdir(ABS_PATH) if os.path.isfile(os.path.join(ABS_PATH, f))] # This is also our test_input



for file_name in FILES:
    json_string = ""
    file_name_wo_path = file_name.split("/")[-1]
    
    if file_name.split(".")[-1].lower() == "json":
        
        with open(file_name,"r") as file:
            contents = file.read()
            contents = contents.replace("true","True") # Just to match python syntax
            contents = contents.replace("null","None") # Just to match python syntax
            if len(contents) == 0 :
                print(f"\"{file_name_wo_path}\" : {"{}"},")
            else:
                print(f"\"{file_name_wo_path}\" : {contents},")
        # print(f"\"Test{index}\" : {contents},")   