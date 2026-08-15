import streamlit as st
import pandas as pd

st.set_page_config(page_title="Manager Lab Hub", layout="wide", page_icon="🦁")

# --- NAVEGAÇÃO LATERAL (SIDEBAR) ---
st.sidebar.title("🦁 Manager Lab Hub")
st.sidebar.caption("Central de Dados & Imersão")
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
        {"Pos": 1, "Clube": "Palmeiras", "PTS": 44, "J": 19, "V": 13, "E": 5, "D": 1, "GP": 32, "GC": 13, "SG": 19, "Forma": "🟢 🟢 🟡 🟢 🟢"},
        {"Pos": 2, "Clube": "Flamengo", "PTS": 37, "J": 18, "V": 11, "E": 4, "D": 3, "GP": 31, "GC": 12, "SG": 19, "Forma": "🟡 🟢 🔴 🟢 🟢"},
        {"Pos": 11, "Clube": "Vitória", "PTS": 26, "J": 19, "V": 7, "E": 5, "D": 7, "GP": 20, "GC": 23, "SG": -3, "Forma": "🟢 🔴 🟡 🔴 🟢"},
        {"Pos": 20, "Clube": "Chapecoense", "PTS": 9, "J": 19, "V": 2, "E": 3, "D": 14, "GP": 10, "GC": 32, "SG": -22, "Forma": "🔴 🔴 🟡 🔴 🔴"},
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
        st.subheader("Elenco Profissional")
        dados_elenco = [
            {"Atleta": "Lucas Arcanjo", "Posição": "GOL", "Jogos": 19, "Nota Média": 7.2, "Gols": 0, "Assist.": 0},
            {"Atleta": "Wagner Leonardo", "Posição": "ZAG", "Jogos": 18, "Nota Média": 7.5, "Gols": 2, "Assist.": 0},
            {"Atleta": "Matheuzinho", "Posição": "MEI", "Jogos": 19, "Nota Média": 7.8, "Gols": 4, "Assist.": 6},
            {"Atleta": "Erick", "Posição": "ATA", "Jogos": 17, "Nota Média": 8.1, "Gols": 9, "Assist.": 3},
        ]
        st.dataframe(pd.DataFrame(dados_elenco), use_container_width=True, hide_index=True)

    with aba_dm:
        col_dm, col_cartoes = st.columns(2)
        with col_dm:
            st.subheader("🏥 Departamento Médico")
            st.info("Nenhum atleta sob cuidados intensivos no momento.")
            
        with col_cartoes:
            st.subheader("🟨 Pendurados (2 Amarelos)")
            st.warning("• **Wagner Leonardo** (ZAG) - Pendurado")

    with aba_fuma:
        st.subheader("📊 Avaliação de Precisão Manual (FUMA)")
        m1, m2, m3 = st.columns(3)
        m1.metric("Precisão de Passe Manual", "82%", "+3%")
        m2.metric("Conversão de Chutes", "34%", "-1%")
        m3.metric("Desarmes Manuais/Jogo", "14.2", "+1.5")

# ==========================================
# PÁGINA 3: MÍDIA HUB & COLETIVAS
# ==========================================
elif pagina == "📰 Mídia Hub & Coletivas":
    st.title("📰 Sala de Imprensa & Bastidores")
    st.caption("Repercussão da Mídia, Entrevistas e Termômetro do Club")

    aba_noticias, aba_coletiva, aba_termometro = st.tabs(["🗞️ Giro da Imprensa", "🎙️ Coletiva do Técnico", "📊 Termômetro do Save"])

    with aba_noticias:
        st.subheader("Últimas Manchetes")
        
        st.markdown("### 🟢 **GE Bahia**")
        st.info("**Expectativa no Barradão:** Ítalo Duarte ajusta a postura tática do Leão para a sequência do segundo turno no Brasileirão.")
        
        st.markdown("### 🗞️ **Jornal A Tarde**")
        st.write("> *'Com proposta pautada no controle de posse e intensidade nos desarmes, o Vitória tenta transformar o Barradão em uma fortaleza.'*")

    with aba_coletiva:
        st.subheader("🎙️ Entrevista Coletiva do Treinador")
        st.write("Responda às perguntas da imprensa pós-jogo:")
        
        resp1 = st.text_area("📻 Rádio Sociedade: 'Professor Ítalo, o que você priorizou na semana de treinos?'")
        resp2 = st.text_area("📺 SporTV: 'Como lidar com a pressão da torcida no Barradão jogando em estilo FUMA?'")
        
        if st.button("Salvar Respostas da Coletiva"):
            st.success("Respostas registradas com sucesso no histórico da temporada!")

    with aba_termometro:
        st.subheader("🗣️ Clima no Clube")
        
        col_torcida, col_diretoria = st.columns(2)
        with col_torcida:
            st.metric("Aprovação da Torcida", "78%", "+5%")
            st.progress(0.78)
            st.caption("Clima: Empulgado com o novo estilo de jogo.")
            
        with col_diretoria:
            st.metric("Confiança da Diretoria", "85%", "Estável")
            st.progress(0.85)
            st.caption("Meta do Semestre: Manter vaga no G-12 (Sul-Americana).")
