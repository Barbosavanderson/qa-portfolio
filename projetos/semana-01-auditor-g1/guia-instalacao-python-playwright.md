# Guia de Instalação — Python, Pytest e Playwright no Windows

## Pré-requisitos

Antes de instalar o Pytest e o Playwright, é necessário ter o **Python** instalado e configurado corretamente no sistema.

---

## 1. Instalar o Python

Abra o **Prompt de Comando (CMD)** como administrador e execute:

```cmd
winget install Python.Python.3.12
```

> O `winget` é o gerenciador de pacotes nativo do Windows 10/11. Caso ele pergunte sobre os termos de uso, digite `y` e pressione Enter.

Após a instalação, **feche e abra um novo CMD**. Se o comando `python` ainda não for reconhecido, adicione o Python ao PATH manualmente:

```cmd
setx PATH "%PATH%;%LOCALAPPDATA%\Programs\Python\Python312;%LOCALAPPDATA%\Programs\Python\Python312\Scripts"
```

Feche e abra o CMD novamente e verifique a instalação:

```cmd
python --version
pip --version
```

A saída esperada é algo como:

```
Python 3.12.x
pip 24.x ...
```

---

## 2. (Opcional) Desabilitar o Alias da Microsoft Store

Se ao rodar `python` aparecer uma mensagem sugerindo instalar pelo Microsoft Store, desative o alias:

1. Vá em **Configurações → Aplicativos → Aliases de execução do aplicativo**
2. Desative as entradas `python.exe` e `python3.exe`

Depois execute novamente `python --version` no CMD.

---

## 3. Instalar o Pytest

```cmd
pip install pytest
```

Verifique a instalação:

```cmd
pytest --version
```

---

## 4. Instalar o Playwright e o plugin para Pytest

```cmd
pip install playwright pytest-playwright
```

---

## 5. Instalar os Browsers do Playwright

O Playwright precisa baixar os navegadores (Chromium, Firefox e WebKit):

```cmd
playwright install
```

> Esse passo pode demorar alguns minutos pois faz o download dos browsers.

---

## 6. Verificar tudo instalado

```cmd
python --version
pip --version
pytest --version
playwright --version
```

---

## Resumo dos Comandos

| Passo | Comando |
|-------|---------|
| Instalar Python | `winget install Python.Python.3.12` |
| Corrigir PATH (se necessário) | `setx PATH "%PATH%;%LOCALAPPDATA%\Programs\Python\Python312;%LOCALAPPDATA%\Programs\Python\Python312\Scripts"` |
| Instalar Pytest | `pip install pytest` |
| Instalar Playwright + plugin | `pip install playwright pytest-playwright` |
| Instalar browsers | `playwright install` |

---

## Possíveis Problemas

**`python` não é reconhecido como comando**
→ Feche e abra um novo CMD após a instalação. Se persistir, execute o comando `setx` do Passo 1.

**`winget` não é reconhecido**
→ Atualize o Windows ou instale o Python manualmente em [python.org/downloads](https://www.python.org/downloads/). Na instalação, marque **"Add Python to PATH"**.

**Erro de permissão ao instalar pacotes**
→ Execute o CMD como **Administrador** (clique com o botão direito → "Executar como administrador").
