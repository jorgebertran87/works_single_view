# Works Single View

Works Single View is an application that aggregates and reconciles	data from multiple sources to create a single view of a musical	work

## Installation

Use Docker.

```bash
# It takes about 15 minutes the first time, 
# because of rest-pandas package
 docker-compose build 
```

```bash
 docker-compose up -d
```

## Usage

### API

- Works list

```
http://localhost:8990/works/
```

- Work detail

```
http://localhost:8990/works/:iswc
```

- Export to csv

```
http://localhost:8990/works/export/[filename.csv]
```

### Tests

```bash
 docker-compose run --rm web python3 -m unittest discover tests -p "*.py"
```
### CLI

- Load works from csv

```bash
docker-compose run --rm web python3 works_single_view.py --cmd load_works_from_csv --csv tests/infrastructure/cli/works_metadata.csv
```

- Get loaded Works

```bash
docker-compose run --rm web python3 works_single_view.py --cmd get_works
```

## Design patterns and architecture

-- The framework and the database are completely decoupled from code

- Hexagonal architecture, TDD, DDD, Value-Object pattern, Repository pattern, SOLID principles, CQRS