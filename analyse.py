import json
from collections import Counter

with open("items.json", "r") as f:
    data = json.load(f)

items = data.get("items", [])
slug_counts = Counter(item.get("slug", "") for item in items)

rapport = ["# Rapport de vérification SEO Webflow\n"]

for item in items:
    nom = item.get("name", "(sans nom)")
    slug = item.get("slug", "")
    seo_title = item.get("seoTitle", "")
    seo_description = item.get("seoDescription", "")

    problemes = []
    if not seo_title:
        problemes.append("❌ Titre SEO manquant")
    elif len(seo_title) < 10:
        problemes.append("⚠️ Titre SEO trop court")

    if not seo_description:
        problemes.append("❌ Description SEO manquante")
    elif len(seo_description) < 20:
        problemes.append("⚠️ Description SEO trop courte")

    if slug_counts[slug] > 1:
        problemes.append("❌ Slug en double")

    if problemes:
        rapport.append(f"- **{nom}** (`{slug}`) : " + ", ".join(problemes))

with open("rapport.md", "w") as f:
    f.write("\n".join(rapport))

print("Analyse terminée. Voir rapport.md")
