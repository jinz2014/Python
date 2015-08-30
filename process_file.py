def skip_header(reader):
  # read the 1-line description (hardcoded)
  line = reader.readline()

  # expect multiple comment lines 
  line = reader.readline()
  while line.startswith('#'):
    line = reader.readline()

  return line


def process_file(reader):
  """ (file open for reading) -> int 
  """
  line = skip_header(reader).strip();

  largest = -1
  for value in line.split():
    v = int(value[:-1]) # remove the "." at the end of each number
    if v > largest:
      largest = v;

  # remaining lines
  for line in reader:
    largest_in_line = -1
    for value in line.split():
      v = int(value[:-1])
      if v > largest_in_line:
        largest_in_line = v;
        if (largest_in_line > largest):
          largest = largest_in_line

  return largest;


if __name__ == '__main__':
  with open('lynx.txt', 'r') as input_file:
    print(process_file(input_file))
    



  
