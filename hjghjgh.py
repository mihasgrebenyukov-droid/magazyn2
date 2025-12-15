import streamlit as st

# --- Konfiguracja Streamlit ---

st.set_page_config(
    page_title="Prosty Magazyn (Lista)",
    layout="centered"
)

st.title("Prosty System Magazynowy")
st.markdown("### Zarządzanie Towarami przy użyciu List")

# --- Inicjalizacja Magazynu (Lista w Session State) ---

# Używamy st.session_state do przechowywania listy towarów, 
# aby jej stan nie znikał po interakcjach użytkownika.
if 'magazyn' not in st.session_state:
    st.session_state.magazyn = []
    
# Możesz dodać początkowe towary, jeśli chcesz:
# st.session_state.magazyn = ["Laptop", "Monitor", "Klawiatura"]

# --- Funkcje Logiki ---

def dodaj_towar(nazwa):
    """Dodaje towar do listy magazynu."""
    if nazwa and nazwa not in st.session_state.magazyn:
        st.session_state.magazyn.append(nazwa)
        st.success(f"Dodano: **{nazwa}**")
    elif nazwa in st.session_state.magazyn:
        st.warning(f"Towar **{nazwa}** już istnieje w magazynie.")
    else:
        st.warning("Nazwa towaru nie może być pusta.")

def usun_towar(nazwa):
    """Usuwa towar z listy magazynu."""
    try:
        st.session_state.magazyn.remove(nazwa)
        st.success(f"Usunięto: **{nazwa}**")
    except ValueError:
        st.error(f"Błąd: Towar **{nazwa}** nie został znaleziony.")

# --- Interfejs Użytkownika (UI) ---

# --- 1. Panel Dodawania Towaru ---
st.header("➕ Dodaj Towar")
with st.container(border=True):
    nowa_nazwa = st.text_input("Wpisz nazwę nowego towaru:", key="input_dodaj")
    
    # Przycisk, który wywoła funkcję dodawania po kliknięciu
    if st.button("Dodaj do Magazynu", type="primary"):
        dodaj_towar(nowa_nazwa)
        # Opcjonalnie: wyczyść pole tekstowe po dodaniu
        st.session_state.input_dodaj = "" 

st.divider()

# --- 2. Panel Usuwania Towaru ---
st.header("➖ Usuń Towar")
with st.container(border=True):
    if st.session_state.magazyn:
        # Pozwala wybrać towar z listy rozwijanej
        towar_do_usuniecia = st.selectbox(
            "Wybierz towar do usunięcia:", 
            options=st.session_state.magazyn,
            key="select_usun"
        )
        
        if st.button("Usuń z Magazynu", type="secondary"):
            usun_towar(towar_do_usuniecia)
    else:
        st.info("Magazyn jest pusty, nie ma nic do usunięcia.")

st.divider()

# --- 3. Wyświetlanie Stanu Magazynu ---
st.header("📋 Aktualny Stan Magazynu")

if st.session_state.magazyn:
    # Wyświetlanie listy towarów
    st.dataframe({
        "Lp.": range(1, len(st.session_state.magazyn) + 1),
        "Nazwa Towaru": st.session_state.magazyn
    }, hide_index=True)
    
    st.info(f"Łączna liczba różnych towarów: **{len(st.session_state.magazyn)}**")
else:
    st.markdown("### Magazyn jest obecnie **pusty**.")
