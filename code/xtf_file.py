from utils import bytes_to_word, byte_to_int
from constants import XTF_HEADER_SIZE, MAGIC_NUMBER
import os
from xtf_file_header import XTFFileHeader
from xtf_data_packets import XTFDataPacket
from dictionaries import xtf_datapacket_types
import time

"""XTFFile is the main class that contains all the objects refering to the packages in the XTF file"""
class XTFFile:
    """The XTF file header headers"""
    XTF_file_header: XTFFileHeader
    data_packets: list[XTFDataPacket]

    def __init__(self, file_path):
        self.file_path = file_path
        self.data_packets = []

    def read(self):
        """The read() function reads the XTF file with the given url"""
        
        # Read the hole file
        byte_array = self.__read_bytes()
        
        # Get the file header
        self.XTF_file_header = XTFFileHeader(byte_array[0:XTF_HEADER_SIZE])

        # Get the data packets
        n=XTF_HEADER_SIZE
        last_percentage = 0
        while n < len(byte_array):
            s_start = time.time()
            percentage_read = (n/len(byte_array)*100)
            if percentage_read > last_percentage:
                # print("Data packets read {:.2f}%".format(percentage_read), end="\r")
                last_percentage += 1
            jump=1
            magic_number = bytes_to_word(byte_array[n:n+2])
            if magic_number == MAGIC_NUMBER:
                header_type = byte_to_int(byte_array[n+2:n+3])
                data_packet_class = xtf_datapacket_types.get(header_type, False)
                if data_packet_class:
                    data_packet = data_packet_class(byte_array[n:], self.XTF_file_header.XTF_chan_info_list)
                    self.data_packets.append(data_packet)

                    jump=data_packet.NumBytesThisRecord
                else:
                    print("Format error. Header type not found in dictionary...")
                    return
            else:
                print("Format error. Magic number does not match. Continue reading...")
                return
            n+=jump
            s_finish = time.time()
            print("Time passed {:.2f} s".format(s_finish-s_start), end="\r")

        print("Data packets read {}%".format((n/len(byte_array)*100)))
        
        
    def __read_bytes(self) -> list[bytes]:
        """__read_bytes() returns the bytes from a file with a given path"""
        
        # Check if file exists
        if not os.path.exists(self.file_path):
            print('File not found! Change the given path')
            return

        byte_array = bytearray()
        
        try:
            with open(self.file_path, "rb") as f:
                byte = f.read(1)
                byte_array.extend(byte)
                while byte:
                    if len(byte_array) % 1048576 == 0:
                        print('Bytes read: {} MB'.format(len(byte_array)/1048576), end='\r')
                    byte = f.read(1)
                    if byte: byte_array.extend(byte)
                print('Bytes read: {} MB'.format(len(byte_array)/1048576))
        except IOError:
            print('Error While Opening the file!')
        
        return byte_array

