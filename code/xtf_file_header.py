from utils import byte_to_int, bytes_to_int_list, bytes_to_float, bytes_to_long, bytes_to_string, bytes_to_word
from xtf_chaninfo import XTFChanInfo 
from constants import XTF_CHANINFO_SIZE, XTF_CHANINFO_START_POS

class XTFFileHeader():
    """List of the chan info packages found"""
    XTF_chan_info_list: list[XTFChanInfo]

    """Looool"""
    FileFormat: int
    SystemType: int
    """RecordingProgramName must have 8 bytes length"""
    RecordingProgramName: str
    """RecordingProgramVersion must have 8 bytes length"""
    RecordingProgramVersion: str
    """SonarName must have 8 bytes length"""
    SonarName: str
    SensorsType: int

    """NoteString must have 64 bytes length"""
    NoteString: str
    """ThisFileName must have 64 bytes length"""
    ThisFileName: str
    NavUnits: int
    NumberOfSonarChannels: int
    NumberOfBathymetryChannels: int
    NumberOfSnippetChannels: int
    NumberOfForwardLookArrays: int
    NumberOfEchoStrengthChannels: int
    NumberOfInterferometryChannels: int
    Reserved1: int
    Reserved2: int
    Reserved3: int

    """ProjectionType must have 12 bytes length"""
    ProjectionType: list[int]
    """SpheriodType must have 10 bytes length"""
    SpheriodType: list[int]
    NavigationLatency: int
    ReferencePointHeight: float

    OriginY: float
    OriginX: float

    NavOffsetY: float
    NavOffsetX: float
    NavOffsetZ: float

    NavOffsetYaw: float
    MRUOffsetY: float
    MRUOffsetX: float
    MRUOffsetZ: float

    MRUOffsetYaw: float
    MRUOffsetPitch: float
    MRUOffsetRoll: float

    def __init__(self, byte_array):
        self.FileFormat = byte_to_int(byte_array[0:1])
        self.SystemType = byte_to_int(byte_array[1:2])
        self.RecordingProgramName = bytes_to_string(byte_array[2:10])
        self.RecordingProgramVersion = bytes_to_string(byte_array[10:18])
        self.SonarName = bytes_to_string(byte_array[18:34])
        self.SensorsType = bytes_to_word(byte_array[34:36])
        self.NoteString = bytes_to_string(byte_array[36:100])
        self.ThisFileName = bytes_to_string(byte_array[100:164])
        self.NavUnits = bytes_to_word(byte_array[164:166])
        self.NumberOfSonarChannels = bytes_to_word(byte_array[166:168])
        self.NumberOfBathymetryChannels = bytes_to_word(byte_array[168:170])
        self.NumberOfSnippetChannels = byte_to_int(byte_array[170:171])
        self.NumberOfForwardLookArrays = byte_to_int(byte_array[171:172])
        self.NumberOfEchoStrengthChannels = bytes_to_word(byte_array[172:174])
        self.NumberOfInterferometryChannels = byte_to_int(byte_array[174:175])
        self.Reserved1 = byte_to_int(byte_array[175:176])
        self.Reserved2 = byte_to_int(byte_array[176:177])
        self.Reserved3 = byte_to_int(byte_array[177:178])
        self.ReferencePointHeight = bytes_to_float(byte_array[178:182])
        self.ProjectionType = bytes_to_int_list(byte_array[182:194])
        self.SpheriodType = bytes_to_int_list(byte_array[194:204])
        self.NavigationLatency = bytes_to_long(byte_array[204:208])
        self.OriginY = bytes_to_float(byte_array[208:212])
        self.OriginX = bytes_to_float(byte_array[212:216])
        self.NavOffsetY = bytes_to_float(byte_array[216:220])
        self.NavOffsetX = bytes_to_float(byte_array[220:224])
        self.NavOffsetZ = bytes_to_float(byte_array[224:228])
        self.NavOffsetYaw = bytes_to_float(byte_array[228:232])
        self.MRUOffsetY = bytes_to_float(byte_array[232:236])
        self.MRUOffsetX = bytes_to_float(byte_array[236:240])
        self.MRUOffsetZ = bytes_to_float(byte_array[240:244])
        self.MRUOffsetYaw = bytes_to_float(byte_array[244:248])
        self.MRUOffsetPitch = bytes_to_float(byte_array[248:252])
        self.MRUOffsetRoll = bytes_to_float(byte_array[252:256])

        self.print()
        # Now obtain the chan info packages
        self.XTF_chan_info_list = []
        for n in range(0,self.NumberOfSonarChannels):
            pos = XTF_CHANINFO_START_POS + n*XTF_CHANINFO_SIZE
            XTF_chan_info = XTFChanInfo(byte_array[pos:pos+XTF_CHANINFO_SIZE])
            XTF_chan_info.print()
            self.XTF_chan_info_list.append(XTF_chan_info)


    def print(self):
        """print() prints in the console all the attributes found in the XTF file header"""
        print('XTF File Header')
        print("\tFileFormat: {}".format(self.FileFormat))
        print("\tSystemType: {}".format(self.SystemType))
        print("\tRecordingProgramName: {}".format(self.RecordingProgramName))
        print("\tRecordingProgramVersion: {}".format(self.RecordingProgramVersion))
        print("\tSonarName: {}".format(self.SonarName))
        print("\tSensorsType: {}".format(self.SensorsType))
        print("\tNoteString: {}".format(self.NoteString))
        print("\tThisFileName: {}".format(self.ThisFileName))
        print("\tNavUnits: {}".format(self.NavUnits))
        print("\tNumberOfSonarChannels: {}".format(self.NumberOfSonarChannels))
        print("\tNumberOfBathymetryChannels: {}".format(self.NumberOfBathymetryChannels))
        print("\tNumberOfSnippetChannels: {}".format(self.NumberOfSnippetChannels))
        print("\tNumberOfForwardLookArrays: {}".format(self.NumberOfForwardLookArrays))
        print("\tNumberOfEchoStrengthChannels: {}".format(self.NumberOfEchoStrengthChannels))
        print("\tNumberOfInterferometryChannels: {}".format(self.NumberOfInterferometryChannels))
        print("\tReserved1: {}".format(self.Reserved1))
        print("\tReserved2: {}".format(self.Reserved2))
        print("\tReserved3: {}".format(self.Reserved3))
        print("\tReferencePointHeight: {}".format(self.ReferencePointHeight))
        print("\tProjectionType: {}".format(self.ProjectionType))
        print("\tSpheriodType: {}".format(self.SpheriodType))
        print("\tNavigationLatency: {}".format(self.NavigationLatency))
        print("\tOriginY: {}".format(self.OriginY))
        print("\tOriginX: {}".format(self.OriginX))
        print("\tNavOffsetY: {}".format(self.NavOffsetY))
        print("\tNavOffsetX: {}".format(self.NavOffsetX))
        print("\tNavOffsetZ: {}".format(self.NavOffsetZ))
        print("\tNavOffsetYaw: {}".format(self.NavOffsetYaw))
        print("\tMRUOffsetY: {}".format(self.MRUOffsetY))
        print("\tMRUOffsetX: {}".format(self.MRUOffsetX))
        print("\tMRUOffsetZ: {}".format(self.MRUOffsetZ))
        print("\tMRUOffsetYaw: {}".format(self.MRUOffsetYaw))
        print("\tMRUOffsetPitch: {}".format(self.MRUOffsetPitch))
        print("\tMRUOffsetRoll: {}".format(self.MRUOffsetRoll))