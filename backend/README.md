# 🗄️ Backend Principal (Núcleo)

> A documentação principal de como inicializar o serviço em dev e produção encontra-se no [README master](../README.md).

Este diretório contém a base principal da API em **Django Rest Framework**, projetada para ser completamente isolada do Frontend, comunicando-se unicamente via JSON/JWT em ambiente conteinerizado.

## Detalhes deste escopo
- As configurações dividem-se em `nucleo.settings.dev`/`base`/`prod`.
- O app `core` cuida de endpoints isolados.
- O app `users` traz base model para o Unfold Admin.