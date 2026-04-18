# 📦 Aplicação Node Frontend (Next.js)

> A documentação principal de rodar serviços e o backend base encontra-se no [README master](../README.md).

Este projeto é desenvolvido integralmente em **Next.js** servindo como a _apresentação (View)_ da API em Django isolada.

O acesso primário de desenvolvimento nesta camada é efetuado por fora do ecossistema do `docker-compose`, exigindo que execute o `npm run dev` aqui dentro enquanto os serviços bases (back/db/cache) correm em paralelo pelo script de root `cli.ps1`.
