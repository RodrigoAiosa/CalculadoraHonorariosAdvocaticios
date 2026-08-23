"""
Calculadora de Honorários Advocatícios
Baseada na Tabela Oficial de Honorários da OAB/SP - 2016

Desenvolvido com Streamlit
"""

import streamlit as st
import pandas as pd
from data.tabela_oab_sp_2016 import TABELA, SERVICOS_LISTA

# Configuração da página
st.set_page_config(
    page_title="Calculadora de Honorários OAB 2016",
    page_icon="⚖️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS customizado
st.markdown("""
<style>
    .main-header {
        font-size: 2.2rem;
        font-weight: 700;
        color: #1a365d;
        text-align: center;
        margin-bottom: 0.5rem;
    }
    .sub-header {
        text-align: center;
        color: #4a5568;
        margin-bottom: 2rem;
    }
    .result-box {
        background: linear-gradient(135deg, #1a365d 0%, #2b6cb0 100%);
        color: white;
        padding: 1.5rem;
        border-radius: 12px;
        text-align: center;
        margin: 1rem 0;
    }
    .result-value {
        font-size: 2.5rem;
        font-weight: 700;
    }
    .info-box {
        background-color: #ebf8ff;
        border-left: 4px solid #3182ce;
        padding: 1rem;
        border-radius: 0 8px 8px 0;
        margin: 1rem 0;
    }
    .warning-box {
        background-color: #fffaf0;
        border-left: 4px solid #dd6b20;
        padding: 1rem;
        border-radius: 0 8px 8px 0;
        margin: 1rem 0;
    }
    .stSelectbox label, .stNumberInput label {
        font-weight: 600;
    }
</style>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.image("https://img.icons8.com/color/96/law.png", width=80)
    st.title("⚖️ Menu")
    pagina = st.radio(
        "Navegação",
        ["🧮 Calculadora", "📋 Tabela Completa", "ℹ️ Sobre"],
        label_visibility="collapsed"
    )
    st.markdown("---")
    st.markdown("""
    **Tabela de referência:**  
    OAB/SP – Atualizada em 11/01/2016
    """)
    st.caption("Valores mínimos orientativos. Cada Seccional da OAB possui sua própria tabela.")

# ==================== PÁGINA: CALCULADORA ====================
if pagina == "🧮 Calculadora":
    st.markdown('<p class="main-header">Calculadora de Honorários Advocatícios</p>', unsafe_allow_html=True)
    st.markdown('<p class="sub-header">Baseada na Tabela Oficial da OAB/SP 2016</p>', unsafe_allow_html=True)

    st.markdown("""
    <div class="warning-box">
        <strong>⚠️ Aviso importante:</strong> Esta calculadora utiliza valores da Tabela de Honorários da 
        <strong>OAB São Paulo de 2016</strong> como referência orientativa. As tabelas de honorários são 
        fixadas por cada Conselho Seccional da OAB e possuem valores atualizados anualmente. 
        Os honorários devem ser sempre contratados por escrito (art. 41 do Código de Ética da OAB).
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns([1.2, 1])

    with col1:
        st.subheader("1. Selecione o serviço")
        
        # Filtro por categoria
        categorias = list(TABELA.keys())
        categoria_selecionada = st.selectbox(
            "Categoria",
            options=["Todas"] + categorias,
            index=0
        )

        # Filtrar serviços
        if categoria_selecionada == "Todas":
            opcoes = SERVICOS_LISTA
        else:
            opcoes = [s for s in SERVICOS_LISTA if s["categoria"] == categoria_selecionada]

        labels = [s["label"] for s in opcoes]
        servico_escolhido = st.selectbox(
            "Serviço / Procedimento",
            options=labels,
            index=0
        )

        # Dados do serviço selecionado
        servico_data = next(s for s in opcoes if s["label"] == servico_escolhido)

        st.markdown("---")
        st.subheader("2. Dados para cálculo")

        valor_causa = st.number_input(
            "Valor da causa / proveito econômico (R$)",
            min_value=0.0,
            value=10000.0,
            step=100.0,
            format="%.2f",
            help="Informe o valor econômico da questão ou o proveito esperado para o cliente."
        )

        # Percentual customizado (opcional)
        usar_percentual_custom = st.checkbox("Usar percentual personalizado", value=False)
        if usar_percentual_custom:
            percentual_usado = st.slider(
                "Percentual de honorários (%)",
                min_value=1.0,
                max_value=30.0,
                value=float(servico_data["percentual"]) if servico_data["percentual"] else 20.0,
                step=0.5
            )
        else:
            percentual_usado = servico_data["percentual"]

    with col2:
        st.subheader("Resultado do Cálculo")

        # Cálculo
        minimo = servico_data["minimo"]
        percentual = percentual_usado

        if percentual is not None and valor_causa > 0:
            valor_percentual = valor_causa * (percentual / 100)
            valor_final = max(valor_percentual, minimo)
            base_calculo = "percentual + mínimo"
        else:
            valor_final = minimo
            valor_percentual = 0
            base_calculo = "valor mínimo fixo"

        # Exibição do resultado
        st.markdown(f"""
        <div class="result-box">
            <div style="font-size: 1rem; opacity: 0.9;">Honorários sugeridos (mínimo)</div>
            <div class="result-value">R$ {valor_final:,.2f}</div>
        </div>
        """, unsafe_allow_html=True)

        # Detalhamento
        st.markdown("#### Detalhamento")
        st.write(f"**Serviço:** {servico_data['servico']}")
        st.write(f"**Categoria:** {servico_data['categoria']}")
        
        if percentual is not None:
            st.write(f"**Percentual aplicado:** {percentual:.1f}%")
            st.write(f"**Valor pelo percentual:** R$ {valor_percentual:,.2f}")
        
        st.write(f"**Valor mínimo da tabela:** R$ {minimo:,.2f}")
        st.write(f"**Base do cálculo:** {base_calculo}")

        if servico_data["observacao"]:
            st.info(f"**Observação da tabela:** {servico_data['observacao']}")

        # Sugestão de parcelamento (padrão da tabela)
        st.markdown("---")
        st.markdown("#### 💡 Sugestão de parcelamento (padrão OAB)")
        st.caption("Salvo estipulação diversa: 1/3 no início, 1/3 até a decisão de 1º grau e 1/3 no final.")
        
        terco = valor_final / 3
        st.write(f"- **Início do trabalho:** R$ {terco:,.2f}")
        st.write(f"- **Até decisão de 1º grau:** R$ {terco:,.2f}")
        st.write(f"- **Final / êxito:** R$ {terco:,.2f}")

    # Observações gerais
    st.markdown("---")
    st.markdown("""
    <div class="info-box">
        <strong>📌 Lembretes importantes:</strong><br>
        • Os honorários de sucumbência pertencem ao advogado e não excluem os contratados.<br>
        • Todas as despesas (custas, locomoção, cópias etc.) são de responsabilidade do cliente.<br>
        • O advogado deve contratar por escrito o valor, reajuste e condições de pagamento.<br>
        • A tabela serve como referência mínima orientativa (Código de Ética da OAB).
    </div>
    """, unsafe_allow_html=True)

# ==================== PÁGINA: TABELA COMPLETA ====================
elif pagina == "📋 Tabela Completa":
    st.markdown('<p class="main-header">Tabela de Honorários OAB/SP 2016</p>', unsafe_allow_html=True)
    st.markdown('<p class="sub-header">Valores mínimos oficiais (atualizados em 11/01/2016)</p>', unsafe_allow_html=True)

    st.markdown("""
    <div class="info-box">
        A atualização monetária da Tabela de 2016 foi calculada com base na 
        “Tabela Prática para Cálculo de Atualização Monetária dos Débitos Judiciais” 
        do TJSP.
    </div>
    """, unsafe_allow_html=True)

    for categoria, itens in TABELA.items():
        with st.expander(f"📁 {categoria}", expanded=(categoria == "Parte Geral")):
            df_data = []
            for item in itens:
                perc = f"{item['percentual']:.0f}%" if item["percentual"] else "—"
                df_data.append({
                    "Item": item["item"],
                    "Serviço": item["servico"],
                    "Percentual": perc,
                    "Valor Mínimo (R$)": f"{item['minimo']:,.2f}",
                    "Observação": item["observacao"][:80] + "..." if len(item["observacao"]) > 80 else item["observacao"]
                })
            df = pd.DataFrame(df_data)
            st.dataframe(df, use_container_width=True, hide_index=True)

    st.markdown("---")
    st.caption("Fonte: Tabela de Honorários Advocatícios da OAB/SP – 2016. Valores em Reais (R$).")

# ==================== PÁGINA: SOBRE ====================
else:
    st.markdown('<p class="main-header">Sobre o Projeto</p>', unsafe_allow_html=True)

    st.markdown("""
    ### 🎯 Objetivo
    Ferramenta simples e prática para advogados(as) calcularem honorários com base 
    na **Tabela de Honorários da OAB/SP de 2016**, uma das mais completas e 
    referenciadas daquele período.

    ### ⚖️ Base Legal
    - **Lei nº 8.906/1994** (Estatuto da Advocacia e da OAB) – art. 22 e art. 58, V  
    - **Código de Ética e Disciplina da OAB** – arts. 36 e 41  
    - Tabela de Honorários da Seccional de São Paulo (aprovada e atualizada em 2016)

    ### 📌 Como usar
    1. Vá em **Calculadora**
    2. Escolha a categoria e o serviço
    3. Informe o valor da causa / proveito econômico
    4. Veja o valor mínimo sugerido e a sugestão de parcelamento

    ### ⚠️ Avisos
    - Esta é uma ferramenta **orientativa**. Os valores reais devem ser negociados 
      entre advogado e cliente e formalizados em contrato escrito.
    - Cada Seccional da OAB (estado) possui sua própria tabela, com valores e 
      critérios que podem diferir.
    - Os valores de 2016 **não estão atualizados** para o poder de compra atual. 
      Use apenas como referência histórica ou base de cálculo.
    - A tabela não substitui a análise da complexidade do caso, tempo, renome do 
      profissional e demais critérios do art. 36 do Código de Ética.

    ### 🛠️ Tecnologias
    - Python 3
    - Streamlit
    - Pandas

    ### 📂 Estrutura do projeto
    ```
    calculadora_honorarios_oab/
    ├── app.py
    ├── data/
    │   └── tabela_oab_sp_2016.py
    ├── requirements.txt
    └── README.md
    ```
    """)

    st.markdown("---")
    st.info("Desenvolvido para fins educacionais e de apoio à advocacia. Não constitui aconselhamento jurídico.")
