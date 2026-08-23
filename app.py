"""Calculadora de Honorarios Advocaticios - Versao Completa"""
import streamlit as st
import pandas as pd
from io import BytesIO
from datetime import datetime
try:
    from data.tabela_oab_sp_2016 import TABELA, SERVICOS_LISTA, FATOR_CORRECAO_2016_2026, CLAUSULAS_MODELO
except ImportError:
    import sys
    from pathlib import Path
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    from data.tabela_oab_sp_2016 import TABELA, SERVICOS_LISTA, FATOR_CORRECAO_2016_2026, CLAUSULAS_MODELO

st.set_page_config(page_title='Calculadora de Honorarios OAB', page_icon='⚖️', layout='wide', initial_sidebar_state='expanded')

st.markdown('''
<style>
.main-header { font-size: 1.9rem; font-weight: 700; color: #1a365d; text-align: center; }
.sub-header { text-align: center; color: #4a5568; margin-bottom: 1rem; }
.result-box { background: linear-gradient(135deg, #1a365d 0%, #2b6cb0 100%); color: white; padding: 1.3rem; border-radius: 12px; text-align: center; margin: 0.8rem 0; }
.result-value { font-size: 2.2rem; font-weight: 700; }
.info-box, .warning-box { padding: 1rem; border-radius: 0 8px 8px 0; margin: 0.8rem 0; color: #000 !important; }
.info-box { background-color: #ebf8ff; border-left: 4px solid #3182ce; }
.warning-box { background-color: #fffaf0; border-left: 4px solid #dd6b20; }
.info-box *, .warning-box * { color: #000 !important; }
</style>
''', unsafe_allow_html=True)

def fmt_brl(v):
    return f'R$ {v:,.2f}'.replace(',', 'X').replace('.', ',').replace('X', '.')

def _ascii_safe(text):
    """Remove acentos e caracteres nao suportados pelo Helvetica do FPDF."""
    if text is None:
        return ""
    s = str(text)
    repl = {
        "á": "a", "à": "a", "ã": "a", "â": "a", "ä": "a",
        "é": "e", "è": "e", "ê": "e", "ë": "e",
        "í": "i", "ì": "i", "î": "i", "ï": "i",
        "ó": "o", "ò": "o", "õ": "o", "ô": "o", "ö": "o",
        "ú": "u", "ù": "u", "û": "u", "ü": "u",
        "ç": "c", "ñ": "n",
        "Á": "A", "À": "A", "Ã": "A", "Â": "A", "Ä": "A",
        "É": "E", "È": "E", "Ê": "E", "Ë": "E",
        "Í": "I", "Ì": "I", "Î": "I", "Ï": "I",
        "Ó": "O", "Ò": "O", "Õ": "O", "Ô": "O", "Ö": "O",
        "Ú": "U", "Ù": "U", "Û": "U", "Ü": "U",
        "Ç": "C", "Ñ": "N",
        "–": "-", "—": "-", "•": "-", "·": "-",
        "R$": "R$", "º": "o", "ª": "a",
    }
    for a, b in repl.items():
        s = s.replace(a, b)
    return s.encode("latin-1", errors="replace").decode("latin-1")


def gerar_pdf_proposta(dados):
    """Gera PDF simples. Retorna bytes vazios se falhar (nao quebra a app)."""
    try:
        from fpdf import FPDF
    except ImportError:
        return b""
    try:
        pdf = FPDF()
        pdf.set_auto_page_break(auto=True, margin=15)
        pdf.add_page()
        pdf.set_margins(15, 15, 15)
        pdf.set_font("Helvetica", "B", 14)
        pdf.cell(0, 10, _ascii_safe("Proposta de Honorarios Advocaticios"), ln=True, align="C")
        pdf.set_font("Helvetica", "", 10)
        pdf.cell(0, 8, _ascii_safe(f"Data: {datetime.now().strftime('%d/%m/%Y %H:%M')}"), ln=True, align="C")
        pdf.ln(6)
        pdf.set_font("Helvetica", "B", 12)
        pdf.cell(0, 8, _ascii_safe("Dados do calculo"), ln=True)
        pdf.set_font("Helvetica", "", 10)
        usable = pdf.w - pdf.l_margin - pdf.r_margin
        for k, v in dados.items():
            line = _ascii_safe(f"{k}: {v}")
            pdf.multi_cell(usable, 6, line)
        pdf.ln(4)
        pdf.set_font("Helvetica", "", 9)
        pdf.multi_cell(usable, 5, _ascii_safe(
            "Valores orientativos com base na tabela OAB e criterios de mercado. "
            "Formalize sempre por contrato escrito (art. 41 do Codigo de Etica da OAB). "
            "Honorarios de sucumbencia pertencem ao advogado e nao excluem os contratados."
        ))
        out_buf = BytesIO()
        pdf.output(out_buf)
        return out_buf.getvalue()
    except Exception:
        return b""

