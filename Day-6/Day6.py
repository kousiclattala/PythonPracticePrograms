
# * A floppy disk shows 'f' bytes free and 'u' bytes used. if you delete a file 'o' size bytes and create a new file of size 'n' bytes
# * how many free bytes will the floppy disk have? . 'f' 'o' 'u' and 'n' are user-entered value.

class FloppyDisk:

    def __init__(self,free,used):
        self.free = free
        self.used = used
        
    def delete_file(self,o):
        self.used = self.used - o
        self.free = self.free + o
        print(f'The remaining free space after deleting {o} bytes of data is {self.free}')
        print(f'The total space used is {self.used}')


    def add_file(self,n):
        self.free = self.free - n
        self.used = self.used + n

        print(f'The space remaining after adding {n} bytes is {self.free}')
        print(f'The total space used is {self.used}')
        


free = int(input('Enter the Total free space available: '))
used = int(input('Enter the Total space used: '))

fd = FloppyDisk(free,used)
select = int(input('Select one option from the below \n1.ADD \n.2.Delete : '))

if select == 1:
    n = int(input('Enter the space want to add: '))
    fd.add_file(n)

else:
    o = int(input('Enter the space want to delete: '))
    fd.delete_file(o)

