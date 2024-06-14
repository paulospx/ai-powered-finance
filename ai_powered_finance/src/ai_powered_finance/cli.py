"""Console script for ai_powered_finance."""
import ai_powered_finance

import typer
from rich.console import Console

app = typer.Typer()
console = Console()


@app.command()
def main():
    """Console script for ai_powered_finance."""
    console.print("Replace this message by putting your code into "
               "ai_powered_finance.cli.main")
    console.print("See Typer documentation at https://typer.tiangolo.com/")
    


if __name__ == "__main__":
    app()
