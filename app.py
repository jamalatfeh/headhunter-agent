import streamlit as st
import pandas as pd

st.set_page_config(page_title="Headhunter Agent", layout="wide")
st.title("🔍 Headhunter Agent")
st.markdown("**Demo: Consented candidate search for verified recruiters.**")

st.sidebar.header("Agent Rules")
st.sidebar.info("1. Blind search (no PII).\n2. Three-way consent gate.\n3. Injection defence.")

# Mock Database of Candidates
CANDIDATES = [
    {"id": 1, "name": "Maria Santos", "role": "Nurse", "skills": "ICU, DHA", "email": "maria@example.com", "consent": False},
    {"id": 2, "name": "John Doe", "role": "Nurse", "skills": "ER, DHA", "email": "john@example.com", "consent": True},
    {"id": 3, "name": "Aisha Khan", "role": "Nurse", "skills": "Pediatrics, DHA", "email": "aisha@example.com", "consent": False}
]

st.write("### 1. Recruiter Search")
search_query = st.text_input("Search by skill (e.g., ICU, ER)", "")

if search_query:
    st.write(f"Searching for: **{search_query}**")
    
    # 1. BLIND SEARCH (No names or emails shown yet)
    results = []
    for c in CANDIDATES:
        if search_query.lower() in c["skills"].lower():
            results.append({
                "Candidate ID": f"#{c['id']}",
                "Role": c["role"],
                "Skills": c["skills"],
                "Status": "Consent Granted" if c["consent"] else "Hidden (Awaiting Consent)"
            })
            
    if results:
        df = pd.DataFrame(results)
        st.dataframe(df, use_container_width=True)
    else:
        st.warning("No candidates found with that skill.")

st.write("### 2. The Consent Gate")
st.info("Candidate names and emails are hidden until they click 'Approve'.")

# Simulate the candidate's dashboard
st.write("---")
st.write("#### Candidate Dashboard (Simulation)")
candidate_to_approve = st.selectbox("Select a candidate to approve contact", ["Maria Santos", "Aisha Khan"])

if st.button("I Approve Contact for this Search"):
    st.success(f"Consent granted for {candidate_to_approve}. The recruiter can now see their email.")
    
    # Reveal the contact detail
    for c in CANDIDATES:
        if c["name"] == candidate_to_approve:
            st.write(f"**Candidate Contact:** {c['email']}")

st.write("### 3. Injection Defence")
uploaded_file = st.file_uploader("Upload a candidate message or PDF", type=["txt"])
if uploaded_file:
    content = uploaded_file.read().decode("utf-8", errors="ignore")
    if "ignore previous instructions" in content.lower():
        st.error("🚨 Quarantine Alert: Injection detected in candidate message.")
    else:
        st.success("Message is clean.")