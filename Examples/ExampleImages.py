#----------------------------------------------------------------------
# This file was generated by .\convertImages.py
#
from wx import ImageFromStream, BitmapFromImage, EmptyIcon
import cStringIO, zlib


def getGroup16Data():
    return zlib.decompress(
'x\xda\x017\x01\xc8\xfe\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x10\
\x00\x00\x00\x10\x08\x02\x00\x00\x00\x90\x91h6\x00\x00\x00\x03sBIT\x08\x08\
\x08\xdb\xe1O\xe0\x00\x00\x00\xefIDAT(\x91\x85\x92\xc1u\xc30\x0cC\x117Sh\rt\
\r\xadA\xceD\xcc\x9150G\xc7P\x0f\xb2]5\xcf\xcf\xc1I\x96\xf8\x01\x89\xe6c\x8c\
\x01@\x92m\x00U\x85{\x8d1\xaaj\x8c1\xc6\x88\x88\x88\x18\x87\xaaj\xfd\x9c\xda\
&v&\x9c\x92\x14\x11$3s\xdd\xdfl\x03\x94\x9c\x99+2y\x92oF_\x00z\x8f\xde{kA\
\xf6\xd6\xba\x94\xad5+\x7f\xd0^\xafWk\xad\xf7\xfe\x97p\xaeH\x90\x98vRV\x85\
\x95\xb0\xc2\xca\xfc>\xcb\x9ek\xdc\x12n\xd8U\x01\x00\x16\xe4k\xe0]\xd6d\xff=\
\xba\xaa\xa4\xa5\x0fRD\xdc\x98l\x87\xd7\xbc\xbb\xbd\x1b\xf2\x03\xb0c$\x08I+`\
\x03\x8ck`)\xf2^\xea\xd9:K\x9aG\xb7\x8f\x9eW\xf3n\x91\x99$\x8f\xd1\xb0>\x90G\
\xf2\x13\xc7\x84f\xa6$\x92\xf6\xc5D\xecy\xe4c\x8e\xf7\xd49gUe[\xca\xfd_2H\
\xcev\xff\x02\x0b[\xa5cP|\xd5p\x00\x00\x00\x00IEND\xaeB`\x82\xf3\x99\x84Y' )

def getGroup16Bitmap():
    return BitmapFromImage(getGroup16Image())

def getGroup16Image():
    stream = cStringIO.StringIO(getGroup16Data())
    return ImageFromStream(stream)

#----------------------------------------------------------------------
def getGroup32Data():
    return zlib.decompress(
'x\xda\x01\xde\x01!\xfe\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00 \x00\
\x00\x00 \x08\x02\x00\x00\x00\xfc\x18\xed\xa3\x00\x00\x00\x03sBIT\x08\x08\
\x08\xdb\xe1O\xe0\x00\x00\x01\x96IDATH\x89\xb5\x95[\x96\x84 \x0cD+}fGaM\xb0\
\xa6dM\xb2\xa6\xccG|D\x05zlz\xea\x0b\x8f\x9aK\x85\x02`ga\x133\xdb7\xf4BPJ\
\xc9\xcc\x96e\x11\x11\x00D\x84y\xed\xa8\xcb\x94E\x84\x99\xe3\x07\xb3\x0ej\
\xad\x17\xb6\x03\x9a\xa2M)\xa5\xb1\x81\x03\xc0\xcc\xaa\x1aaw\xa4\xebQ\'\x7f\
\xa2\x83\x1d0\xae\xbe,\x8bO\xc8-\xaa*\x11Y\x08H\xc3\x01\x11\x89X\xdd\xe4\xa4\
Z\xeb\xfd\xb7G\x9d\x04\x00/af"\x96\xf3\xa9\xdc\xfe\x18\x17\x8d\x99E\xc4\xc7\
\xde\xa5q\x16\xd6\x16\xa9"\xe7\xb5\xda\x85\xc1\x8c\xd8\x81?vr\xd7\xb1\x06\
\xfe\x97\xc81\xdeJ\x1cc"2\x01\x95\xba\xa7\x80\x99\x9b\x9dl\x00"\xc6\xdd\xa8\
\xde\xaa\x9bA\xc92(\xe4\xcd\xf2\x1a\xa4&\xe6\n\x88\x98\x86{%d\x03`8E\xd32p\
\xee\xe4\x1b\xc0HJ\x00 v\x8c]\x9d\xb5x\x0e\x88\x98\xbca\xfa+\xfd) b\x869z\
\x8d^~C/\x00fVJ\xff<\xd17I\x7f\x0f\x18I\xab"\rb\xfe\x18PK\x98\xef\xdc\xdc\
\xdb\x80+)3\x80R\n\x003\xa3\xd2-\xd4;2\xfa-\xca\xec\xd5]\xce\x18TO\xb5\xbd\
\x93\x1f\xa4(2j\xe7\xb0\x9a\x024\xe5$\xbf\x11\x9a.\xe76\xdaVz\x973\xfc*u\xfd\
\xcbF+\xa5\xecnf\x1d\x8c1\x88\x0eF\x9byB\xab\x03O\x98\xdf\x1b\x12nMU\xca\xdb\
]:\x05\xb8c\\\xb1\xba\x88\xc4\xdb\xf8\x13@\xc4\xf4D\x05&\x83\xf7\x87<K\xcf\
\x169Z\x8c\xb3 \xbdz=^}|R\x0e:\x19?\xfb\x05+L\xbc\xc4\xa4k\x1fx\x00\x00\x00\
\x00IEND\xaeB`\x82\xc6\'\xc9\x85' )

