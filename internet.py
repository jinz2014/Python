# urllib.request not supported in P2.7

from urllib.request import urlopen

for line in urlopen('http://tycho.usno.navy.mil/cgin-bin/timer.pl'):
  line = line.decode('utf-8') # binary data -> text
  if 'EST' in line or 'EDT' in line:
    print(line)





