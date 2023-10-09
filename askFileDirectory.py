# Ask File Directory:

from tkinter import filedialog
from tkinter.filedialog import askdirectory

path = askdirectory()
print(path)

# other ways to store the path:
# path = r'{}'.format(path)
# path = rf'{path}'
# path = r'{}'.format(askdirectory())
# path = rf'{askdirectory()}'

# more:
path = askdirectory(title="Where do you want to save the file?")

# more:
path = askdirectory(title="Select Save Location",
                    initialdir=r".\images")

# more:
path = askdirectory(title="Select Save Location",
                    initialdir=r".\images",
                    mustexist=True)
