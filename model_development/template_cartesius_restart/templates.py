# -*- coding: utf-8 -*-
"""
This templates module can replace parts of an ascii file that are tagged with special characters
with values. This is often an easy way to write scripting tools. The following steps are needed:
- replace the changing parts of the input files with tags eg date="22-DEC-1999" by date="#DATE#"
 Here we assume that the # character does not occur elsewhere in the template file.
- create a python hash-table or dict with the keys and values
- apply the substitutions with a call to replace_all

Created on Mon Jul 13 20:14:55 2015

@author: verlaanm
"""

def replace_all(template_name,out_name,key_values,special_char):
    '''replace all occurrances of key between special_chars with the values '''
    f_in  = open(template_name,'r')
    f_out = open(out_name,'w')
    for line in f_in.readlines():
        #print ">>>"+line
        # look for the tags
        if( line.count(special_char)==2 ):
            print (">>>"+line)
            left_index=line.find(special_char)
            right_index=line.rfind(special_char)
            key=line[left_index+1:right_index]
            key_with_chars=special_char+key+special_char
            if(key in key_values):
                value=key_values[key]
                line=line.replace(key_with_chars,value)
            else:
                raise Exception("Could not find key:"+key)
        f_out.write(line)
    f_in.close()
    f_out.close()

def test():
   '''testing this module'''
   #write test template file
   f = open('test.tpl', 'w')
   f.write("name=%NAME%\n")
   f.write("tstart=%TSTART%\n")
   f.write("dt=%DT%\n")
   f.write("#Some other comment line\n")
   f.close()
   key_values={'NAME':'KATRINA', 'TSTART':'20080801','DT':'10'}
   #now apply substitutions
   replace_all("test.tpl","test.inp",key_values,'%')
   #and check the output
   f = open('test.inp','r')
   expected_output=["name=KATRINA\n","tstart=20080801\n","dt=10\n","#Some other comment line\n"]
   iline=0
   for line in f.readlines():
       if(iline<len(expected_output)):
          if(line==expected_output[iline]):
              print (iline,":OK:",expected_output[iline])
          else:
              print (iline,":ERROR:")
              print ("EXPECTING:"+expected_output[iline])
              print ("FOUND    :"+line)
       else:
           print ("Found too many lines in file")
       iline+=1
   if(iline<len(expected_output)):
       print ("Found too few lines of output")
   f.close()
   
# If this is run as the main program then run the tests
if __name__ == '__main__':
    test()