class CutestCats:
    def __init__(self,name,description,averageweight,averagelength,averagelifeexpectancy,imageurl):
        self.__name = name
        self.__description = description
        self.__averageweight = averageweight
        self.__averagelength = averagelength
        self.__averagelifeexpectancy = averagelifeexpectancy
        self.__imageurl = imageurl    
    
    def GetCatDetails(self):
        return (self.__name, self.__description, self.__weight,self.__length,self.__lifeexpectancy,self.__imageurl)
    
    def GetCatLife(self):
        return 'Life expectancy: ' + str(self.__lifeexpectancy) + '\nName: ' + str(self.__name)
    
with open('CutestCats.txt','r') as f, open('ModifiedCutestCats.txt','w') as o:
    for line in f:
        if line.strip():
            if 'COAT' not in line:
                o.write(line)
            
cat_database = []
with open('ModifiedCutestCats.txt','r') as f:
    num_lines = len(f.readlines())
    f.seek(0)
    for i in range(num_lines//6):
        cat_name = f.readline().strip()
        cat_description = f.readline().strip()
        cat_weight = f.readline().strip().replace('WEIGHT: ','')
        cat_length = f.readline().strip().replace('LENGTH: ','')
        cat_lifeexpectancy = f.readline().strip().replace('LIFE EXPECTANCY: ','')
        cat_imageurl = f.readline().strip()
        cat_weight_list = cat_weight.split(' ')
        total=0
        count = 0
        for i in cat_weight_list:
            if i.isdigit():
                total += int(i)
                count += 1
        cat_averageweight = total/count
        print(cat_averageweight)
        total=0
        count = 0
        cat_length_list = cat_length.split(' ')
        for i in cat_length_list:
            if i == 'foot':
                total += 12
                count += 1
            elif i == 'feet':
                total += (cat_length_list[i-1]*12)
                count += 1
            elif i == 'half':
                total += 6
            elif i == 'inches':
                for j in cat_length_list:
                    if j:
                        pass
