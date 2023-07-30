from sqli import *
from xss import *
def main():
   
    while True:
            str=input("SELECT THE SCANNER TO BE PERFORMED\n1.xss scanner\n2.sqli scanner\n3.crlfi scanner\n")
            if str.lower()=="xss scanner":
                    url = input("ENTER THE URL:")
                    if scan_xss(url)==False:
                            print("THE GIVEN URL IS SECURE")
                           
                    else:
                            print("THE GIVEN URL IS INSECURE")
                            
            elif str.lower()=="sqli scanner":
                    url1 = input("ENTER THE URL:")
                    scan_sql_injection(url1)
                    continue;
            else :
                break;
if __name__=="__main__":
    main()

        
