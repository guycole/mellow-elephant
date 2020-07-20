#
# Title:pid_lock.py
# Description:ensure only a single instance runs
# Development Environment:OS X 10.15.5/Python 3.7.6
# Author:G.S. Cole (guycole at gmail dot com)
#
import os


class PidLock:
    def lock_test(self, file_name: str) -> bool:
        """
        return True if active lock noted
        """
        target_pid = os.getpid()

        try:
            infile = open(file_name, "r")
            target_pid = int(infile.readline())
            infile.close()
        except IOError:
            return False

        command = "/bin/ps -p %d" % target_pid
        temp = os.popen(command).readlines()
        # returns one or two lines, w/first line as header
        # ['  PID TTY           TIME CMD\n', '52645 ttys000    0:00.04 python pid_lock.py\n']

        if len(temp) > 1:
            return True

        return False

    def write_lock(self, file_name: str) -> bool:
        """
        write a PID lock file
        """
        outfile = open(file_name, "w")
        outfile.write("%d\n" % (os.getpid()))
        outfile.close()


if __name__ == "__main__":
    print("start")

    pid_lock = PidLock()

    flag = pid_lock.lock_test("/tmp/target")

    if flag:
        print("pidlock test true")
    else:
        print("pidlock test false, now write lock")
        pid_lock.write_lock("/tmp/target")

    flag = pid_lock.lock_test("/tmp/target")
    print("pidlock test now %s" % flag)

    print("stop")

# ;;; Local Variables: ***
# ;;; mode:python ***
# ;;; End: ***
