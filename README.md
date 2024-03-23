# Sistema de fila
Este é um exemplo simples de um sistema de fila que visa o processamento de resultados de apostas realizadas. Utilizamos o Celery + RabbitMQ para fila e processamento, além do Flower para um  monitoramento adequado da fila.

## Guia de uso
1. Criar o ambiente virtual python utilizando o comando `python -m venv env`, ative usando o `active.bat` em env/Scripts
2. Instalar o Celery utilizando `pip install celery`
3. Criar uma task (para exemplo, temos o arquivo task.py)
4. Instalar o [docker](https://www.docker.com/get-started/)
5. Caso deseje, configure o docker-compose.yml
6. Subir o container utilizando o comando `docker compose up`
7. Iniciar um worker, utilizando o comando `celery -A task worker -l info --pool=solo`
8. Instalar o flower para monitorar melhor a execução do sistema de fila, o comando de instalação é `pip install flower`
9. Rodar o flower em conjunto com o celery, utilizando o comando `celery -A task flower --address=127.0.0.6 --port=5566`, após isso temos acesso a interface web do flower na url `http://127.0.0.6:5566/tasks`
10. Adicionar itens a fila, utilizando o comando `python app.py`

Agora você já pode acompanhar o processamento na interface web do flower.