# pyconkr2021-APITest

[API Response 효율적으로 테스트하기](https://www.youtube.com/watch?v=mTmlhcYvwwc&feature=youtu.be) 발표 예시 프로젝트입니다. 

[Schema](https://github.com/keleshev/schema)와 [pytest-lazy-fixture](https://github.com/TvoroG/pytest-lazy-fixture)의 사용법을 더 자세하게 알고 싶다면, [다음 글](https://www.qu3vipon.com/32c46e43-1bab-4be0-8fdc-1e67c0b12dc9)을 참고해주세요. 

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
