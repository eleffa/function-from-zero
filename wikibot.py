import click
from mylib.bot import scrape
#import wikipedia

#@click.command()
#@click.option("--name", prompt="Wikipedia page to scrape",help="Web page we want to scrape")
#def scrape(name='Microsoft', length=1):
#    result = wikipedia.summary(name, sentences=length)
#    click.echo(click.style(f"{result}:", fg="blue"))


@click.command()
@click.option("--name", help="Web page we want to scrape")
def cli(name):
    result = scrape(name)
    click.echo(click.style(f"{result}:", fg="blue"))


if __name__ == "__main__":
    cli()
#    scrape()