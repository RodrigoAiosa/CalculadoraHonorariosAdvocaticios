# ⚖️ Calculadora de Honorários Advocatícios – OAB 2016

Aplicação web em **Python + Streamlit** para cálculo de honorários de advogados(as) com base na **Tabela Oficial de Honorários da OAB/SP de 2016**.

## 🎯 Funcionalidades

- **Calculadora interativa** de honorários
- Seleção por categoria e tipo de serviço
- Cálculo automático considerando percentual + valor mínimo da tabela
- Sugestão de parcelamento (1/3 + 1/3 + 1/3)
- Visualização completa da tabela de 2016
- Interface limpa e responsiva

## 📋 Serviços incluídos

| Categoria | Exemplos |
|-----------|----------|
| Parte Geral | Ações contenciosas, recursos, audiências, precatórias, advocacia de partido |
| Advocacia Cível | Despejo, possessórias, usucapião, mandado de segurança, juizados especiais |
| Família e Sucessões | Inventários, separação, divórcio, alimentos, investigação de paternidade |
| Atividades Avulsas | Consultas, pareceres, hora técnica |

## 🚀 Como executar

### 1. Clone ou baixe o projeto

```bash
cd calculadora_honorarios_oab
```

### 2. Crie um ambiente virtual (recomendado)

```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
# ou
venv\Scripts\activate      # Windows
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Execute a aplicação

```bash
streamlit run app.py
```

Acesse no navegador: **http://localhost:8501**

## ⚠️ Avisos Importantes

1. **Tabela de referência**: Utiliza a Tabela de Honorários da **OAB São Paulo de 2016**. Cada Seccional da OAB possui sua própria tabela.
2. **Valores históricos**: Os valores de 2016 **não estão atualizados** pelo índice de correção atual.
3. **Orientativa**: A tabela serve como referência mínima. O contrato escrito entre advogado e cliente prevalece.
4. **Sucumbência**: Honorários de sucumbência pertencem ao advogado e não excluem os contratados.

## ⚖️ Base Legal

- Lei nº 8.906/1994 (Estatuto da Advocacia) – arts. 22 e 58, V
- Código de Ética e Disciplina da OAB – arts. 36 e 41

## 🛠️ Tecnologias

- Python 3.8+
- Streamlit
- Pandas

## 📂 Estrutura

```
calculadora_honorarios_oab/
├── app.py                      # Aplicação principal
├── data/
│   └── tabela_oab_sp_2016.py   # Dados da tabela 2016
├── requirements.txt
└── README.md
```

## 📝 Licença

Uso livre para fins educacionais e profissionais. Não constitui aconselhamento jurídico.
