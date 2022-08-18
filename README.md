# anon-ftp-scanner
Anonymous FTP scanner by ip address, using the python ftplib library.

program logs in anonymously if successful displays contents of the root directory.

    few sites to test against:
        ftp.pureftpd.org
        ftp.gnu.org
        ftp.vim.org
        ftp.slackware.com


Using the ftplib

firstly instantiating the ftplib library by setting the ftplib.FTP(IP) to a variable for use.

use the login method to login to the ftp service with credentials, if no credentials use "anonymous" and the username will be aanonymous and the password will be "anonymous@" as shown in the ftplib.py file.
if login is not successful an error will be raised hence why the try except is used.

when you are done with the ftp connection do not forget to close the connection by using the quit() method.

    Copied from ftplib.py file for refference to ftplib.FTP method


        To create a connection, call the class using these arguments:
            host, user, passwd, acct, timeout

        The first four arguments are all strings, and have default value ''.
        timeout must be numeric and defaults to None if not passed,
        meaning that no timeout will be set on any ftp socket(s)
        If a timeout is passed, then this is now the default timeout for all ftp
        socket operations for this instance.

