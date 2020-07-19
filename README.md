<img src="services/web/app/static/imgs/logos/200px.png" align="right" width="200px">

# Freezy

*it ain't easy being freezy*

A hastily written freezer log written hastily.

## Development notes.

### Setting environment variables

```bash
FREEZYUSER="Admin"
FREEZYTOKEN="7c67f2f5-c299-40ab-badc-7386a19290c0"
```

### Add test site

```bash
curl --location --request POST 'http://0.0.0.0:5000/storage/api/add/site' \
--header 'User-Token: "'"$FREEZYTOKEN"'"' \
--header 'Username: "'"$FREEZYUSER"'"' \
--header 'Content-Type: application/json' \
--data-raw '{
    "name": "Test Site"
}'
```

### Add test FCS

```bash
curl --location --request POST 'http://0.0.0.0:5000/storage/api/add/fcs' \
--header 'User-Token: "'"$FREEZYTOKEN"'"' \
--header 'Username: "'"$FREEZYUSER"'"' \
--header 'Content-Type: application/json' \
--data-raw '{
    "name": "Test Freezer",
    "type" : "FRE",
    "temperature" : "-80",
    "site_id": 1
}'
```

### Add test Shelf

```bash
curl --location --request POST 'http://0.0.0.0:5000/storage/api/add/shelf' \
--header 'User-Token: "'"$FREEZYTOKEN"'"' \
--header 'Username: "'"$FREEZYUSER"'"' \
--header 'Content-Type: application/json' \
--data-raw '{
    "name": "Test Shelf",
    "storage_id": 1
}'
```

### Add test Drawer

```bash
curl --location --request POST 'http://0.0.0.0:5000/storage/api/add/drawer' \
--header 'User-Token: "'"$FREEZYTOKEN"'"' \
--header 'Username: "'"$FREEZYUSER"'"' \
--header 'Content-Type: application/json' \
--data-raw '{
    "name": "Test Drawer",
    "shelf_id": 1,
    "size" : "L"
}'
```