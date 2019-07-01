print "Which file would you like to copy from?"
from_file = raw_input()

print "Which file would you like to copy to?"
to_file = raw_input()

print "We will now join the files and read the product file."
opened_product = open(to_file,'r+')
opened_product.write(from_file)
print opened_product.read()
