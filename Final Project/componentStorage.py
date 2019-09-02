import os

class componentStorage:

    #categories list
    categories = []

    #current category
    currCategory = ""

    #current components list
    currComponents = []
    
    #gets the initial categories
    def categoriesInit(self):
        try:
            #opens category file
            catFile = open("data/categories.txt", "r")

            for x in catFile:
                #gets rid of the newline
                if(x[len(x) - 1] == '\n'):
                    x = x[:-1]
                
                #saves the categories to the array
                self.categories.append(x)

            #sanity check to make sure the categories are sorted
            self.categories.sort()

            #closes catagory file
            catFile.close()

        except FileNotFoundError:
            os.mkdir("data")
            print("ERROR: No categories.txt creating now...")
            try:
                catFile = open("data/categories.txt", "w+")
                catFile.close()

            #handles if there is no directory
            except FileNotFoundError:
                os.mkdir("data")
                catFile = open("data/categories.txt", "w+")
                catFile.close()

            except:
                print("\nERROR LOADING CATEGORIES")
        
        except:
            print("\nERROR LOADING CATEGORIES")


    #function to add a new category
    def addCategory(self, name):

        #checks to make sure the category does not exist
        for x in self.categories:
            if name == x:
                return
        
        #adds the new category and sorts it into the list
        self.categories.append(name)
        self.categories.sort()

        #saves updated list to categories.txt and creates a new file for the new category
        try:
            catFile = open("data/categories.txt", "w")

            for x in self.categories:
                catFile.write(x + "\n")

            catFile.close()

            newFile = open("data/"+ name + ".txt", "w+")
            newFile.close()
        
        except:
            print("\nERROR CREATING NEW CATEGORY\n")

    #removes a category
    def removeCategory(self, name):
        i = 0
        for x in self.categories:
            if(name == x):
                try:
                    del self.categories[i]
                    os.remove("data/" + name + ".txt")

                    catFile = open("data/categories.txt", "w")
                    for x in self.categories:
                        catFile.write(x + "\n")
                    catFile.close()

                except:
                    print("\nERROR REMOVING CATEGORY\n")

                return
            i = i + 1
        


    #loads all the compoents stored in 1 folder into an array
    def loadComponents(self, category):
        
        #clears list
        self.currComponents.clear()

        #sets the current category
        self.currCategory = category
        
        #opens the specified category text file and loads the raw data into an array
        catFile = open("data/" + self.currCategory + ".txt", "r")
        componentData = catFile.readlines()
        catFile.close()

        #cleans the newline character off of the data
        i = 0
        for x in componentData:
            if(x[len(x) - 1] == '\n'):
                    x = x[:-1]
                    componentData[i] = x
            i = i + 1

        #stores the data into the working array
        x = 0
        while(x + 2 < len(componentData)):
            self.currComponents.append(component(name = componentData[x], description = componentData[x + 1], num = componentData[x + 2]))
            x = x + 3

    #function to add a new component
    def addComponent(self, tempName, tempDescription, tempNum):

        categoryExists = False

        #makes sure the category still exists
        for x in self.categories:
            if(self.currCategory == x):
                categoryExists = True
        
        if(not categoryExists):
            print("\nERROR CURRENT CATEGORY DOES NOT EXIST")
            return

        #makes sure the component doesnt already exist
        for x in self.currComponents:
            if (tempName == x.name):
                return
        
        #creates new component and sorts it into the list
        self.currComponents.append(component(name = tempName, description = tempDescription, num = tempNum))
        self.currComponents.sort(key = lambda x: x.name)
        
        #saves the new list to the file
        catFile = open("data/" + self.currCategory + ".txt", "w")
        for x in self.currComponents:
            catFile.write(x.name + "\n")
            catFile.write(x.description + "\n")
            catFile.write(str(x.num) + "\n")
        catFile.close()

    #function to change the number of components available
    def changeComponentNum(self, comName, newNum):

        categoryExists = False

        #makes sure the category still exists
        for x in self.categories:
            if(self.currCategory == x):
                categoryExists = True
        
        if(not categoryExists):
            print("\nERROR CURRENT CATEGORY DOES NOT EXIST")
            return

        i = 0
        for x in self.currComponents:
            if(x.name == comName):
                self.currComponents[i].num = newNum

                #saves the new list to the file
                catFile = open("data/" + self.currCategory + ".txt", "w")
                for j in self.currComponents:
                    catFile.write(j.name + "\n")
                    catFile.write(j.description + "\n")
                    catFile.write(str(j.num) + "\n")
                catFile.close()

                return
            
            i = i + 1

    #function to delete component
    def removeComponent(self, comName):

        categoryExists = False

        #makes sure the category still exists
        for x in self.categories:
            if(self.currCategory == x):
                categoryExists = True
        
        if(not categoryExists):
            print("\nERROR CURRENT CATEGORY DOES NOT EXIST")
            return
            
        i = 0
        for x in self.currComponents:
            if(x.name == comName):
                del self.currComponents[i]

                #saves the new list to the file
                catFile = open("data/" + self.currCategory + ".txt", "w")
                for j in self.currComponents:
                    catFile.write(j.name + "\n")
                    catFile.write(j.description + "\n")
                    catFile.write(str(j.num) + "\n")
                catFile.close()

                return
            
            i = i + 1


#
# CLASS: class for holding the component values
#
class component:
    def __init__(self, name, description, num):
        self.name = name
        self.description = description
        self.num = num