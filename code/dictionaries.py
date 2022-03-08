import constants
import xtf_data_packets
xtf_datapacket_types = {
    constants.XTF_HEADER_SONAR: xtf_data_packets.XTFPingHeader,
    constants.XTF_HEADER_NOTES: xtf_data_packets.XTFHeaderNotes
}