#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Requirements:

    Console app for walk journey simulation in different environments.
    Simulate journey and calculate running time.
    Inputs: name, path length and environment type

    Stage 2:
    Simulate run journey

    Stage 3:
    Simulate swimm journey


Q: Console color output?
    YAGNI

Q: Different kinds of movements (bike, fly)?
A: For future definitely
    YAGNI

Q: How about weight input?
A: If there is success after third project release, definitely
    YAGNI

Q: History of running tests?
A: YGNI
    log file vs pickle vs db
    Which one to choose right now :) pickle/db is YAGNI

    YGNI, Choose db if results needs to searched, further analyzed etc.

Q: Reports?
A: Email reports
    plain txt vs html vs web app
    simple cronjob or manual send of plain txt is good enough
    -> html/web is YAGNI

    YGNI html for better visuals
    YGNI web if reports needs to be full time accessible, searched, ...

"""

import time
import sys


class EnvTypeError(Exception):  # KISS
    pass


class Movement:
    """Base movement class.
    """
    ENV_TYPES = {
        1: '-',
        2: '~',
        3: 'w',
    }
    SPEED = 0

    def __init__(self, name, path, env_type):
        """Init"""
        self.name = name
        self.path = path
        self.env_type = env_type
        if self.env_type not in self.ENV_TYPES.keys():
            # Custom Exception ->  KISS
            raise EnvTypeError("env_type arg '{}' not in {}.".format(
                self.env_type, self.ENV_TYPES.keys()))
        self._runtime = 0

    def __str__(self):  # KISS
        return "<{} #{}>".format(self.__class__.__name__, self.name)

    def run(self):
        """Moving simulation.
        """
        sim_time = (self.env_type / 16.0) * self.SPEED
        for s in range(self.path):
            self._runtime += sim_time
            time.sleep(sim_time)
            sys.stdout.write(str(self.ENV_TYPES.get(self.env_type)))
            sys.stdout.flush()
        print()
        # self.report()  # KISS

    def report(self):
        # ...
        # Some serious calc
        # ...
        if self._runtime <= 0:  # KISS
            raise Exception(
                "Please do the simulation first by running run method.")

        result = "{}\tpath={}\truntime={}\tspeed={}".format(
            self, self.path, round(self._runtime, 3),
            round(self.path / self._runtime, 3))

        # Print and log
        print(result)
        self.log_to_file(result)  # KISS (perhaps oversimplified)

        # Reset runtime
        self._runtime = 0

    def log_to_file(self, result):  # KISS (perhaps oversimplified)
        """Log run result to file.

        :param str result: report output
        """
        with open("log.txt", "a") as f:
            f.write("{}\n{}\n".format(
                time.strftime("%Y-%d-%m %H:%M:%S"), result))

    def run_and_report(self):  # KISS
        """Do the run and report afterwards.
        """
        self.run()
        self.report()


class Walk(Movement):
    """Walk class.
    """
    SPEED = 1


class Swimm(Movement):
    """Swimm class.
    """
    SPEED = 1.5


class Run(Movement):
    """Run class.
    """
    SPEED = 0.5


if __name__ == '__main__':
    # != DRY Not needed here. Like in tests.
    w = Walk('A', 44, 1)
    w.run_and_report()  # KISS...
    w = Walk('B', 42, 2)
    w.run_and_report()
    w = Walk('C', 36, 3)
    w.run_and_report()
    r = Run('A', 44, 1)
    r.run_and_report()
    r = Run('B', 42, 2)
    r.run_and_report()
    r = Run('C', 36, 3)
    r.run_and_report()
    s = Swimm('A', 44, 1)
    s.run_and_report()
    s = Swimm('B', 42, 2)
    s.run_and_report()
    s = Swimm('C', 36, 3)
    s.run_and_report()
