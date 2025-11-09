# Machine Learning End-to-End

Este repositório reúne um pequeno projeto de exemplo que percorre um fluxo end-to-end de Machine Learning: preparação de dados e experimentos (notebooks), um modelo treinado para previsão de aluguel, e uma API + front-end para demonstrar o uso em produção local.

## Visão geral

- API: Flask que carrega um modelo (joblib) e serve endpoints para previsão de aluguel.
- FrontEnd: aplicação Angular (SimpleRent) para interface com o usuário.
- MakingModel: dados e notebooks usados para explorar e treinar modelos.

O objetivo é ser um projeto didático que mostra: preparação de dados, treinamento de modelo, empacotamento (joblib) e exposição via API, e uma UI simples em Angular.

## Estrutura do repositório

```
README.md
API/
	├─ BancoDeDados/        # módulo de persistência usado pela API
	├─ main.py               # API Flask que carrega o modelo e fornece endpoints
	└─ model/                # onde o modelo serializado (pkl) deve ficar
FrontEnd/
	└─ SimpleRent/           # app Angular (package.json, src/, etc.)
MakingModel/
	├─ house_data.csv       # dados brutos
	├─ main.ipynb           # notebook de exploração/treinamento
	└─ main.py              # (scripts auxiliares de experimentos)
model/                    # (pasta para modelos treinados, se utilizada)
```

## Pré-requisitos

- Python 3.8+ (recomendo 3.8–3.11)
- pip
- Node.js + npm (para rodar o front-end Angular)
- (Opcional) Angular CLI para fluxo de desenvolvimento front-end

OBS: Não há um `requirements.txt` no repositório atualmente. As dependências mínimas usadas pela API incluem: `Flask` e `joblib`. O modelo pode ter sido treinado com scikit-learn; nesse caso instale `scikit-learn` também.

## Rodando a API (Windows PowerShell)

1. Abra um terminal na pasta `API`:

```powershell
cd API
```

2. Crie e ative um ambiente virtual (recomendado):

```powershell
python -m venv .\venv
.\venv\Scripts\Activate
```

3. Instale dependências (se não houver `requirements.txt`, instale manualmente):

```powershell
pip install flask joblib scikit-learn
```

4. Verifique se existe o arquivo do modelo em `API/model/Modelo_Floresta_Aleatoria_v1.pkl`. O arquivo deve existir para que a API consiga responder às previsões.

5. Execute a API:

```powershell
python main.py
```

A API expõe (entre outros):

- GET /Welcome — retorna uma mensagem de boas-vindas.
- POST /Rent-Forecast — recebe JSON com os campos abaixo e retorna a previsão do aluguel.

Exemplo de corpo JSON esperado pelo endpoint `/Rent-Forecast` (os nomes das chaves são os que o código espera):

```json
{
  "city": 1,
  "area": 85.0,
  "rooms": 3,
  "bathroom": 2,
  "parkingspaces": 1,
  "floor": 2,
  "animal": 0,
  "furniture": 1,
  "hoa(R$)": 350.0,
  "propertytax(R$)": 80.0
}
```

Observação: o código salva logs usando `BancoDeDados.database.LogDb()` e grava as entradas na base configurada ali.

## Rodando o FrontEnd (Angular)

1. Vá para a pasta do front-end e instale dependências:

```powershell
cd FrontEnd\SimpleRent
npm install
```

2. Inicie o servidor de desenvolvimento:

```powershell
npm start
# ou
ng serve
```

Isso inicia a aplicação Angular (por padrão em `http://localhost:4200`) — verifique o `package.json` para os scripts (ex.: `start` -> `ng serve`).

## Notebooks e experimentos

Veja `MakingModel/main.ipynb` para a exploração de dados e o fluxo de treinamento. O CSV `MakingModel/house_data.csv` contém os dados originais usados para treinar modelos.

## Observações e suposições

- Suponho que o arquivo de modelo serializado (`Modelo_Floresta_Aleatoria_v1.pkl`) esteja presente em `API/model/`. Se não estiver, execute os notebooks ou scripts em `MakingModel` para treinar e gerar o artefato.
- Se quiser um ambiente reproduzível, recomendo adicionar um `requirements.txt` e/ou um `Dockerfile` para a API e um `package-lock.json` para o front-end.

## Próximos passos sugeridos

1. Adicionar `requirements.txt` em `API/` com as dependências exatas.
2. Incluir um `README` curto dentro de `API/` e `FrontEnd/SimpleRent/` com instruções locais específicas.
3. Criar testes automatizados (ex.: testes unitários para a API que validem o endpoint `/Rent-Forecast`).
4. (Opcional) Criar um pipeline CI que rode lint/tests e construa a aplicação.

## Contato

Se quiser que eu: gerar o `requirements.txt`, criar exemplos de requests (curl/PowerShell) automatizados, adicionar um Dockerfile ou preparar testes, diga qual desses itens quer priorizar que eu implemente primeiro.

---

Atualizado automaticamente para fornecer um guia mais completo de execução local.