with st.sidebar:
    st.markdown('### ⚖️ Menu')
    pagina = st.radio('Nav', ['Calculadora Principal', 'Custo Real da Hora', 'Comparar Cenarios', 'Sucumbencia (art. 85 CPC)', 'Tabela Completa', 'Clausulas Contratuais', 'Sobre'], label_visibility='collapsed')
    st.markdown('---')
    aplicar_correcao = st.checkbox('Aplicar correcao 2016->2026 (x1,75)', value=True)
    fator = FATOR_CORRECAO_2016_2026 if aplicar_correcao else 1.0
    st.caption(f'Fator: **{fator:.2f}**')
    st.caption('Base: OAB/SP 2016 + mercado 2025/2026')

# ===== CALCULADORA PRINCIPAL =====
if pagina == 'Calculadora Principal':
    st.markdown('<p class="main-header">Calculadora de Honorarios Advocatícios</p>', unsafe_allow_html=True)
    st.markdown('<p class="sub-header">Tabela OAB · Percentual · Fixo · Hora · Exito · Misto</p>', unsafe_allow_html=True)
    st.markdown('<div class="warning-box"><strong>Aviso:</strong> Valores orientativos. Formalize por contrato escrito. Sucumbencia nao exclui honorarios contratados.</div>', unsafe_allow_html=True)
    modelo = st.radio('Modelo de precificacao', ['Tabela OAB (minimo)', 'Percentual sobre base', 'Valor fixo', 'Por hora tecnica', 'Exito (success fee)', 'Misto (fixo + exito)'], horizontal=True)
    col1, col2 = st.columns([1.15, 1])
    with col1:
        st.subheader('1. Servico e base')
        cat = st.selectbox('Categoria', ['Todas'] + list(TABELA.keys()))
        busca = st.text_input('Buscar servico', placeholder='Ex: inventario, despejo...')
        opcoes = SERVICOS_LISTA
        if cat != 'Todas':
            opcoes = [s for s in opcoes if s['categoria'] == cat]
        if busca.strip():
            q = busca.strip().lower()
            opcoes = [s for s in opcoes if q in s['servico'].lower() or q in s['categoria'].lower()]
        if not opcoes:
            st.warning('Nenhum servico encontrado.'); st.stop()
        labels = [s['label'] for s in opcoes]
        escolha = st.selectbox('Servico / Procedimento', labels)
        serv = next(s for s in opcoes if s['label'] == escolha)
        minimo_tab = serv['minimo'] * fator
        perc_tab = serv['percentual']
        st.markdown('---'); st.subheader('2. Dados do calculo')
        valor_base = st.number_input('Valor da causa / proveito economico (R$)', min_value=0.0, value=50000.0, step=500.0, format='%.2f')
        valor_final = 0.0; detalhe = {}
        if modelo == 'Tabela OAB (minimo)':
            if perc_tab is not None and valor_base > 0:
                vp = valor_base * (perc_tab / 100); valor_final = max(vp, minimo_tab)
                detalhe = {'Percentual tabela': f'{perc_tab:.1f}%', 'Valor %': fmt_brl(vp), 'Minimo': fmt_brl(minimo_tab)}
            else:
                valor_final = minimo_tab; detalhe = {'Base': 'Valor minimo da tabela'}
        elif modelo == 'Percentual sobre base':
            p = st.slider('Percentual (%)', 1.0, 40.0, float(perc_tab or 20.0), 0.5)
            valor_final = valor_base * (p / 100); detalhe = {'Percentual': f'{p:.1f}%', 'Base': fmt_brl(valor_base)}
        elif modelo == 'Valor fixo':
            valor_final = st.number_input('Valor fixo contratado (R$)', min_value=0.0, value=float(minimo_tab), step=100.0, format='%.2f')
            detalhe = {'Tipo': 'Valor fixo'}
        elif modelo == 'Por hora tecnica':
            horas = st.number_input('Horas estimadas', min_value=0.5, value=10.0, step=0.5)
            valor_hora = st.number_input('Valor da hora (R$)', min_value=50.0, value=400.0, step=10.0, format='%.2f')
            valor_final = horas * valor_hora; detalhe = {'Horas': horas, 'Valor/hora': fmt_brl(valor_hora)}
        elif modelo == 'Exito (success fee)':
            p_exito = st.slider('Percentual de exito (%)', 5.0, 40.0, 20.0, 0.5)
            valor_final = valor_base * (p_exito / 100)
            detalhe = {'% exito': f'{p_exito:.1f}%', 'Base': fmt_brl(valor_base)}
            st.info('Cobrado apenas em caso de exito.')
        elif modelo == 'Misto (fixo + exito)':
            fixo = st.number_input('Valor fixo (R$)', min_value=0.0, value=float(minimo_tab * 0.5), step=100.0, format='%.2f')
            p_exito = st.slider('% de exito sobre o resultado', 5.0, 30.0, 15.0, 0.5)
            valor_exito = valor_base * (p_exito / 100); valor_final = fixo + valor_exito
            detalhe = {'Fixo': fmt_brl(fixo), '% exito': f'{p_exito:.1f}%', 'Valor exito': fmt_brl(valor_exito)}
        st.markdown('---')
        complexidade = st.select_slider('Fator de complexidade / urgencia', options=['Baixa (0,8x)', 'Normal (1,0x)', 'Alta (1,3x)', 'Muito alta (1,6x)'], value='Normal (1,0x)')
        mult = {'Baixa (0,8x)': 0.8, 'Normal (1,0x)': 1.0, 'Alta (1,3x)': 1.3, 'Muito alta (1,6x)': 1.6}[complexidade]
        valor_final *= mult
    with col2:
        st.subheader('Resultado')
        st.markdown(f'<div class="result-box"><div style="opacity:0.9;font-size:0.95rem;">Honorarios sugeridos</div><div class="result-value">{fmt_brl(valor_final)}</div><div style="font-size:0.85rem;opacity:0.85;margin-top:0.3rem;">{modelo} · {complexidade}</div></div>', unsafe_allow_html=True)
        st.markdown('#### Detalhamento')
        st.write(f"**Servico:** {serv['servico']}")
        st.write(f"**Categoria:** {serv['categoria']}")
        st.write(f'**Minimo tabela (ajustado):** {fmt_brl(minimo_tab)}')
        for k, v in detalhe.items(): st.write(f'**{k}:** {v}')
        if serv['observacao']: st.info(serv['observacao'])
        st.markdown('---'); st.markdown('#### Parcelamento sugerido')
        forma = st.selectbox('Forma', ['1/3 + 1/3 + 1/3', '50% inicio + 50% final', '30% + 40% + 30%', 'A vista', 'Personalizado'])
        if forma == '1/3 + 1/3 + 1/3':
            t = valor_final / 3; parcelas_txt = f'Inicio {fmt_brl(t)} | 1 grau {fmt_brl(t)} | Final {fmt_brl(t)}'
            st.write(f'- Inicio: **{fmt_brl(t)}**'); st.write(f'- Ate 1 grau: **{fmt_brl(t)}**'); st.write(f'- Final: **{fmt_brl(t)}**')
        elif forma == '50% inicio + 50% final':
            m = valor_final / 2; parcelas_txt = f'Inicio {fmt_brl(m)} | Final {fmt_brl(m)}'
            st.write(f'- Inicio: **{fmt_brl(m)}**'); st.write(f'- Final: **{fmt_brl(m)}**')
        elif forma == '30% + 40% + 30%':
            p1, p2, p3 = valor_final*0.3, valor_final*0.4, valor_final*0.3
            parcelas_txt = f'30% {fmt_brl(p1)} | 40% {fmt_brl(p2)} | 30% {fmt_brl(p3)}'
            st.write(f'- Entrada 30%: **{fmt_brl(p1)}**'); st.write(f'- Intermed. 40%: **{fmt_brl(p2)}**'); st.write(f'- Final 30%: **{fmt_brl(p3)}**')
        elif forma == 'A vista':
            parcelas_txt = f'A vista {fmt_brl(valor_final)}'; st.write(f'- **{fmt_brl(valor_final)}** a vista')
        else:
            n = st.number_input('N de parcelas', 2, 24, 3); parc = valor_final / n
            parcelas_txt = f'{n}x de {fmt_brl(parc)}'; st.write(f'- **{n}x** de **{fmt_brl(parc)}**')
        st.markdown('---')
        dados_pdf = {'Modelo': modelo, 'Servico': serv['servico'], 'Categoria': serv['categoria'], 'Valor base': fmt_brl(valor_base), 'Complexidade': complexidade, 'Honorarios': fmt_brl(valor_final), 'Parcelamento': forma, 'Detalhe': parcelas_txt}
        pdf_bytes = b''
        try:
            pdf_bytes = gerar_pdf_proposta(dados_pdf) or b''
        except Exception:
            pdf_bytes = b''
        if pdf_bytes:
            st.download_button('Baixar Proposta em PDF', data=pdf_bytes, file_name=f"proposta_{datetime.now().strftime('%Y%m%d_%H%M')}.pdf", mime='application/pdf')
        texto_prop = f"PROPOSTA\nServico: {serv['servico']}\nModelo: {modelo}\nBase: {fmt_brl(valor_base)}\nHonorarios: {fmt_brl(valor_final)}\n{forma}: {parcelas_txt}\n"
        st.download_button('Baixar proposta (TXT)', texto_prop, file_name='proposta_honorarios.txt')

