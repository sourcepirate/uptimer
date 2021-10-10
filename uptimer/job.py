from typing import List

from uptimer.memory import InmemoryDB
from uptimer.uptimer import access_domains


def run_checker_job(db: InmemoryDB, domains: List[str]):

    responses = access_domains(domains)
    for response in responses:
        db.put(response["domain"], response["current_time"], response)
