import os

def CreateFile(filename):
    try:
        with open(filename , 'x') as f:
            print(f"File Name {filename}: Creted successfully!")
    except FileExistsError:
        print(f"File name{filename} already exist")
        
    except Exception as E:
        print('An error occured')
        
def ViewAllFiles():
    files = os.listdir()
    if not files:
        print('No file found')
    else:
        print('files in directory')
        for file in files:
            print(file)
            
def DeleteFile(filename):
    try:
        os.remove(filename)
        print(f"{filename} has been deleted successfully")
    except FileNotFoundError:
        print("File not found")
        
    except Exception as e:
        print("An error occured")
        
def ReadFile(filename):
    try:
        with open("sample.txt" , 'r') as f:
            content = f.read()
            print(f"Content of {filename} :\n{content} ")
            
    except FileNotFoundError:
        print(f"{filename} doesn't exist")
        
    except Exception as e:
        print("An error occured")
        
def EditFile(filename):
    try:
        with open(f'{filename}' , 'a') as f:
            content = input("Enter data to add = ")
            f.write(content + "\n")
            print(f'Content added to {filename} Successfully')
            
        
    except FileNotFoundError as e:
        print(f"{filename} doesn't exist")
        
    except Exception as e:
        print("An error occured")
        
def main():
    while True:
        print('        File.........Management.........App')
        print('                 1: Create file')
        print('                 2: View all files')
        print('                 3: Delete file')
        print('                 4: read file')
        print('                 5: edit file')
        print('                 6: exit')
        
        choice = input("Enter your instruction from (1-6) = ")
        
        if choice =='1':
            filename = input("Enter filename = ")
            CreateFile(filename)
            
        elif choice == '2':
            ViewAllFiles()
            
        elif choice =='3':
            filename = input("Enter filename = ")
            DeleteFile(filename)
            
        elif choice =='4':
            filename = input("Enter filename = ")
            ReadFile(filename)
            
        elif choice =='5':
            filename = input("Enter filename = ")
            EditFile(filename)
            
        elif choice =='6':
            print("closing the App...")
            break
        else:
            print("In-valid input")
            
if __name__ == "__main__":
    main()