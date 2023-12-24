import argparse

def initialize_parser():
    parser = argparse.ArgumentParser(description="Process some inputs.")
    # log directory
    parser.add_argument("--log-dir", type=str, required=False, default="./execsentry/", help="Where to log the output of the running command")
    # log to stdout
    parser.add_argument("--log-to-stdout", type=bool, required=False, default=True, help="Whether to log the output of the running command to stdout")
    # attach log in email
    parser.add_argument("--attach-log-to-email", type=bool, required=False, default=False, help="Whether to attach the log file in the notification email")
    # save environment info
    parser.add_argument("--log-env-info", type=bool, required=False, default=True, help="Whether to log the info of the running environment")
    # save git version
    parser.add_argument("--log-git-version", type=bool, required=False, default=True, help="Whether to log the version of the github repository")
    # list all running processes
    parser.add_argument("--list-process", type=bool, required=False, default=False, help="Whether to list all processes")
    # wait until a precondition is satisfied
    parser.add_argument("--pre-command", type=str, required=False, default="true", help="In this flag, the user need to provide a user-defined pre-command to check whether the user-defined precondition is satisfied (If the pre-command is satisfied, it should return 0). \nIf satisfied, start the given command; otherwise, wait until the pre-command is satisfied. \nThe pre-command is tested in every 5 minutes. The default pre-command is 'true', it always return 0.")
    # monitor cpu usage
    parser.add_argument("--monitor-cpu", type=bool, required=False, default=False, help="Whether to monitor the cpu usage of the command")
    # monitor memory usage
    parser.add_argument("--monitor-memory", type=bool, required=False, default=False, help="Whether to monitor the memory usage of the command")
    return parser