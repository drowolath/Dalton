#!/usr/bin/env python
# -*- coding: utf-8 -*-

from libdalton import analyze
from libdalton import fileio
from libdalton import optimize
from libdalton import simulate

import click


@click.command()
@click.option('--ana')
@click.option('--mc')
@click.option('--md')
@click.option('--opt')
def cmd(ana, mc, md, opt):
    """CLI for libdalton"""
    input_file_name = fileio.validate_input()
    # default type of options is string
    # they not exclusive though
    if ana:
        analysis = analyze.Analysis(input_file_name)
        analysis.run()
    elif mc:
        simulation = simulate.MonteCarlo(input_file_name)
        simulation.run()
    elif md:
        simulation = simulate.MolecularDynamics(input_file_name)
        simulation.run()
    elif opt:
        optimization = optimize.Optimization(input_file_name)
        optimization.optimize()


if __name__ = '__main__':
    cmd.run()

# EOF
