import os
from dataloader import DataLoader


current_dir = os.path.dirname(os.path.realpath(__file__))

def test_c_tokenization():
    c_filedir_relative_path = "../tiny_dataset/C"
    c_filedir_path = f"{current_dir}/{c_filedir_relative_path}"

    # make a DataLoader object to test the helper functions
    dataloader = DataLoader(c_path=c_filedir_path)

    with open(f"{c_filedir_path}/arithmetic-subarrays-2.txt", "r") as f:
        c_code = f.read()

    c_code = dataloader.clean_c(c_code)
    tokens = dataloader.tokenize_c(c_code)

    print(tokens)

if __name__ == "__main__":
    test_c_tokenization()