def getGroup32Bitmap():
    return BitmapFromImage(getGroup32Image())

def getGroup32Image():
    stream = cStringIO.StringIO(getGroup32Data())
    return ImageFromStream(stream)

#----------------------------------------------------------------------
def getMusic16Data():
    return zlib.decompress(
'x\xda\x01\xba\x02E\xfd\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x10\
\x00\x00\x00\x10\x08\x06\x00\x00\x00\x1f\xf3\xffa\x00\x00\x00\x04sBIT\x08\
\x08\x08\x08|\x08d\x88\x00\x00\x02qIDAT8\x8d\x8d\x92MH\xd3q\x18\xc7?\xff\xff\
\xfe{\xd1\xe96u\xba\xcd\xa6\xa0f\x18fJX\x84\x06\x19\x18Z\x16a\x8c\xec \x9d\
\x82 \xe8\xed\x10\x11]\xbbx\xe9\x10t\x8a\xe8\xd2\xa5\x17#\x88\nC\xa2\x1013\t\
K\xcc\x10-\xd1\xb9Ms\xc3\xbd\xe8\xdc\xfe\xfb\xff:\xa8esP\xcf\xf1\xf9>\xdf\
\xef\xf3}^$\xfe#\xc6\x06\x07\x0b\x9cf\x9d9\xa8*\xf1\xeduu\xf3\x9b1)\x13\xa1\
\x0e<m\xbb8}\xb8\xc9~\xc0Y^\xe80\xe4\xe8\x91\xe5$"\x12$\xb9\xb0\xc8\x87\xf7\
\xeah\xe7\x1b\xf6\x01+\x7f\t8\xc0\xfc\xf4\\\xc1d\xc3\xa5\xe3\x0e\xaa\xaaA5\
\x81&@\x8d@l\x01\xc2>\x88xI\x8dMP\xd4\x19\xd8\x1f\x84Ae\xb3@\x00\xa4\xea\x96\
=\x0e*\xea \x96\x0f:+\xe8\x14\xd0G\xc0j^+J\xac \xdbl\xd8\x08\x14\x07\x81\xbf\
\x04\x80h,\x94\xc0*\xdb!\xa7\x12\x92&b\x9f\x07X\xf1\x8f\x91\\\xf2\xa2(Q,\xa5\
\x06\x8c\x85\x16\x8ae\xdcSZ\x86\xf9\xbfv\xed\r\t\xf1B\xf4]\xa9\x9f9a\xe5r\
\xa5\x9eZ g\x1d6\xddjP^\x8a\xef\xcd\xa2=\x97.28\xc0;\x1f\xf1U-L\xdb.\xde\xfe\
x\xfeS\x8a\xe7ip|\xe8\x87:\x80\x96:RZ\x88\x9b\x08\xc8\xe9\x02\xd3\xb3\x8b~\n\
\x15\xdc\x16\xdc[\xaec\xa69W\xa3\x84\xb9\x10e\x0eJ2:\x98\xf7\x85\x03\x10%\
\xcf\x84s#\xe7\x82\xaa\x9e\xeb\x15\xc3\xd5\xed\xb5\xd9j8\x00I?\xee\xbc\xb5\
\x06[\x1c\xcc\xfaW\xbd\xacNa\xb7\xeb\x1c\x1b\xb9\xbbg\n\x1e\xd5\\k\xcd\x96\
\x8d+\x18\x0cQ\x88-RnOs\x90\x0f\xdb\x1a\x1d\x9c\xcc\x8a\xb3\x9b\x99\t*\\z\
\x17_R\x00\xec(1\xb9\xf0~\x83\xa0\x1f\x96|\x90\x08\x93X\xe5\xcf\rjtxB7d!\x1e\
\xea\x84xf\x15\xe2m\x99\xe8\xee0\rn\xe0\x1e7\x17V\xef9\x85\xe8\xb1\x08\xd1-\
\x8b\xe5\x9b\xb28h\xe4,\xac\xbf\xf2\x90\x87x}\x8bbDh`\x10\x90-\xf3\xee\x95\
\x98i\xba\xaf\x95n\x88\xd4\xe6\xd0x\xc8\xcd)U#\xd13\xcb\x83\x89eF~\x8f`\x920\
\x12\x93@\xd2\x81*@\x81p(\xb5\xb4y7#Q\xfaG\xc6\xe9O\xdf\x99\x0e`t\x9c\x9fm\
\xa5\xda\xd1,\xbd\x86\x1a\xd7\x98\x1c\xd6\xe8x\xc2\xb1\xb0\xc6\\:!=\x14\x80>\
\x8d;\xbd;\xbb^\xd7\x17I\xad\xcb*\x91^\x93\xf4xV\xbd\x1a\xfb\x17\x19\xe0\x17\
\xd0\xed\xebS\x0fL\x08\xf6\x00\x00\x00\x00IEND\xaeB`\x82 ^9\xf8' )

