import click
from termcolor import cprint
from imppkg.harmonic_mean import harmonic_mean


@click.command()
@click.argument("floats", nargs=-1)
@click.option("--fgcolor", "fgcolor", type=str, default="red")
@click.option("--bgcolor", "bgcolor", type=str, default="on_cyan")
@click.option("--attrs", "attrs", type=str, multiple=True)
def read_cl_arguments(floats: tuple[str], fgcolor: str, bgcolor: str, attrs: list[str]) -> None:
    cprint(harmonic_mean([float(n) for n in floats]), fgcolor, bgcolor, attrs=attrs)
