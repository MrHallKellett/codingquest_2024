from collections import defaultdict
from uuid import uuid4
with open("day7.txt") as f:
    ACTUAL_DATA = f.read().splitlines()


TEST_DATA = '''Folder: 0
 - taskmgr.exe 5065932
 - Customer_Feedback_Compilation_2024.xlsx 2646384
 - VLC-3.0.16-win64.exe 3971817
 - ProductLaunch2024.png 3712336
 - temporary_573 5048816
 - delete_708 2054307
 - temporary_023 [FOLDER 1]
Folder: 1
 - Conference_Break_Music.mp3 5179931
 - SlackSetup-x64-4.3.2.exe 2384929
 - Strategic_Plans [FOLDER 2]
 - Client_Dinner_Mar_2024.jpeg 5364778
 - FileZilla_3.55.1_win64-setup.exe 4623628
 - Charity_Event_011524.HEIC 2134414
 - Office_Christmas_Party_2023.jpeg 687062
Folder: 2
 - Product_Video_Soundtrack.aiff 813896
 - Operations_Manuals [FOLDER 3]
 - Signed_NDA_JohnDoe_021523.pdf 3257437
 - delete_930 9940460
 - Client_Acquisition_Strategies [FOLDER 4]
 - temporary_493 1332303
 - Marketing_Brochure_Image1.PSD 5913782
Folder: 3
 - ProductLaunch2024.png 4396529
 - Motivational_Morning_Playlist.m3u 5619626
 - Network_Configuration_Settings.txt 1068226
 - CRM_Database_Export_021724.csv 5812973
 - Competitor_Analysis_0224.pdf 1088620
 - Employee_Training_Videos_Link.txt 267104
 - delete_530 7150742
Folder: 4
 - temporary_751 1051994
 - delete_208 6042521
 - Logo_Rebrand_Options.svg 3438585
 - Node-v14.17.3-x64.msi 2056068
 - Expense_Report_Jan_2024.pdf 5775782
 - user32.dll 2371618
 - delete_027 9003131'''.splitlines()

EXPECTED = 103879262
RECEIVED = 117456299


def traverse(parent):
    

    if parent.visited_from_parent_already:

        #print("already visisted", parent.name)
        return 0

    #print("visiting", parent.name, "First time")
    
    q = [(parent, False, None)]
    total = 0
    while len(q):
        pad = len(q)*" "
        current, deleting, came_from = q.pop(0)
        deleting = deleting or "delete" in current.name or "temporary" in current.name
        #print(current.name, "came from", came_from.name if came_from is not None else "")
        if type(current) == Folder:
            if came_from is not None:
                
                current.visited_from_parent_already = True
                pass

            for child in current.children:     
                
                
                if child.visited_from_parent_already == False:
                    q.append((child, deleting, current))
        else:
            if deleting:
                if not current.deleted:
                    total += current.size
                    #print(total, "deleted")
                    current.deleted = True

    return total


class File:

    def __init__(self, name, size):

        self.name = name
        self.size = int(size)
        self.deleted = False
        self.id = uuid4()
        self.visited_from_parent_already = False

class Folder:
    def __init__(self, name, num):
        
        if name is None:
            name = f"Folder {num}"
        self.name = name
        self.num  = int(num)
        self.children = []
        self.id = uuid4()
        self.visited_from_parent_already = False
    
        
def solve(data):
    global freed_up_space

    folders = {}

    current_parent = None

    for line in data:
        line = line.strip()
 
        
        if "Folder" in line:
            fol_num = int(line.split(" ")[-1])
            this_folder = folders.get(fol_num)
            if this_folder is None:                
                folders[fol_num] = Folder(None, fol_num)
            
    

            current_parent = folders[fol_num]
            

        else:

            

            if "FOLDER" in line:
                _, name, _, this_fol_num = line.split(" ")
                this_fol_num = int(this_fol_num[:-1])
                
                this_folder = folders.get(this_fol_num)

                if this_folder is None:    
                    folders[this_fol_num] = Folder(f"{name} : FOLDER {this_fol_num}", this_fol_num)
                    
                else:
                    folders[this_fol_num].name = f"{name} : FOLDER {this_fol_num}"

                new_child = folders[this_fol_num]
   

            else:
                _, name, data = line.split(" ")
                new_child = File(name, data)


            current_parent.children.append(new_child)

    freed_up_space = 0

    for parent in folders.values():       

        freed_up_space += traverse(parent)

    result = freed_up_space

    print("Result obtained:", result)
    return result




if __name__ == "__main__":

    assert solve(TEST_DATA) == EXPECTED
    print("TEST PASSED!!!")
    freed_up_space = 0

    
    print(solve(ACTUAL_DATA))