def getMusic16Bitmap():
    return BitmapFromImage(getMusic16Image())

def getMusic16Image():
    stream = cStringIO.StringIO(getMusic16Data())
    return ImageFromStream(stream)

#----------------------------------------------------------------------
def getMusic32Data():
    return zlib.decompress(
'x\xda\x01\xa9\x06V\xf9\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00 \x00\
\x00\x00 \x08\x06\x00\x00\x00szz\xf4\x00\x00\x00\x04sBIT\x08\x08\x08\x08|\
\x08d\x88\x00\x00\x06`IDATX\x85\xcd\x97kl\x1cW\x15\xc7\x7f\xf7\xce\xec<v\xd7\
ko\xbc\xb1\x9d\xc4I\x9c\x07i\x9c> \x8fBM\t\x10Z\x9e\n*\x01A>\x90R\xa9\xaa\
\x04\xdf\x80\n\x12\t!!U\xb4\xa8\x82\x82\xc4\x17\x90\x10\x12\xa2\x12B\xfd\x06\
i*\x10%J\x81\x82\xa24m\x11y9\x8e\xdd\xa4\xc1\x9bd\xd7\xbb\xeb\xdd\xd9\xddy\
\xcf\xe5\xc38\x0f\xe2\x14oP$8\xd2h\xae4\xf7\x9e\xf3\xdb\xff=\xf7\xdc\xb3\xf0\
?6q\'\x9c\xbc\xf0\xdcw\x96Ea\xbc"B\xf5\xbfw\x98B\x92\x08}\xb6\xab\xda\xb3\
\xbet4\x19\x97\x1f}\xf2\x99Kw\x0c`<\xc7\xdd[\x07\xf8\xd8\x86\x1c\x1f\xb8\xbf\
\xc8}a\xccFs\x00\xac\x01\x9dL\xce@\xe8\x1aR\x83\xd8\xf5\x89\xbd\x00w\x1e|\
\x07U\xf19\xfa\xd2%~\xf2\xdb\xcb\xfc\xf2F\x7fz/A\xd7\x17\xe9\xdf]\xe2\xc9\
\xdd+\xf9\x8a\xbe\xcc\x1cZ~\xff\x06\x067\xaf\xa5\xb0a\x84\xdc\xe8 H \x0c!\
\xf2!\xf4\xc0\xef@\xd8\x05\xbf\r~\x0b\x9c\xa6\x98\x9b\xaa=p\xef\xe1\xd6\x03\
\xc9\xdf\xd4\xec\x8be\xfe\xd83\xc0\xd7\xc6\xd9\xff\x89a\x9e]\xf5\xe1M\x8c}\
\xfa}\xe47\xad\x05\x0c@\x03% Q\xa0\x12\xd0\x02P\x1e$:\xe8\x12b\x012\x01\x11\
\x83\x11S\xba+\xa6:\xedb\x1e\x0b6C\x8f\x00{V\xf3\xd1=\xf7\x18\xcfN<\xb5\x97\
\xcc\xf2a\xd0l\x88\xb3 ,\x10\x99\x14B\x02\xc4 \x03\xd0<\xd0M\x90\x12\x10\xa0\
\x14$\tD\x11\x10`\x16,VY\xc1\xaa\x9e\xb7\xe0D\x8dj&\x9f%34\x04\xd8 \x0b \xb2\
\xe9\xa3\x0c\x90Z:1\x89A\xfa\xa0\xdc\xd4\xa5)@\x01q\x04I\x08\xb1\x07\xca\xc6\
\xe83Y\x91ce\xcf\x00\xb1\xa0\xec\xd6\xdb`\xe6!\xca\x82\xc8\x03y\x90\xb9T\x85\
\xab\xcbe\x98\xca\x1fg@\n \x01#\x848H\xf3B\xb7A\xf3\xb1\x07,\x82\x98\xde\x15\
\x98\xe9P\t\x9a\x11\x18Y\x88m\x109\x90y\x90}\xe9X\xb3R\x15d\x04tAu@\x99i\x1e\
$\x02\xb4\x08T\x00Q\x17\xb4\x0cf\xbf\xc5D\x89\xd5=\x03\xa42\x10\xa8Nb\x08\
\xcdL\x7f\xb5\xcc\x83\xb5\x1c\x15\x1a\xd4\xde8J\xe3\xc41\x9c\xb7N\x12T\xde\
\xc6k\xd4\x08\xdb\x1dT\x14\xa1\xdb&V)O~m\x89M\x0fo\xc022X\xfd\x16q\xcc\x8a\
\xdb\x02\x90\x82\xb2\xd7\xe8\x8c\xd9C#\xa0[\xf8M\x97\x13\xdf\xfb:\xd5#\x87\
\xb9\xec\xf2\xe7\xd7\xea\xbc2\x17p\xe2x\x8d\xb3BQ\xb1\x0b\xcc7\xaf\x10\xdbY\
\xbf\xa8\xeb\xfe\xaa\xbdkj_\xfed\xd3yb\xfb\x97\xeeA/\x98(I\xe1\xb6\x00f]*\
\xfe|w\xcc\x1e\xd1\xf0\xe7[\xfca\xef>\x8e\xce\xf1\xed\xe7O\xf2\xdc\x05\xf0\
\x16-p\x17\xde].\x01\x97\xe4E\xe2]\x95\xd6\x13h\x12\x94\xc2\xea\x13\x0c\xa2V\
\xd6\xa0\xdc\x13@\xd9\xa3\x1c\xd4\xeb\xa0kT\x8f\xbd\xca\xb9&\xbf\xfe\xeeI\
\x9e^j\xddU\xf3u\xceu\xaa\x9d\xb4\xe6*\x85]\xd0\x81p%\x0b\x00r)\x07\x9a\xe0\
\x8a\xdfl\x81\n\xb0\x97\x15iG\x14{\r\x0e0Y\xc3\x89]\x15\xaa\x8e\x07I\x82\x91\
\xd3\xd9\xd1\xcf\x9a\xab\xdf\x97\x04\x98lR\t\xea\xf3\xa0<2\x05\x8b\xbb\n\x0c\
\xdd\x0e\x00\x80\x14\xcct\xab\x0e$\x11V\x9f$T\xd7k\xc1\x92[\xe0$\x94\xfdZ\
\x1dT\x17\xb3h\xd0\xa7\xfd{!\xb9\x95m]\xce\xc6\x0f-\xe3\xd1!\x93{cE\xbe\xec0\
\xd8\xa9:\xe4r\x02+\'\xd8\\`\xf4p\xabG\x00]R\xf1\x1aM\x88\x1c\xccb\x1f\x8a\
\xff\xac\xc0\xf7\xb7\xf1\xfc\xd6!\xf6\xadz\xf8\xdd\x14\xd7\x15\xc9h\x01\xcd\
\xf3\x15\n%\x1d\x82\x0ev6!\xa7_\xaf\x05K\x02L9\x94\x83Z3\xbd\xd5r\x12a 6\x82\
y\x0e\xfc\x9b\xe7\xfet\x07\x7f\xda\xbek\xfd\xce\x1d\xdfx\x04\x826t\x1a\xe0\
\xb6X6\x92@\xbb\x01\x9e\x8fiGd\xb5\xeb\xd5p\xc9\x1ch\xc7\\\xf1[]\xf0Z\xd0\
\xaec\x97rD\x03\x8c\xdc<\xef\xf3ky\xfc\xbe\xf7\x94v\xee\xf8\xd6g\xd2`N\x03\\\
\x07\xbc6\xb8m\xf0]\x08\xbaXf\xc4\x96\x01F{\x06\xd0\r\xaa\xde\xbc\x97*\xd0m`\
\xf6\x19\x08\x7f\xf16\xec\x1e\xe1\xb1\x8d{\xb6A\xbd\n\xdd&x\xceB\xe0\x0ex\
\x1d\x08\xdb)\x80\xa5\x88\xd5m\x00\x9c\xaa\xd2V>\xd0\xaaCw\x9eL\xd6`bxq"\xae\
\xc8R\xca\xe6E*\xbb\xdfL\x15\x0b\x1c\xf0\x1d\x08;\xe0w!L\x90J"n\xd8\xfa[\xe5\
\x80\xf5\xd5\xcd\xec\xdf9\xc4g\xf3\x1a\xe3\t\xc8\xf9\x0e\xca\xaf\xce\t\xb3\
\x14b\xe5\x05~\xb2X\x81\xa96S\xe3g.l\xc9m+\x81\xe7B\xe8\x82\xd7M\x83{-\x08BP\
\x82\xf2\xb4b\xce\xe3/\xb7\x04\x98(\xf1\xc1\xa7\xb6\xf2\xbb\xe5\xeb\xb0\xd7l\
\x11\xf4\x8f\x18\x08+K\xbbe`\xd2\x86v\x84a*\xf2rq\x0e\xfc\xea<?\x18?8\xf9\
\xc8\x8a\xf5\x02M\x06\xe0y\x10\xb8i[\x16E\x80 p\xe0\xf4\xb1\x84\x9f\x9d\xe5\
\xc0\xd5u\xda\xd5\xc1:\x83M?\x9a\xe0\xf8\xf6]Zfl\x8b\xc4\xb6\x05B\xc5\x88$\
\xc0\xb4\x93\xb4\xe9\x88C:u\x9f\xcb\xd3\xee\x99\x97/s\xe8F\x80\x8b]\xde\x1e\
\xd4\x08\x8d\xc9\xb9\x87,;\xa6\xaf\xbf\x9b^\xc3I\x0c\xa1\xe0\xfc)\xc5\x1bG\
\x12^\xba\xc8\xe3\xbf\xb9\xc2\x8b\x8b\x148\xb0\x85\x1f\xbf\xebnA\xb1(\xd2+F\
\x02\x9a\x82XA\xe4\xa6\xed\x96i`j\x10\xdfb\x0b\x00~x\x9ag&[\xfc\xf5\x0b\x8d\
\xd6\xd3\xc3Y\xde\x9f-\xa4\xedb\xd7\x81\xb7\x1c\x0e\xfe|\x9a\xfd\xc7k\x9c\
\xb9q\xcd5\x80\x92\xc5\xc7\xd7\xac\xd6\xd3\xd3-\x13\xc8\x90R$\xc9B{\xa5 \xf1\
15\x85\x12\xef\\\x8c\x0e\xcdr\xe4\xd0,\x0fn\x87L\xa7\x8fu\xb1$\x9aj2\xf3N\
\xf3\xaf\x01(\x80\x98\xb4\xcb\xd5\x16\x0eG\x92\x80\x90\xe9G\x99\x80\x12\xc4.\
\xe8B-*B7\xdbq\x08q8\xbb\xd4\xbck\xc7\xd0\x8d\xf9\xc7\xdce\x05\x91\x84H@\xa0\
 \\h\xaf\xc3\x85\xb1\x12L\x9fJ\x98isp)\xc7\xbd\xda\xb5$\x0cBf\xd6\x1b\xc9\
\xbe\xd1!\x89\xa6\x89\xb4\xe7W*\xed\xed\x10\xa0\tN\xbf\x19s\xe1\x1c3\xdf|\
\x9d/\xdeq\x80\xa9.\xd3\xa5\x0cs\x19\'\xf9T\x14\x81\xa1\x0b2\x9a \x0c\xa0z%\
\xe1\xcd\xd7"\xfey\x91\xbf?\xf6\n\x0f\xfa\xb7\xea\x84\xfeK[\xf4\xdfp\x18\xc6\
>7\xca\x81]#|$T\xac\xd6\x04\xadI\x87\xd7_\xad\xf0\x8b\xdf7x\xe1N\x05\xfe\xbf\
\xb1\x7f\x01ZO\xc0s\xed\x0ev\x00\x00\x00\x00\x00IEND\xaeB`\x82~\x17/$' )

