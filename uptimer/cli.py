"""Console script for uptimer."""
import sys
import click
import schedule
import time
from functools import partial
from uptimer.memory import InmemoryDB
from uptimer.job import run_checker_job
from uptimer.parser import parse_domain


db = InmemoryDB()


@click.command()
@click.argument("filename")
def main(filename):
    """Console script for uptimer."""
    click.echo(f"Parsing - {filename}")
    domains = parse_domain(filename)
    job_func = partial(run_checker_job, db, domains)
    schedule.every(10).seconds.do(job_func)
    schedule.every(3).seconds.do(db.flush)
    while True:
        schedule.run_pending()
        time.sleep(1)
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
