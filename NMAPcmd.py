import pandas as pd
import subprocess
iplist = pd.read_csv('C:/SEPDiscovery/OOCLIP(parsed).csv',header=[0]) # For picking up the IP range from CSV file automatically
iplist.dropna(subset=['IPSegment'],inplace=True) #drop the dataframe without IP range
for iprange in iplist['IPSegment']:
    try:
        nmapcmd ='C:/Program Files (x86)/Nmap/nmap.exe -O -F -oX C:/SEPDiscovery/hostlist.xml --fuzzy --osscan-guess --osscan-limit --append-output ' + iprange #Append the xml file to store multiple outputs
        print(nmapcmd)
            
        nampprocess = subprocess.Popen(nmapcmd)
        output, error = nampprocess.communicate()
        nampprocess.wait()  # avoid process race condition, start another nmap cmd after the previous one is finished
    except:
        location = iplist[iplist['IPSegment']==iprange]['Location'].values[0]
        print('Fail to scan the network of' + location)
print ('INFO :NMAP scanning completed')
