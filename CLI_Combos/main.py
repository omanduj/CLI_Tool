import typer
from logic import get_pins

app = typer.Typer()


@app.command()
def main(pin_numbers: str):
    """Purpose: To serve as function to be called as CLI, displaying all possible number combinations of
              an inputted pin number
    Parameters: pin_numbers = A string of numbers
    Return Value: results = Output of all possible combinations sorted in ascending order
    """
    results = []

    if len(pin_numbers) != 4:
        print("Error: Incorrect Amount of Pin Numbers")
        return

    output = get_pins(f"{pin_numbers}")
    sorted_values = sorted(output)

    for grouping in sorted_values:
        results.append("".join(grouping))
        print("".join(grouping))


if __name__ == "__main__":
    app()
