from pathlib import Path


import os, sys
script_path = os.path.realpath(os.path.dirname(__name__))


# instead of the traditional usage of import os, this new python way is more clean
script_path = Path(__file__).parent # the path in which this executable file exists
# C:\Python_Rust_Removal\Keith New Tips

# ----------------
# # same as:
# import os, sys
# file_path = os.path.realpath(os.path.dirname(__name__))
# ----------------


augmented_path = Path(__file__).parent / "data" / "info.txt"
# C:/Python_Rust_Removal/Keith New Tips/data/info.txt


home_directory = Path().home()
# C:/Users/shaib

my_favorites_directory = Path().home() / "Favorites"
# C:/Users/shaib/Favorites



