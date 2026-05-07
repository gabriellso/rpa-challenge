# RPA Challenge Solver

Automação em Python utilizando Selenium para resolver o desafio:

https://rpachallenge.com/

---

## Sobre o desafio

O formulário altera dinamicamente a posição dos campos após cada submissão.

Para resolver isso, a automação identifica os inputs através de atributos estáveis do DOM (`ng-reflect-name`) ao invés de depender da posição visual dos elementos.

---

## Tecnologias utilizadas

- Python
- Selenium
- Pandas
- OpenPyXL
- WebDriver Manager

---

## Funcionalidades

- Leitura automática do Excel
- Mapeamento dinâmico dos campos
- Automação resiliente
- Normalização de colunas do Excel
- Screenshot final da execução

---

## Resultado

✅ 100% de sucesso (70/70 campos)

---

## Como executar

Clone o repositório:

```bash
git clone https://github.com/SEU_USUARIO/rpa-challenge.git
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

Execute o projeto:

```bash
python main.py
```

---

## Screenshot

<img src="screenshots/final.png" width="800">