# ===== CUSTO REAL DA HORA =====
elif pagina == 'Custo Real da Hora':
    st.markdown('<p class="main-header">Custo Real da Hora do Escritorio</p>', unsafe_allow_html=True)
    st.markdown('<p class="sub-header">Preco minimo para nao trabalhar no prejuizo</p>', unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    with c1:
        st.subheader('Custos mensais')
        aluguel = st.number_input('Aluguel / coworking (R$)', 0.0, value=2000.0, step=100.0)
        softwares = st.number_input('Softwares / internet (R$)', 0.0, value=500.0, step=50.0)
        anuidade = st.number_input('Anuidade OAB + seguro (mensal)', 0.0, value=150.0, step=10.0)
        contador = st.number_input('Contador / admin (R$)', 0.0, value=400.0, step=50.0)
        outros = st.number_input('Outros custos fixos (R$)', 0.0, value=300.0, step=50.0)
        prolabore = st.number_input('Pro-labore desejado (R$)', 0.0, value=8000.0, step=500.0)
    with c2:
        st.subheader('Capacidade produtiva')
        horas_mes = st.number_input('Horas totais no mes', 1.0, value=160.0, step=8.0)
        pct_faturavel = st.slider('% horas faturaveis', 30, 80, 55)
        margem = st.slider('Margem de lucro (%)', 0, 50, 20)
        horas_fat = horas_mes * (pct_faturavel / 100)
        custo_total = aluguel + softwares + anuidade + contador + outros + prolabore
        custo_hora = custo_total / horas_fat if horas_fat else 0
        preco_hora = custo_hora * (1 + margem / 100)
        st.markdown('---')
        st.markdown(f'<div class="result-box"><div>Custo real da hora</div><div class="result-value">{fmt_brl(custo_hora)}</div><div style="margin-top:0.5rem;">Preco sugerido (com margem)</div><div style="font-size:1.6rem;font-weight:700;">{fmt_brl(preco_hora)}</div></div>', unsafe_allow_html=True)
        st.write(f'**Custo mensal total:** {fmt_brl(custo_total)}')
        st.write(f'**Horas faturaveis/mes:** {horas_fat:.0f}h')
        st.caption('Use este valor no modelo Por hora tecnica.')

# ===== CENARIOS =====
elif pagina == 'Comparar Cenarios':
    st.markdown('<p class="main-header">Comparar Cenarios de Precificacao</p>', unsafe_allow_html=True)
    base = st.number_input('Valor da causa / proveito (R$)', min_value=0.0, value=100000.0, step=1000.0, format='%.2f', key='cen_base')
    cols = st.columns(3); resultados = []
    for i, col in enumerate(cols):
        with col:
            st.markdown(f'#### Cenario {i+1}')
            tipo = st.selectbox('Tipo', ['Percentual', 'Fixo', 'Hora', 'Exito', 'Misto'], key=f't{i}')
            if tipo == 'Percentual':
                p = st.number_input('%', 1.0, 40.0, 20.0, key=f'p{i}'); v = base * p / 100
            elif tipo == 'Fixo':
                v = st.number_input('Valor (R$)', 0.0, value=5000.0, key=f'f{i}')
            elif tipo == 'Hora':
                h = st.number_input('Horas', 1.0, value=20.0, key=f'h{i}'); vh = st.number_input('R$/hora', 50.0, value=400.0, key=f'vh{i}'); v = h * vh
            elif tipo == 'Exito':
                pe = st.number_input('% exito', 5.0, 40.0, 25.0, key=f'e{i}'); v = base * pe / 100
            else:
                fx = st.number_input('Fixo (R$)', 0.0, value=3000.0, key=f'mx{i}'); pe = st.number_input('% exito', 5.0, 30.0, 15.0, key=f'me{i}'); v = fx + base * pe / 100
            st.metric('Total', fmt_brl(v)); resultados.append({'Cenario': f'Cenario {i+1}', 'Tipo': tipo, 'Valor': v})
    df = pd.DataFrame(resultados); df['Valor formatado'] = df['Valor'].apply(fmt_brl)
    st.dataframe(df[['Cenario', 'Tipo', 'Valor formatado']], use_container_width=True, hide_index=True)
    melhor = max(resultados, key=lambda x: x['Valor'])
    st.success(f"Maior valor: **{melhor['Cenario']}** ({melhor['Tipo']}) -> {fmt_brl(melhor['Valor'])}")

# ===== SUCUMBENCIA =====
elif pagina == 'Sucumbencia (art. 85 CPC)':
    st.markdown('<p class="main-header">Honorarios de Sucumbencia – art. 85 CPC</p>', unsafe_allow_html=True)
    st.markdown('<div class="info-box"><strong>Base legal:</strong> Art. 85, §2º CPC – 10% a 20% sobre condenacao, proveito economico ou valor atualizado da causa.</div>', unsafe_allow_html=True)
    base_suc = st.number_input('Base de calculo (R$)', 0.0, value=80000.0, step=500.0, format='%.2f')
    faixa = st.slider('Percentual de sucumbencia (%)', 10.0, 20.0, 15.0, 0.5)
    if st.checkbox('Majoracao em grau recursal (ilustrativo)', value=False):
        faixa = min(faixa + 5.0, 25.0)
    valor_suc = base_suc * (faixa / 100)
    st.markdown(f'<div class="result-box"><div>Honorarios de sucumbencia estimados</div><div class="result-value">{fmt_brl(valor_suc)}</div><div style="opacity:0.9;">{faixa:.1f}% sobre {fmt_brl(base_suc)}</div></div>', unsafe_allow_html=True)
    st.caption('Sucumbencia pertence ao advogado e e cumulativa com honorarios contratuais.')

# ===== TABELA =====
elif pagina == 'Tabela Completa':
    st.markdown('<p class="main-header">Tabela de Honorarios (referencia)</p>', unsafe_allow_html=True)
    st.caption(f'Valores base 2016 x fator {fator:.2f}' if fator != 1 else 'Valores base 2016')
    for categoria, itens in TABELA.items():
        with st.expander(categoria, expanded=(categoria == 'Parte Geral')):
            rows = []
            for it in itens:
                perc = f"{it['percentual']:.0f}%" if it['percentual'] else '-'
                rows.append({'Item': it['item'], 'Servico': it['servico'], 'Percentual': perc, 'Minimo (R$)': fmt_brl(it['minimo'] * fator), 'Observacao': (it['observacao'][:70] + '...') if len(it['observacao']) > 70 else it['observacao']})
            st.dataframe(pd.DataFrame(rows), use_container_width=True, hide_index=True)

# ===== CLAUSULAS =====
elif pagina == 'Clausulas Contratuais':
    st.markdown('<p class="main-header">Clausulas Contratuais – Modelo</p>', unsafe_allow_html=True)
    valor_c = st.number_input('Valor dos honorarios (R$)', 0.0, value=10000.0, step=500.0, format='%.2f')
    parc_c = st.text_area('Descricao do parcelamento', '1/3 no inicio, 1/3 ate decisao de 1 grau e 1/3 no final.')
    texto = CLAUSULAS_MODELO.format(valor=valor_c, parcelamento=parc_c)
    st.text_area('Modelo de clausulas', texto, height=380)
    st.download_button('Baixar clausulas (TXT)', texto, file_name='clausulas_honorarios.txt')
    st.info('Modelo generico. Adapte conforme Codigo de Etica da OAB.')

# ===== SOBRE =====
else:
    st.markdown('<p class="main-header">Sobre esta Calculadora</p>', unsafe_allow_html=True)
    st.markdown('''
### Funcionalidades
- Modelos: Tabela OAB, Percentual, Fixo, Hora, Exito, Misto
- Custo real da hora (break-even + margem)
- Comparacao de ate 3 cenarios
- Sucumbencia (art. 85 CPC)
- Correcao 2016 -> 2026 e fator de complexidade
- Parcelamentos flexiveis e exportacao PDF/TXT
- Clausulas contratuais modelo
- Categorias: Civel, Familia, Trabalhista, Previdenciario, Criminal, Empresarial, Digital

### Base legal
- Lei 8.906/1994 arts. 22, 23 e 58, V
- Codigo de Etica OAB arts. 36 e 41
- CPC art. 85

Valores orientativos. Formalize por contrato escrito.
''')
