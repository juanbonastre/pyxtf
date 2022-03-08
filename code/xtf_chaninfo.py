from utils import bytes_to_dword, bytes_to_float, bytes_to_int_list, bytes_to_string, byte_to_int, bytes_to_word

class XTFChanInfo():
    TypeOfChannel: int

    SubChannelNumber: int
    CorrectionFlags: int

    UniPolar: int
    BytesPerSample: int
    DReserved: int

    """ChannelName, 16 char long name of the chan info"""
    ChannelName: str
    VoltScale: float

    Frequency: float
    HorizBeamAngle: float
    TiltAngle: float
    BeamWidth: float


    OffsetX: float
    OffsetY: float
    OffsetZ: float

    OffsetYaw: float

    OffsetPitch: float
    OffsetRoll: float

    BeamsPerArray: int
    SampleFormat: int
    """53 bytes reserved"""
    ReservedArea2: list[int]

    def __init__(self, byte_array):
        self.TypeOfChannel = byte_to_int(byte_array[0:1])
        self.SubChannelNumber = byte_to_int(byte_array[1:2])
        self.CorrectionFlags = bytes_to_word(byte_array[2:4])
        self.UniPolar = bytes_to_word(byte_array[4:6])
        self.BytesPerSample = bytes_to_word(byte_array[6:8])
        self.Reserved = bytes_to_dword(byte_array[8:12])
        self.ChannelName = bytes_to_string(byte_array[12:28])
        self.VoltScale = bytes_to_float(byte_array[28:32])
        self.Frequency = bytes_to_float(byte_array[32:36])
        self.HorizBeamAngle = bytes_to_float(byte_array[36:40])
        self.TiltAngle = bytes_to_float(byte_array[40:44])
        self.BeamWidth = bytes_to_float(byte_array[44:48])
        self.OffsetX = bytes_to_float(byte_array[48:52])
        self.OffsetY = bytes_to_float(byte_array[52:56])
        self.OffsetZ = bytes_to_float(byte_array[56:60])
        self.OffsetYaw = bytes_to_float(byte_array[60:64])
        self.OffsetPitch = bytes_to_float(byte_array[64:68])
        self.OffsetRoll = bytes_to_float(byte_array[68:72])
        self.BeamsPerArray = bytes_to_word(byte_array[72:74])
        self.SampleFormat = byte_to_int(byte_array[74:75])
        self.ReservedArea2 = bytes_to_int_list(byte_array[75:128])

    def print(self):
        print('XTF chan info')
        print("\tTypeOfChannel: {}".format(self.TypeOfChannel))
        print("\tSubChannelNumber: {}".format(self.SubChannelNumber))
        print("\tCorrectionFlags: {}".format(self.CorrectionFlags))
        print("\tUniPolar: {}".format(self.UniPolar))
        print("\tBytesPerSample: {}".format(self.BytesPerSample))
        print("\tReserved: {}".format(self.Reserved))
        print("\tChannelName: {}".format(self.ChannelName))
        print("\tVoltScale: {}".format(self.VoltScale))
        print("\tFrequency: {}".format(self.Frequency))
        print("\tHorizBeamAngle: {}".format(self.HorizBeamAngle))
        print("\tTiltAngle: {}".format(self.TiltAngle))
        print("\tBeamWidth: {}".format(self.BeamWidth))
        print("\tOffsetX: {}".format(self.OffsetX))
        print("\tOffsetY: {}".format(self.OffsetY))
        print("\tOffsetZ: {}".format(self.OffsetZ))
        print("\tOffsetYaw: {}".format(self.OffsetYaw))
        print("\tOffsetPitch: {}".format(self.OffsetPitch))
        print("\tOffsetRoll: {}".format(self.OffsetRoll))
        print("\tBeamsPerArray: {}".format(self.BeamsPerArray))
        print("\tSampleFormat: {}".format(self.SampleFormat))
        print("\tReservedArea2: {}\n".format(self.ReservedArea2))