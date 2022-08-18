import ftplib

def loginWithAnon(host):
    try:
        ftp = ftplib.FTP(host)
        ftp.login('anonymous')
        print(f'\n-----Success-----\n\n{str(host)} logged in via FTP anonymously.\n\n')
        ftp.quit()
        return True
    except Exception:
        print(f'\n-----Failure-----\n\n{str(host)} not logged in via FTP anonymously.\n\n')
        return False

if __name__ == '__main__':
    print('Welcome to the anonymous FTP scanner.\n\n')
    hostname = input('Enter IP of host to scan: ')
    print(f"\nIP to be scanned is {hostname}\n")
    loginWithAnon(hostname)