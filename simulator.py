#David Roster
#CS176B HW2

from functools import partial
import os
import sys

def read_sample(method, source_file, total_bytes, total_packets, total_loss, dest_file):
    create_dest_file(dest_file)
    with open(source_file, 'rb') as openfileobject:
        for chunk in iter(partial(openfileobject.read, 1), b''):
            if(method == 1):
                count = 1
                loss_remainder = total_bytes / total_loss
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
                print("This is where I am getting confused what to do")

def record_prev_sample(prev_sample):
    temp = prev_sample

def store_sample(dest_file, sample):
    with open(dest_file, "ab") as f:
        f.write(sample)

def store_alternate_data(sample_size):
    new_file = open("test_pinkpanther.au", "wb")
    new_file.close()
    with open("test_pinkpanther.au", "ab") as f:
    #Methods for alternate data

        alternate_date = 1
        if (alternate_date == 1):
    #1. Make sample all Zeros (Playling Silence)
            zero_sample = sample_size * 0
            f.write(zero_sample)

    #2. Repeat last sample sent
        if (alternate_date == 2):
            print("Resending last sample")

    #3. Repeat last packet sent
        if (alternate_date == 3):
            print("resending last packet")

def create_dest_file(dest_file):
    f = open(dest_file, "wb")
    f.close()

def calculate_metrics(source_file, loss_probability, packet_size, ):
    total_bytes = os.path.getsize(source_file)
    total_packets = total_bytes / packet_size

    loss_percentage = loss_probability / 100
    total_loss = total_bytes * loss_percentage

    return total_bytes, total_packets, total_loss

def main():

    print("Let's get this money!!")

    source_file = input("What is the desired source file?")
    dest_file = input("What is the desired dest file?")
    packet_size = input("What is the desired packet size?")
    sample_size = input("What is the desired sample size?") #Make sample size = 1 byte = 8 bits always! Way easier and follow mu law encoding 
    loss_probability = input("What is the desired loss probability - enter num between 1-100?")
    threshold = input("What is the desired threshold?") #Do i really need this?
    method = input('''What is the desired Methods for alternate data? This is for the whole duration of audio file!
                     1=play silence, 
                     2=repeat sample, 
                     3=repeat packet''')

    #Going to assume uniform loss over audio file

    total_bytes, total_packets, total_loss = calculate_metrics(source_file, loss_probability, packet_size)
    read_sample(method, source_file, total_bytes, total_packets, total_loss, dest_file)
'''
    #Make sample all zeros
    if (method == 1):
        create_dest_file(dest_file)
        with open(source_file, 'rb') as openfileobject:
            for chunk in iter(partial(openfileobject.read, 1), b''):
                count = 1
                loss_remainder = total_bytes / total_loss
                if ((count % loss_remainder) == 1):
                    #sample is saved
                    store_sample(dest_file, chunk)
                else:
                    #sample is lost
                    #make chunk 8 zero bits - silence
                    chunk = 00000000
                    store_sample(dest_file, chunk)
                count = count + 1
    
    #Repeat last sample sent
    if(method == 2):
        create_dest_file(dest_file)
        with open(source_file, 'rb') as openfileobject:
            for chunk in iter(partial(openfileobject.read, 1), b''):
                prev_chunk = ()
                count = 1
                loss_remainder = total_bytes / total_loss
                if ((count % loss_remainder) == 1):
                    #sample is saved
                    store_sample(dest_file, chunk)
                else:
                    #sample is lost
                    #Repeat last sample sent
                    
                    store_sample(dest_file, chunk)
                count = count + 1 
'''

if __name__ == '__main__':
    main()
