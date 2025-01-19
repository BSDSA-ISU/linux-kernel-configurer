from Alimod.troysrc import MenuconfigPacman as pacman
import os
import click

@click.command()
@click.option("--choice", type=click.Choice(["manual", "Default config of the kernel booted on", "config based on modules/feature turned on"], case_sensitive=False))
def choose(choice):
    click.echo(f"You selected: {choice}")

choose()
pacman()