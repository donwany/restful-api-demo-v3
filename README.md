### Usage:
```shell
curl --location --request POST '0.0.0.0:5000/api/v1.0/books' \
--header 'Content-Type: application/json' \
--data-raw '{
    "name": "Return Trump 2024",
    "isbn": "202583438-ISBN-2025",
    "page": 5,
    "author": "Donald Trump",
    "Country": "USA",
    "year_published": 2019,
    "State": "NYC",
    "Edition": 2
}'
```
```shell
curl --location --request GET '0.0.0.0:5000/api/v1.0/books/63ca280beb5a997069dd203b'
```

```shell
curl --location --request GET '0.0.0.0:5000/api/v1.0/books'
```
```shell
curl --location --request PUT '0.0.0.0:5000/api/v1.0/books/63ca1f04f1dcf518da9ccdef' \
--header 'Content-Type: application/json' \
--data-raw '{
    "name": "Introduction to Research",
    "isbn": "202083438-ISBN-2023"
}'
```
```shell
curl --location --request DELETE '0.0.0.0:5000/api/v1.0/books/63ca2227b1acf0b870776635'
```
```shell

```