import click
from core.infrastructure.cli.load_works_from_csv import LoadWorksFromCSV
from tests.stubs.work_repository_stub import WorkRepositoryStub

@click.command()
@click.option('--cmd', help='The command to be executed')
@click.option('--csv', help='The csv path containing works')
def launcher(cmd: str, csv: str):
	if cmd == 'load_works_from_csv':
		print('Loading works from csv...')
		
		workRepositoryStub = WorkRepositoryStub()

		command = LoadWorksFromCSV(csv, workRepositoryStub)
		command.execute()

		print(str(len(workRepositoryStub.all())) + ' work(s) loaded!')

if __name__ == '__main__':
    launcher()
