# pyconkr2021-APITest

"API Response 효율적으로 테스트하기" 발표 예시 프로젝트입니다. 

[Schema](https://github.com/keleshev/schema)와 [pytest-lazy-fixture](https://github.com/TvoroG/pytest-lazy-fixture) 사용법을 정리한 글은 다음 링크를 통해 확인하실 수 있습니다. [👉 Link](https://www.qu3vipon.com/32c46e43-1bab-4be0-8fdc-1e67c0b12dc9#b0e4ac60-8816-4153-b60f-783d10925f85)

<br>

## Requirements
- Python 3.8+
- Docker
- Docker Compose

<br>

## Run PyTest
Clone this repository:
```
git clone https://github.com/qu3vipon/pyconkr2021-APITest.git
```

<br>

Run PyTest:
```
docker-compose up --build --exit-code-from app
```
