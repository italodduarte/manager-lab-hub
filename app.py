import streamlit as st
import pandas as pd

st.set_page_config(page_title="Manager Lab Hub", layout="wide", page_icon="🦁")

# --- NAVEGAÇÃO LATERAL ---
st.sidebar.title("🦁 Manager Lab Hub")
st.sidebar.caption("Central de Dados & Imersão | Prof. Ítalo Duarte")
pagina = st.sidebar.radio("Selecione a Página:", [
    "📊 Estatísticas Gerais", 
    "👤 Perfil do Clube & Elenco",
    "📰 Mídia Hub & Coletivas"
])

# ==========================================
# PÁGINA 1: ESTATÍSTICAS GERAIS
# ==========================================
if pagina == "📊 Estatísticas Gerais":
    st.title("🏆 Campeonato Brasileiro - Série A 2026")
    st.caption("Central de Análise do Campeonato | Manager Lab Hub")

    dados_tabela = [
        {"Pos": 1, "Clube": "Palmeiras", "PTS": 44, "J": 20, "V": 13, "E": 5, "D": 2, "GP": 33, "GC": 15, "SG": 18, "Forma": "🟢 🟢 🟡 🟢 🔴"},
        {"Pos": 2, "Clube": "Flamengo", "PTS": 40, "J": 20, "V": 12, "E": 4, "D": 4, "GP": 32, "GC": 14, "SG": 18, "Forma": "🟡 🟢 🔴 🟢 🟢"},
        {"Pos": 10, "Clube": "Vitória", "PTS": 25, "J": 20, "V": 7, "E": 4, "D": 9, "GP": 22, "GC": 24, "SG": -2, "Forma": "🟢 🟢 🔴 🟡 🟢"},
        {"Pos": 20, "Clube": "Chapecoense", "PTS": 9, "J": 20, "V": 2, "E": 3, "D": 15, "GP": 10, "GC": 34, "SG": -24, "Forma": "🔴 🔴 🟡 🔴 🔴"},
    ]
    df_tabela = pd.DataFrame(dados_tabela)
    df_tabela["Aprov (%)"] = ((df_tabela["PTS"] / (df_tabela["J"] * 3)) * 100).round(1)

    st.dataframe(
        df_tabela[["Pos", "Clube", "PTS", "J", "V", "E", "D", "GP", "GC", "SG", "Aprov (%)", "Forma"]],
        use_container_width=True,
        hide_index=True,
        column_config={
            "Aprov (%)": st.column_config.ProgressColumn("Aproveitamento", format="%.1f%%", min_value=0, max_value=100),
            "Forma": st.column_config.TextColumn("Últimos 5 Jogos")
        }
    )

# ==========================================
# PÁGINA 2: PERFIL DO CLUBE & ELENCO
# ==========================================
elif pagina == "👤 Perfil do Clube & Elenco":
    st.title("🦁 Esporte Clube Vitória - Elenco 2026")
    st.caption("Gestão de Plantel, Departamento Médico e Notas FUMA")

    aba_elenco, aba_dm, aba_fuma = st.tabs(["📋 Plantel Principal", "🏥 D.M. & Pendurados", "⚙️ Desempenho FUMA"])

    with aba_elenco:
        st.subheader("Elenco Profissional (Notas da Última Partida)")
        dados_elenco = [
            {"Atleta": "Erick", "Posição": "ATA", "Nota Último Jogo": 6.5, "Destaque": "⭐️ Craque do Jogo vs Botafogo"},
            {"Atleta": "Lucas Arcanjo", "Posição": "GOL", "Nota Último Jogo": 6.0, "Destaque": "7 Defesas Importantes"},
            {"Atleta": "Emmanuel Martínez", "Posição": "MEI", "Nota Último Jogo": 6.5, "Destaque": "Distribuição no Meio"},
            {"Atleta": "Matheuzinho", "Posição": "MEI", "Nota Último Jogo": 6.5, "Destaque": "Criação de Jogadas"},
            {"Atleta": "René Sousa", "Posição": "ATA", "Nota Último Jogo": 6.5, "Destaque": "Pressão de Ataque"},
            {"Atleta": "Cacá", "Posição": "ZAG", "Nota Último Jogo": 6.0, "Destaque": "Solidez Defensiva"},
        ]
        st.dataframe(pd.DataFrame(dados_elenco), use_container_width=True, hide_index=True)

    with aba_dm:
        st.subheader("🏥 Departamento Médico & Disciplinar")
        st.info("Nenhuma nova lesão detectada no duelo contra o Botafogo.")

    with aba_fuma:
        st.subheader("📊 Média da Gameplay FUMA (Rodada 23)")
        m1, m2, m3 = st.columns(3)
        m1.metric("Precisão de Passe Manual", "68.3%", "82/120 Certos")
        m2.metric("Conversão de Chutes", "41.6%", "5 no Gol / 12 Totais")
        m3.metric("Desarmes Manuais", "9", "+8 em relação ao rival")

# ==========================================
# PÁGINA 3: MÍDIA HUB
# ==========================================
elif pagina == "📰 Mídia Hub & Coletivas":
    st.title("📰 Sala de Imprensa & Pós-Jogo")
    
    st.success("🏆 **ÚLTIMO RESULTADO:** EC Vitória 2 x 1 Botafogo (Barradão)")
    
    st.markdown("### 🗞️ **Giro da Imprensa**")
    st.info("**ge.globo:** Estreia com vitória! Ítalo Duarte ajusta a marcação e Leão bate o Botafogo no Barradão.")
    
    st.markdown("### 🎙️ **Coletiva de Imprensa do Técnico**")
    resp1 = st.text_area("📻 Rádio Sociedade: 'O time teve menos posse, mas foi cirúrgico nos desarmes (9) e nos contra-ataques. Esse era o plano?'")
    resp2 = st.text_area("📺 GE Bahia: 'Erick foi o craque do jogo hoje. Como avalia o desempenho individual e coletivo?'")
    
    if st.button("Salvar Respostas da Coletiva"):
        st.success("Respostas salvas no histórico da temporada!")