def getMusic32Bitmap():
    return BitmapFromImage(getMusic32Image())

def getMusic32Image():
    stream = cStringIO.StringIO(getMusic32Data())
    return ImageFromStream(stream)

#----------------------------------------------------------------------
def getUser16Data():
    return zlib.decompress(
'x\xda\x01\xab\x02T\xfd\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x10\
\x00\x00\x00\x10\x08\x06\x00\x00\x00\x1f\xf3\xffa\x00\x00\x00\x04sBIT\x08\
\x08\x08\x08|\x08d\x88\x00\x00\x02bIDAT8\x8d\xb5\x92KHTq\x14\xc6\x7fw\xee\
\xbd:\xd9\xf8\x9c\xb4T\xa61\x1fD\x89\xa91\x04A\x86\x11\x99Dn\n\xb2\x08\xa4Z\
\x14\xe8\xa6U\xb4\x10\x82\x16AA.\x02wA\x0f\nWm\xc2"2\x12L\x82t\x12\xb5\x87\
\x90\xa4\x89\x98:\x8d\xf3\xb8sg\xe6\xde\x99\xb9\xf7\xdf\xc6ELQn:\xcb\x8f\xef\
;\xe7|\xdf9\xf0\x9f\xcaq\xb1\x9e{\xfe\xdb\xa7\x84\xbf\xafS\xf44\xf2\x00\x907\
\xac\x1e\xe8\xaa\x1a\x17\x81wB$\x03B\xa4\x82B\x84&\xc4@W\xed\xfb\r\x89[+9i\
\x8f\xf5\x0b\xb1\xe2\x17"\x11\x14\xc2\x88\n\x11\x98\x12b\xe2\xaeh\xad\xa0\
\xf3\xb7U\xb3\x81#M\xe5g\xa4\xd220\xe3`\x84 \x19\x04S\x07w)\xc7|\x95\xa7\xb3\
\xf9J6\xd0XS^E\\\x03U\x01i}\x86\x19\x86t\x98=5\xdb\xaa`\xe9\xef\r\xbe\x87b\
\x1a\x89\x04B\xcd Y\x06 !2q\xa4\xb4\xc1r(\xae\xfd\xd3\xc2\x9b\xc9\x85a3\xaca\
\xc642\xda\n\xb6\xb6B*\x1a&\x1d\xd6\x18\x99\x9c\x1f\xce\xe6K\xd9\x00\xa0L\\\
\xd9\x1f\xad;\xd4\x91gc!!\xe1\x90dfG\x9e%\x9bo\x8c\x96\x00\xc6\xaf\xe4\xec\
\xdb\xe6\xd2\xc2U\xbd\xda\xdd\xec\x99\xf9\xbaY\x91\x15\x12\x91\x10\xb3c\xa3\
\xf4)Z\xf8\x93\xfd\xc3b\x91\xb7\x7f\xb6PC\xfb\xf1\';\xe3\x03C\xdd\xd7\x1d\
\xf5\xdeRo\xcfS>\xd8^>\xda\xd5\xec\xe8\x19\xc4\xd1\xe0){<t\xe9V\xeb}\x8f\xc6\
\x16\x9a\xb3-4\\\x18\xdd7\xdd\xb6\xd7\x87b\xbb\x08\x86b\x8c\x0c/p\xd6\xd7\
\x8d%l\x1e\x8d\xdf\xa1\xed\xe8.\n\xf3\x9d\x085\xc1\xc3\xe7C\x0c\x9e\xf8R\x0c\
Dd\x00G\x07\xfd\xe7\xcf\x1d\xdc\x9d6-\x1c\x12\x14\xba\x8a\xf05\xd51o\xf8\xd1\
\x9ds\x1c>\xd0\x88,\xdb\x18\x19\x9d\xa8\xaeSY\xe1\xe6\xe5\xab\xcf\x16\xab\
\xbcV\x00j[\xd4\xf6\xc0Z\x18ER\x88\xa8:\xc5\x05:\xaa\x91CA\xa1\x02X,E\xe6H[)\
"\x9aN\xd24\xb1d\x9b\xf26:\x97\xa7\xe9U\x00V\xb5\xb4kl\xe63q\xcd\xc0]\x94\
\x8f\xd7\xb3\x95\\U%GU\x01\xc8X\x16f*\xc5\xb7\xc5U\x82Q\r\x97\xcbI\\f;\xac?\
\xd2e\xf9\x9a\xec\x8c:\x1b\x9c\xc5R\x85P\xed\x12;"\n\xb0\xedM\x12R\xeezR6\
\x92#\xe9\xcd\x934a\xb1\x96\x89Y\x8b/n\xf6N\x01\xfc\x04\xcd\xa1\x0c<$\xbd\
\xd7\x7f\x00\x00\x00\x00IEND\xaeB`\x82\xc8\xd03+' )

