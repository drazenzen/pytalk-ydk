#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Requirements:

    Console app for walk journey simulation in different environments.
    Simulate journey and calculate running time.
    Inputs: name, path length and environment type

    Stage 2:
    Simulate run journey


Q: Console color output?
    YAGNI

Q: Version of Python?
A: Python 3 only
    Refactor ~~ YAGNI (Python 2 references)

Q: Different kinds of movements (bike, swimm, fly)?
A: For future definitely
    YAGNI

Q: How about weight input?
A: If there is success after second project release, definitely
    YAGNI

Q: History of running tests?
A: YGNI
    log file vs pickle vs db
    Which one to choose right now :) pickle/db is YAGNI

Q: Reports?
A: Email reports
    plain txt vs html vs web app
    simple cronjob or manual send of plain txt is good enough
    -> html/web is YAGNI

"""

import time
import sys


class Movement:  # DRY
    """Base movement class.
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

    def run(self):  # DRY
        """Movement simulation.
        """
        sim_time = (self.env_type / 16.0) * self.SPEED
        for s in range(self.path):
            self._runtime += sim_time
            time.sleep(sim_time)
            sys.stdout.write(str(self.ENV_TYPES.get(self.env_type)))
            sys.stdout.flush()
        print()
        self.report()

    def report(self):  # DRY
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
        self._runtime = 0


class Walk(Movement):
    """Walk class.
    """
    SPEED = 1

    def __str__(self):
        return "<{} #{}>".format("Walk", self.name)


class Run(Movement):
    """Run class.
    """
    SPEED = 0.5

    def __str__(self):
        return "<{} #{}>".format("Run", self.name)


if __name__ == '__main__':
    # != DRY Not needed here. Like in tests.
    w = Walk('A', 44, 1)
    w.run()
    w = Walk('B', 42, 2)
    w.run()
    w = Walk('C', 36, 3)
    w.run()
    r = Run('A', 44, 1)
    r.run()
    r = Run('B', 42, 2)
    r.run()
    r = Run('C', 36, 3)
    r.run()
