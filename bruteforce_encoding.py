import xml.etree.ElementTree as ET
import sys

encoding_standards = ['ascii', 'big5', 'big5hkscs', 'cp037', 'cp273', 'cp424', 'cp437', 'cp500', 'cp720', 'cp737', 'cp775', 'cp850', 'cp852', 'cp855', 'cp856', 'cp857', 'cp858', 'cp860', 'cp861', 'cp862', 'cp863', 'cp864', 'cp865', 'cp866', 'cp869', 'cp874', 'cp875', 'cp932', 'cp949', 'cp950', 'cp1006', 'cp1026', 'cp1125', 'cp1140', 'cp1250', 'cp1251', 'cp1252', 'cp1253', 'cp1254', 'cp1255', 'cp1256', 'cp1257', 'cp1258', 'euc_jp', 'euc_jis_2004', 'euc_jisx0213', 'euc_kr', 'gb2312', 'gbk', 'gb18030', 'hz', 'iso2022_jp', 'iso2022_jp_1', 'iso2022_jp_2', 'iso2022_jp_2004', 'iso2022_jp_3', 'iso2022_jp_ext', 'iso2022_kr', 'latin_1', 'iso8859_2', 'iso8859_3', 'iso8859_4', 'iso8859_5', 'iso8859_6', 'iso8859_7', 'iso8859_8', 'iso8859_9', 'iso8859_10', 'iso8859_11', 'iso8859_13', 'iso8859_14', 'iso8859_15', 'iso8859_16', 'johab', 'koi8_r', 'koi8_t', 'koi8_u', 'kz1048', 'mac_cyrillic', 'mac_greek', 'mac_iceland', 'mac_latin2', 'mac_roman', 'mac_turkish', 'ptcp154', 'shift_jis', 'shift_jis_2004', 'shift_jisx0213', 'utf_32', 'utf_32_be', 'utf_32_le', 'utf_16', 'utf_16_be', 'utf_16_le', 'utf_7', 'utf_8', 'utf_8_sig']

#originalData = "âëâOâgâîâCâô_Chorus.mp3"

try:
    targetEncoding = sys.argv[1]
    originalData = sys.argv[2]
except:
    print("Error: please supply a target encoding scheme")
    print("Format: {} [encoding] [message]".format(sys.argv[0]))
    print("[encoding]: target encoding scheme, in other words: the message's original encoding scheme (you must guess it)")
    print("[message]: message to bruteforce")
    print("The arrow in the output (-->) means 'reencoded as'")
    sys.exit(-255)
#targetEncoding = "SHIFT_JIS"
print("Now attempting to decode as {}: {}".format(targetEncoding, originalData))

encodingTries = []  
for encoding in encoding_standards:
    try:
        reencode = originalData.encode(encoding)
        decodingAttempt = reencode.decode(targetEncoding)
        if not decodingAttempt in encodingTries: # Filters out duplicates, such as CP437/720/850/852/857/858/863/865 can have similar results and floods the terminal
            encodingTries.append(decodingAttempt)
            print("{} --> {}: {}".format(encoding, targetEncoding, decodingAttempt))
    except:
        continue
        print("Decoding failed: {} --> {}".format(encoding, targetEncoding))
