#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Requirements:

    Console app for walk journey simulation in different environments.
    Simulate journey and calculate running time.
    Inputs: name, path length and environment type


Q: Console color output?
    YAGNI

Q: Version of Python?
A: It depends on which server it will run at client.
    Server environment is mixed (unix, microsoft) and
    run environment is not known in advance
    2 and 3
    YGNI

Q: Different kinds of movements (run, bike, swimm, fly)?
A: For future definitely
    YAGNI

Q: How about weight input?
A: If there is success after initial project release, definitely
    YAGNI

Q: History of running tests?
A: YGNI
    log file vs pickle vs db
    Which one to choose right now? pickle/db is YAGNI

Q: Reports?
A: Email reports
    plain txt vs html vs web app
    simple cronjob or manual send of plain txt is good enough
    -> html/web is YAGNI

"""

from __future__ import print_function  # YGNI
import time
import sys

# YGNI
# try:
#     from some.module import some.class    # py3
# except ImportError:
#     from some.module2 import some.class2  # py2


class Walk(object):
    """Walk class.
    """
    ENV_TYPES = {  # Special class?  YAGNI
        1: '-',
        2: '~',
        3: 'w',
    }

    def __init__(self, name, path, env_type):
        """Init"""
        self.name = name
        self.path = path
        self.env_type = env_type
        if self.env_type not in self.ENV_TYPES.keys():
            # Custom Exception?  YAGNI
            raise Exception("env_type arg '{}' not in {}.".format(
                self.env_type, self.ENV_TYPES.keys()))
        self._runtime = 0

    def __str__(self):
        return "<#{}>".format(self.name)

    def run(self):
        """Vehicle run simulation.
        """
        sim_time = self.env_type / 16.0
        for s in range(self.path):
            self._runtime += sim_time
            time.sleep(sim_time)
            sys.stdout.write(str(self.ENV_TYPES.get(self.env_type)))
            sys.stdout.flush()
        print()
        self.report()

    def report(self):
        # ...
        # Some serious calc
        # ...
        res = "{}\tpath={}\truntime={}\tspeed={}".format(
            self, self.path, round(self._runtime, 3),
            round(self.path / self._runtime, 3))
        # Print and log
        print(res)
        with open("log.txt", "a") as f:
            f.write("{}\n{}\n".format(time.strftime("%Y-%d-%m %H:%M:%S"), res))
        # Reset runtime
        self._runtime = 0


if __name__ == '__main__':
    v = Walk('A', 44, 1)
    v.run()
    v = Walk('B', 42, 2)
    v.run()
    v = Walk('C', 36, 3)
    v.run()

    # Tests? YAGNI or NOT?
