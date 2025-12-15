import streamlit as st

# --- Konfiguracja Streamlit ---

st.set_page_config(
    page_title="🎄 Świąteczny Magazyn Mikołaja 🎁",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# --- Obrazek świąteczny (możesz wstawić link do dowolnego obrazka) ---
# Wskazówka: aby obrazek był dostępny na Streamlit Cloud,
# musi być on hostowany online lub umieszczony w repozytorium GitHub
# i odniesiony relatywną ścieżką (np. "images/santa_banner.png")
# Dla uproszczenia, użyjemy miejsca na obrazek.
st.image("https://www.freeiconspng.com/uploads/christmas-gift-png-27.png", width=150) # Przykładowy link do ikony prezentu

st.title("🎅 Skład Mikołaja - Świąteczny Magazyn Prezentów 🎁")
st.markdown("### Zarządzaj magicznymi podarkami przed Wielkim Dniem! ✨")

# --- Inicjalizacja Magazynu (Lista w Session State) ---

if 'magazyn' not in st.session_state:
    st.session_state.magazyn = []
    # Kilka początkowych prezentów świątecznych!
    st.session_state.magazyn = ["Lalka Elza", "Zestaw klocków LEGO", "Pluszowy Miś", "Ciasteczka Piernikowe"]

# --- Funkcje Logiki ---

def dodaj_towar(nazwa):
    """Dodaje prezent do listy magazynu."""
    if nazwa and nazwa not in st.session_state.magazyn:
        st.session_state.magazyn.append(nazwa)
        st.success(f"🎄 Dodano magiczny prezent: **{nazwa}**!")
        # Opcjonalnie resetujemy input po dodaniu (bezpieczna metoda)
        st.session_state.input_dodaj = "" 
    elif nazwa in st.session_state.magazyn:
        st.warning(f"🔔 Prezent **{nazwa}** już czeka w magazynie!")
    else:
        st.warning("🎁 Nazwa prezentu nie może być pusta, Mikołaju!")

def usun_towar(nazwa):
    """Usuwa prezent z listy magazynu."""
    try:
        st.session_state.magazyn.remove(nazwa)
        st.success(f"🗑️ Usunięto prezent: **{nazwa}** (pewnie trafił już do sań!)")
    except ValueError:
        st.error(f"🚨 Błąd: Prezent **{nazwa}** nie został znaleziony w składzie!")

# --- Interfejs Użytkownika (UI) ---

# --- 1. Panel Dodawania Prezentu ---
st.header("➕ Dodaj Nowy Prezent do Składu 🌟")
with st.container(border=True):
    # Inicjalizacja input_dodaj w session_state jeśli go nie ma
    if 'input_dodaj' not in st.session_state:
        st.session_state.input_dodaj = ""
        
    nowa_nazwa = st.text_input(
        "Wpisz nazwę magicznego prezentu:", 
        key="input_dodaj", 
        value=st.session_state.input_dodaj, # Używamy wartości z session_state
        placeholder="Np. 'Latający Dron', 'Rękawiczki Ciepłe'"
    )
    
    # Przycisk z callbackiem, aby wyczyścić pole po dodaniu
    # 'on_click' wywoła funkcję 'dodaj_towar' bez argumentów,
    # jeśli 'nowa_nazwa' zostanie przekazana w 'args'
    if st.button("DODAJ PREZENT! 🎁", type="primary"):
        dodaj_towar(nowa_nazwa)


st.divider()

# --- 2. Panel Usuwania Prezentu ---
st.header("➖ Usuń Prezent ze Składu 🦌")
with st.container(border=True):
    if st.session_state.magazyn:
        towar_do_usuniecia = st.selectbox(
            "Wybierz prezent, który już wyruszył w drogę:", 
            options=st.session_state.magazyn,
            key="select_usun"
        )
        
        if st.button("USUŃ PREZENT! 🔥", type="secondary"):
            usun_towar(towar_do_usuniecia)
    else:
        st.info("❄️ Magazyn jest pusty, wszystkie prezenty już rozdane!")

st.divider()

# --- 3. Wyświetlanie Stanu Magazynu ---
st.header("📖 Aktualna Lista Prezentów Mikołaja 📜")

if st.session_state.magazyn:
    # Stylizowana tabela z prezentami
    df_prezenty = {
        "Lp.": range(1, len(st.session_state.magazyn) + 1),
        "Nazwa Magicznego Prezentu 🪄": st.session_state.magazyn
    }
    st.dataframe(df_prezenty, hide_index=True)
    
    st.info(f"✨ Obecnie w składzie czeka na dostawę: **{len(st.session_state.magazyn)}** różnych magicznych prezentów!")
else:
    st.markdown("### 🎅 Ho ho ho! Magazyn jest obecnie **pusty**! Czas na tworzenie nowych prezentów!")

st.markdown("---")
st.markdown("🌟 Wesołych Świąt i Szczęśliwego Nowego Roku! 🌟")
