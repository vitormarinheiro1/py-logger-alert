# Py-Logger-Alert 🤖

O **Py-Logger-Alert** é uma biblioteca leve e eficiente para monitoramento de robôs de automação em Python.  
Ela se integra ao módulo nativo `logging` para salvar logs em arquivos locais e enviar notificações críticas automaticamente para o **Telegram**.

Ideal para desenvolvedores que gerenciam múltiplos robôs e precisam de **avisos em tempo real** quando algo falha.

---

## ✨ Funcionalidades

- ⚡ **Configuração Zero**: Configure arquivos de log e alertas em uma única linha de código.
- 🧩 **Integração Nativa**: Funciona com o `logging` padrão do Python.
- 🔐 **Segurança com `.env`**: Protege seu Token e Chat ID através de variáveis de ambiente.
- 🗂️ **Logs Flexíveis**: Gera arquivos `.log` automaticamente com o nome que você escolher.

---

## 🚀 Como Instalar

Instale via **pip**:

```bash
pip install py-logger-alert
```

---

## 🛠️ Configuração Inicial

Antes de rodar o seu robô, configure suas credenciais do Telegram.

1. Crie um arquivo chamado `.env` na raiz do seu projeto.
2. Adicione seu Token do BotFather e seu Chat ID:

```plaintext
TELEGRAM_TOKEN=seu_token_aqui
TELEGRAM_CHAT_ID=seu_chat_id_aqui
```

> 💡 **Dica**: Adicione o arquivo `.env` ao seu `.gitignore` para manter suas chaves seguras!

---

## 💻 Exemplo de Uso

```python
import logging
from py_logger_alert import setup_monitoring

# Inicializa o monitoramento (cria 'meu_robo.log' e ativa o Telegram)
setup_monitoring("meu_robo")

# Logs de INFO e DEBUG vão apenas para o arquivo .log
logging.info("O robô iniciou a tarefa com sucesso.")

try:
    # Simulando uma falha técnica
    resultado = 10 / 0
except Exception as e:
    # Erros de nível ERROR ou CRITICAL são enviados para o Telegram automaticamente
    logging.error(f"Falha detectada: {e}", exc_info=True)
```

---

## 📁 Estrutura de Arquivos Gerada

Ao rodar o script, a biblioteca garantirá que seus logs sejam organizados:

```plaintext
projeto/
├── .env
├── meu_robo.log    <-- Gerado automaticamente
└── seu_script.py
```

---

## 📄 Licença

Distribuído sob a licença **MIT**.  
Veja o arquivo [LICENSE](LICENSE) para mais informações.