def getUser16Bitmap():
    return BitmapFromImage(getUser16Image())

def getUser16Image():
    stream = cStringIO.StringIO(getUser16Data())
    return ImageFromStream(stream)

#----------------------------------------------------------------------
def getUser32Data():
    return zlib.decompress(
'x\xda\x01\x14\x07\xeb\xf8\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00 \
\x00\x00\x00 \x08\x06\x00\x00\x00szz\xf4\x00\x00\x00\x04sBIT\x08\x08\x08\x08\
|\x08d\x88\x00\x00\x06\xcbIDATX\x85\xe5\x96il\\W\x15\xc7\x7f\xf7-3c{\xc6v\
\xbc\xc4\xf1\x12/MLZ\x93\xc5Y!\xabD\xda\xa6AP\xaaT\x89X\x12\x90\xf2\x05)\x88\
T\xa4\x12E \xf1\x05\xb5H,a\x91\x8a\x80\xc2\x97\xa8\x15\x08\xda \x15\x01Q\xb6\
6$mJI\xe2\x14\x9a\xc6M\xec\x18\xdb\x89\xed\xc4\xb1=Nf<3\xef\xdd\x8d\x0f\xcf-\
M\xda`\x0b\x07\xf1\x81#]\xe9=\xdds\xfe\xe7w\xef\xb9\xef\xbc\x0b\xff\xef&\xfe\
\x83\x18\xef\xf3\xad|m}#;\x8a|\xee\x05\xc8K\xbaN\xf4\xf3\xabg\xbb\xf86\x10\
\xde]\xc4\xf7\xd8\xea&\x7f\xe9o\x1fM\x8d\x9d\xfe\xee\x16;~\xfa7\xd6\xa6\xdf\
\xb6\xf6\xc6\x05;\xde\xf1\x82=\xb3w\xab=\xf0\xb9\xd4\xf8\xea\x06o\xe5\x7f%\
\xf9\xba\xc6X\xdb\x9f\xb6\xcf\xb2C\x87\xf6Z;\xf2\x86\xb5#\xe7\xadM_\xb2v\xbc\
\xc7\xda\xd1\x0b\xd6\x8e\x9d\xb3\xd7^\xfe\x89=\xb0\xa3\xc2\xaei\xf2\xdb\xa7\
\xab\xebN\xd7\xf1\xfb\x0f\x94\xfc}\xe5\xf6\xaf$k\x97l\x88\xc2\xfc$\xc4\x92\
\xe0%\x00\x0b\xb2@IE5\xc9\x9a:\xea\x86^\xdb\xfa|g\xf8\x83h\xe2.\x00<\xb6*\
\xf9\xc4\xbau\xcb\xb7\xdc\xb7\xf93`\\\xf0\x8b\xc1/\x01?\x05n\x02\x8c\x04\x13\
\x80\xcc\x93\xac\x9eM~\xb8\xaf\xb8(;l^\x1f\x08\xff<\x95\xb63\x1d\x80\x87\xe6\
\xfbO|x\xe3\xc3\x10\x14xwQ\xd6\x82\xd5`\x14X3\xf9n!,\xd0\xb6\xf1\x11\x1e\x9a\
\xe7=>\x1d\xed)\x01\x96\xd4\xf9\xed\x89YU\x95\xc9\xaaj0:\x1aZ\x82\x0e@fAf\
\xa2g#A+\xd0\x9a\xe2\xcaJ\x8a\xabkK\xd7\xb7x\xabf\x0c0\xaf\xccY]Q\xdf\x04*\
\x9c\xdc\xea\x10t\x01d\x0e\xc2,\x04\x19\x90\x13\xa0\n`\xc3h^\x06T7\xb6P\x15\
\xf7\xd7\xcc\x18\xa0\xb5\xcak.*\xad\x04\x15\x80\x0e\xa3D*\x1f%\r3\x10\xde\
\x8c@d.\x9a\xd3!\xe8\x90X\xb2\x9c\x95\r~\xe3T\xfa\xdeT\x0e\xa9\x98\x1b\x17B\
\xa0\xa5\xc2\x11y\x84\xe3\x81p\xa2\xbak?r2**C\x98\x03\x95\x03\x19\xe0\x08\
\x17clb\xc6\x00C\x19\x9d\x91\x85<&\xd4\x08\x11 \x84\x03\xc6FI\x1d\x17\x10\
\x93g#\x04\x9d\xc7\xca\x02*\xd4\x84\x85<\xd9\xd0dg\x0c0\x9c\xd3\x17\xb2c\xd7\
QRa\xd1x\x80\xf0\r\xc2J\xc0\x8d\x8ah\x0c\x18\x89U\x05T\x10\xa2\x95%;z\x9d\
\xae1\xdb5c\x80\xb3\x83\x85c\xe9\xa1>t\xa81\x06\xac\x15x\xc6 \xdc\x10\xe1L\
\x1e!k1Z\xa3\xa5B\x86\x1a\xa1\x05\xa3\x03\xff\xa0oD\x1f\x9d1@\xf7\x18W&&r\
\xe7\xaf\xf6u\xb5U74c\x8d\xc5h\x07\xc7\xf5p\x1c\x01X\xac\xb5\x18m\xd1Jc\xa4f\
t\xe02\x13\xd9L\xf7\xe9\xe1\xa0g*\xfdiuB\x8d\xb8:\xdfO\x7f\xbav\xdeb\x8c\xd6\
Xc\xb1\xda`\xb4B+\x8b\x96\x1a\x19*t\xa8\xb0F\xf0\xd6\xf1\x17\xd9\xf7\xd7\xf1\
\xdd\xe7\xaf\xcb7\xef\n@\xe7u\xd5y\x7f=\x1b\x90\xb9\x96\x8a9\xcd\x18)\xd1\
\xda\xbcg\xd5Qr\xac\xa0\xbb\xe3\x15z\xde\xbe\xf4\xeaS\xaf\xde\xdc3\x1d\xedi\
\x01\xc4\xdah{}^\xb8\xe8C\xc3C\xed^6OyM\x13Vi\xb4\xd6he0\xca`\rt\x9f>\xc6\
\xd9\x8b\'y\xb24\x7fx<c\xdf \xcd\x8d\xa9\xb4\xff\xed\x85\xa4x-\x1f\x8f/\xe1\
\xa9TMl\xa9/J\xf8\xce\xb2g\xb0\x07\x7f\x84{\xfd<\xf5\xad\xcbH\x96\xcf\x06!\
\xc8\xa6\xaf1\xd4\xfd7\xc2Y\xf3\x88=\xf2Uv\xbe\xb4\x95T\x89O\xe6\x9a<\x92=\
\xc2\xe3\xf2\x02w,\xc5\x07\x03\xcc\xa1\xbab\x1b\xfb+\xeb\x8a\xd7?\xfc\xb1\
\xd5\xac]\xba\x90\x9d_\xff1\xdd\xdf\xbcJ\xc7\x99\x0bd{;\xb0=\'\xb0\xe3\x97#\
\x91\xf2\xb9\xd0\xb2\x8e\xea{\xd7R\xd6\xe8\xf2\xa9_\xae\xe2\x87\xdf\xf82\x07\
O\x9c\xe2\xc0\xc9Sd\xbb\xf5/\xc6\x9f\xb3_\x9c\x16\x80\xbf\x80E\xa5\xdb8\xb5\
\xf9#\xcb\xe2\x9b7\xac\xc0\xb1>\xbe\x1b\xe7\x0f\xc7Nr\xa5+\xe0\xe8\x9e\x0ez{\
\xfb\xe9\x1f\x18$\x93\x8d\xfaLii\x8a{\x1a\x1b\xa9\xaf\xafe\xf1\xb7\x1a\xd8\
\xb4q1\xab\xda\xefC\x9b\x02\x05\x15\xb0\xefw\x87y\xebb\x7f\xe7\xc8\xf7X\x0e\
\xe4\xef\x0cPI]\xf5.\xfa\xbe\xf0\x89\xfb\xbdE\x0b\x9a\x11\xb8x$\xf0\xdd8%\
\x89\x14O>\xf3s\xe2a\x15\xfbw\x1d\xa5\xa2\xa8\xf2\x96\xd0\xfe\xb1^>\xf9\xf4:\
\x1a\x1aK\xd9\xbd\xfd\xb3d\xf2\x19\x94) M\x01\xc7\x83\xfd\x07_\xe1\xf8\xf1\
\xce3\xe9\xa7YqG\x80\xca\xc78\xbc\xe9\xc1\xf6\x076\xacX\x88\xebz\xc4\xbd8\
\x9e\x13\xc7w\x12\xf8N\x9cTQ\x19\xcf\x1f>\xc4s\x07\x0e\xb1\xb4\xbe\x8d\xf6\
\xb9\xabPFq\xaa\xf7$\x17Gz\xd8\xf5\xe8\x166\xad^\xc3\xcd\xfc\r\x94\t\x90\xa6\
\x80\xb4\x01\x81\x0c\x10\x0e\xfc\xec\xd7\x7f\xe4\xe2\xefG\xbe\x94=\xc2O\xdf\
\x0fPAC\xfdn\xef\xf2\x9e\x9d[p\x85C"\x16#\xee\xc7\xf0\xdd8\x1eq<7\x8e\xe7\
\xc4(\xf2\x8b\xf1D\x8cs=]\\\x19\xbe\x8a\x10\x82\xa69u\xb4\xb5\xb4\x12\xa8\
\x1c\x05\x95G\x99\xe0\xdd\x11\x9a\x90 \x0c\x08\x94\xe2\xf2\xc05\xf6\xbd\xf0r\
\xef\xe8^Z\xdeI\xfb\xafN\xb8\x80\x1d\xadMu\x14\xc2\x00\xdf\xf1\x10"b\xb3\x80\
u\x0c\xc6h\x8c\x95h\x13\xe2\x08\x8f\x96\xb95\xcco\xaa\xc3b1\xc60\x9e\x1fF[\
\x8d\x9e\xf4\xd1V"uH\xa0$\x81\x8cFUu\x19e\x15E\xcd\xa3u\xf9\xa5\x0cr\xf6\x16\
\x00\xe7\x1e6\xd5\xce\xa9 \x97\x0f\x88\xf9\x1a\xad\rZk\x941\xf8\xae\xc4s\x03\
<\xc7\xc7u\x1c\x04.\x8ex\xa7\x85D\xed\xd8X\x83\xb1\nc\r\xca(\x94VH\xa5\x08\
\x95$\x08#\x00\xa55-\r5\xf44\xf5n{\x1f\x80?\x8b\x15\xc9\x92\x18\xd9B\x9e\x98\
\xf4\x89\xc7\x15WG\xd3\x04\x85\x90\xf9\xcd\xf5\xb8\xae\x8b\xe7\x08\\\xd7\xc3\
q\x1c\x1c\x88~\xcd\x18\xac\x15\x18\x1b\xed\x846\n\xa5\r\xda\x18.\xf5\r\xe1z\
\x0e\xe5\xa5\xc5\x04J"\xb5\xa4\xaa2\x89\xd3\xc2F\xf3\xda\xed%\x80\x94\x16\
\x86\\\x90G\xba\nM\x8c7;{p\x84KMM9 \xf0\x1c7J\xee\x08\x10\xe0L^\xa8\x0c\x06\
\xb4\xc5\x00\xdaD;g\x85\xa5\xbbo\x90PI\x96\xb7\xcf\xa7\x10\x84H-\xf1\x13\x1e\
\xb1J\x16\x16n?\x03\xae\xe5//\x1d?\xf7\xd1\xb2T\x82\xe2\xe2\x04\xa9d\x11\x03\
\xc3i\xeak+\xe8\x1b\x1c\xc6\x8fy\xc4\x1c\x97DQ\x0c\x81C<\xee\xdf\xf2\x19Zk\t\
B\x89\xd6\x9a \x0c\x91\xa1F\xa3\x19\x1e\xbd\xc1\xf9\xae~2\xb9<\x13\x13ynd\
\xf2\x98,\'?\xf03\xa4\x9c\xc5\xd4\xb3\x04\x9f\x16QO\x1d\x82\xd9VQ\x19o\xa5\
\xdc\x1aJ\xad\xa5H@)\xe0X\x88s\x9b\t\x81\xc6\x12\x027q\xc8\xea4i\x93f\x14\
\x18\xb4\xe3\\a\x8cn\xae\xd1A\x9as\xb7\xc7\xfe\xcf\xec\x9f\x1f\xf9\x8e\xc5\
\xde\x02\xa0w\x00\x00\x00\x00IEND\xaeB`\x82i9j\x97' )

def getUser32Bitmap():
    return BitmapFromImage(getUser32Image())

def getUser32Image():
    stream = cStringIO.StringIO(getUser32Data())
    return ImageFromStream(stream)

