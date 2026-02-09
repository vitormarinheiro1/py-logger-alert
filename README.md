# py-logger-alert 🚀

Uma biblioteca leve e eficiente para monitoramento de scripts e bots em Python.

O **py-logger-alert** integra o sistema de `logging` padrão do Python com o **Telegram**, permitindo receber **alertas de erros críticos em tempo real**, enquanto mantém um **histórico completo de logs em arquivos locais**.

Ideal para quem roda bots, automações, robôs de trading ou scripts agendados e precisa saber imediatamente quando algo dá errado.

---

## ✨ Principais Funcionalidades

- 📢 **Notificações em Tempo Real**  
  Envia logs de nível `ERROR` e `CRITICAL` diretamente para o Telegram.

- 🗂 **Registro Local Automático**  
  Salva logs (`INFO`, `WARNING`, `ERROR`, etc.) em arquivos `.log`.

- ⚙️ **Configuração Simplificada**  
  Suporte nativo a variáveis de ambiente via arquivo `.env`.

- 🧾 **Formatação Amigável**  
  Mensagens formatadas em blocos de código, facilitando leitura de tracebacks.

- 🔐 **Segurança**  
  Truncamento automático de mensagens longas para respeitar os limites da API do Telegram.

---

## 🛠 Instalação

```bash
pip install py-logger-alert
```

---

## ⚙️ Configuração do Telegram

Crie um arquivo `.env` na raiz do projeto:

```env
TELEGRAM_TOKEN=seu_token_aqui
TELEGRAM_CHAT_ID=seu_chat_id_aqui
```

---

## 🚀 Como Usar

```python
from py_logger_alert import setup_monitoring
import logging

setup_monitoring(
    nome_robo="Robô Trader v1",
    log_filename="logs_bot"
)

logging.info("Sistema iniciado com sucesso.")

try:
    10 / 0
except Exception as e:
    logging.error(f"Erro crítico detectado: {e}", exc_info=True)
```

---

## 📖 Função Principal

### setup_monitoring(nome_robo, log_filename)

Configura o ambiente global de logging da aplicação.

---

## 📜 Licença

MIT License

---

## 👨‍💻 Autor

Vitor Marinheiro  
https://github.com/vitormarinheiro1  
https://github.com/vitormarinheiro1/py-logger-alert
