# functions-from-zero
Creating function from zero

[![LangServe test deploy](https://github.com/niikun/functions-from-zero/actions/workflows/main.yml/badge.svg)](https://github.com/niikun/functions-from-zero/actions/workflows/main.yml)

### To call Microservice

```bash
curl -X 'POST' \
  'https://obscure-parakeet-66747977x6r25rp4-8000.app.github.dev/wiki' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "word": "OpenAI"
}'
```

### Build container

`docker build .`
`docker image ls`


