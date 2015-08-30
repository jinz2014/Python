# not support in P2.7

import sys
'''
2. This with statement takes a comma-separated list of contexts .  The comma-separated list acts like a series of nested with blocks.  The first context listed is the “outer” block; the last one listed is the “inner” block.  The first context opens a file; the second context redirects sys.stdout to the stream object that was created in the first context.

3.  Because this print() function is executed with the context created by 
the with statement, it will not print to the screen; it will write to the file out.log .  

4.  The with code block is over.  Python has told each context manager to do whatever it is they do upon exiting a context.  The context managers form a last-in-first-out stack.  Upon exiting, the second context changed sys.stdout back to its original value, then the first context closed the file named out.log .  Since standard output has been restored to its original value, calling the print() function will once again print to the screen.
'''

class RedirectStdoutTo:
  def __init__(self, out_new):
    self.out_new = out_new

  def __enter__(self):
    self.out_old = sys.stdout
    sys.stdout = self.out_new

  def __exit__(self, *args):
    sys.stdout = self.out_old

if __name__ == '__main__':
  print('A')
  # chain multiple context managers in a single 'with' 
  with open('out.log', mode='w', encoding='utf-8') as a_file, RedirectStdoutTo(a_file):
    print('B')
  print('C')
