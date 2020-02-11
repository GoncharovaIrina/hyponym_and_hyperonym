from bs4 import BeautifulSoup
import os
import codecs
import pandas as pd   #  pip install pandas

def get_soup(file):
    with codecs.open(file, encoding='utf-8')as f:
        handler = f.read()
    return BeautifulSoup(handler, features="lxml")

def parse_synsets(file):
    soup = get_soup(file)
    return [(element.attrs['id'], element.attrs['ruthes_name']) for element in soup.findAll('synset')]

def parse_senses(file):
    soup = get_soup(file)
    return [( element.attrs['synset_id'], element.attrs['name']) for element in
            soup.findAll('sense')]

#---------------------------------------------------------------------------------------------------------
def main():
    path_files = "D:\\CompTech\\Python\\projects\\get_giponim\\ruwordnet\\"
#-save ruthes_name from synset.N---------------------------------------------------------------------------    
    #rutes_names = []
    #rutes_names = parse_synsets(path_files + 'synsets.N.xml')#29296 строк
    
    #print(rutes_names)
    #print(len(rutes_names))
    
    #columns=['id', 'words']
    
    #df = pd.DataFrame(rutes_names, columns=columns)
    #print(df)
    #df.to_csv(r'D:\CompTech\Python\projects\get_giponim\ruwordnet\result\ruthes_name_synset.csv', sep=';', index=False,header=False)
#-------------------------------------------------------------------------------------------------------------

#---get names from file senses.N 
    senses_names_N = []
    senses_names_N = parse_senses ( path_files + 'senses.N.xml' )

    senses_namesN_df = pd.DataFrame (senses_names_N)
    print(senses_namesN_df)# [76817 rows x 3 columns]

    senses_namesN_df.to_csv (r'D:\CompTech\Python\projects\get_giponim\ruwordnet\result\senses_names_Noun_and_Verbs.csv', sep=';', index=False, header=False)
 
#---get names from file senses.V 
    senses_names_V = []
    senses_names_V = parse_senses ( path_files + 'senses.V.xml' )

    senses_namesV_df = pd.DataFrame (senses_names_V)
    print(senses_namesV_df) # [35279 rows x 2 columns]


    senses_namesV_df.to_csv (r'D:\CompTech\Python\projects\get_giponim\ruwordnet\result\senses_names_Noun_and_Verbs.csv', sep=';', index=False, header=False, mode = "a")

if __name__ == '__main__':
    main()
