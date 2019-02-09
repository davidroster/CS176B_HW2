#David Roster
#CS176B HW2

from functools import partial
import os
import sys

def read_sample(method, source_file, total_bytes, total_packets, total_loss, dest_file):
    create_dest_file(dest_file)
    with open(source_file, 'rb') as openfileobject:
        last_byte = iter(partial(openfileobject.read, 1), b'') #[0]
        for chunk in iter(partial(openfileobject.read, 1), b''):
            if(method == 1):
                count = 1
                loss_remainder = total_bytes // total_loss
                if ((count % loss_remainder) == 1):
                    #sample is saved
                    store_sample(dest_file, chunk)
                else:
                    #sample is lost
                    #make chunk 8 zero bits - silence
                    chunk = 00000000
                    store_sample(dest_file, chunk)
                count = count + 1
            if(method == 2):
                count = 1
                loss_remainder = total_bytes // total_loss
                if ((count % loss_remainder) == 1):
                    #sample is saved
                    last_byte = chunk
                    store_sample(dest_file, chunk)
                else:
                    #sample is lost
                    #replay last sample
                    store_sample(dest_file, last_byte)
                count = count + 1

def store_sample(dest_file, sample):
    with open(dest_file, "ab") as f:
        f.write(sample)

def create_dest_file(dest_file):
    f = open(dest_file, "wb")
    f.close()

def calculate_metrics(source_file, loss_probability, packet_size, ):
    total_bytes = os.path.getsize(source_file)
    total_packets = total_bytes // packet_size

    loss_percentage = loss_probability / 100
    total_loss = total_bytes * loss_percentage

    return total_bytes, total_packets, total_loss

def main():

    print("Let's get this money!!")

    source_file = input("What is the desired source file?")
    dest_file = input("What is the desired dest file?")
    packet_size = int(input("What is the desired packet size?"))
    #sample_size = int(input("What is the desired sample size?")) #Make sample size = 1 byte = 8 bits always! Way easier and follow mu law encoding 
    loss_probability = int(input("What is the desired loss probability - enter num between 1-100?"))
    #threshold = int(input("What is the desired threshold?")) #Do i really need this?
    method = int(input('''What is the desired Methods for alternate data? This is for the whole duration of audio file!
                     1=play silence, 
                     2=repeat sample, 
                     3=repeat packet'''))

    #Going to assume uniform loss over audio file

    total_bytes, total_packets, total_loss = calculate_metrics(source_file, loss_probability, packet_size)
    read_sample(method, source_file, total_bytes, total_packets, total_loss, dest_file)


if __name__ == '__main__':
    main()
