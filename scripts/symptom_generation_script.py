import pandas as pd

# ----------------------------
# 1️⃣ Load Master Symptom List
# master_symptoms.csv columns: symptom,category,risk_level
symptoms_df = pd.read_excel("../datasheets/EutaSathi_symptoms_sheet.xlsx")
print(symptoms_df.columns)
# 2️⃣ Load Template List
# templates.csv columns: template_id, template_text, category_context
templates_df = pd.read_excel("../datasheets/EutaSathi_template_symptoms_sheet.xlsx")
print(templates_df.columns)
# 3️⃣ Prepare output
generated_rows = []

# ----------------------------
# 4️⃣ Loop through each symptom and generate sentences
for _, symptom_row in symptoms_df.iterrows():
    symptom = symptom_row['symptom']
    category = symptom_row['category']
    risk = symptom_row['risk_level']

    # Select all templates matching this category
    matched_templates = templates_df[templates_df['category_context'] == category]

    for _, template_row in matched_templates.iterrows():
        sentence = template_row['template_text'].replace("{symptom}", symptom)
        generated_rows.append({
            "text": sentence,
            "category": category,
            "risk_level": risk
        })

# ----------------------------
# 5️⃣ Convert to DataFrame
dataset_df = pd.DataFrame(generated_rows)

# Optional: shuffle dataset
dataset_df = dataset_df.sample(frac=1, random_state=42).reset_index(drop=True)

# ----------------------------
# 6️⃣ Save CSV for Hugging Face / NLP training
dataset_df.to_csv("../datasheets/generated_postnatal_dataset.csv", index=False, encoding='utf-8-sig')

print(f"✅ Generated {len(dataset_df)} sentences!")