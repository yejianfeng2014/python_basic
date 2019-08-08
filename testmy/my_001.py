import sys

def start(*args, **kwargs):
    # if self.verbose >= 1:
    #     print('ready to starting ......');
    # check for a pid file to see if the daemon already runs
    pid = 123

    if pid:
        msg = 'pid file %s already exists, is it already running?\n'
        # sys.stderr.write(msg % self.pidfile);
        sys.exit(1);
        return 1
    # start the daemon
    # self.daemonize();
    # self.run(*args, **kwargs);

    print(123)



start()