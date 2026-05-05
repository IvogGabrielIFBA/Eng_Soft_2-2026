# Planejamento da Interface de Linha de Comando (CLI)

**Responsável:** Thiago (Engenheiro de CLI)

## Objetivo
O objetivo é desenvolver a camada de interação via terminal para o programa Mida, que é uma aplicação desktop de Conversão de Arquivos, garantindo o processamento seguro de argumentos e o feedback de execução em tempo real.

## Ferramentas Utilizadas
* **Typer:** Biblioteca principal para a construção da interface, fará a definição de comandos, subcomandos e validação rigorosa de tipos de entrada (Type Hints).
* **Rich:** Será utilizada para a formatação de saída no console, incluindo o uso de tabelas de status e barras de progresso para monitoramento de várias conversões feitas ao mesmo tempo.

## Requisitos de Implementação
* **Desacoplamento:** A CLI irá atuar como um cliente independente, consumindo a API do Core sem interferir nas regras de negócio internas.
* **Parsing de Argumentos:** Implementação de flags de configuração e tratamento de erros amigáveis para entradas inválidas.
* **Feedback de Execução:** Emissão de eventos de progresso que permitirão ao usuário acompanhar o tempo estimado e a conclusão das tarefas diretamente no terminal.

## Padrões de Comandos Planejados
* Comando para conversão individual de arquivos com definição de origem e destino.
* Comando para processamento em lote (batch) de diretórios inteiros.
* Flag para forçar sobrescrita de arquivos existentes, respeitando as Regras de Negócio do projeto.