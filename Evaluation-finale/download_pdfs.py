"""Cree les PDF de la base documentaire touristique dans data/pdfs/.

Lancer avec : uv run python download_pdfs.py
"""
from pathlib import Path

PDF_DIR = Path(__file__).resolve().parent / "data" / "pdfs"

DOCUMENTS = {
    "guide_marrakech_atlas_essaouira.pdf": {
        "title": "Guide touristique - Marrakech, Atlas et Essaouira",
        "sections": [
            ("Marrakech", "Marrakech est une destination culturelle majeure. La medina, la place Jemaa el-Fna, les souks, les jardins Majorelle et les palais historiques permettent de comprendre l'architecture, l'artisanat et l'ambiance urbaine du Maroc. Les visites sont plus agreables le matin ou en fin d'apres-midi, surtout en ete."),
            ("Atlas", "Les excursions vers l'Atlas permettent de decouvrir les vallees, les villages berbères, les cascades et les paysages de montagne. Il faut prevoir des chaussures confortables, de l'eau, une veste en hiver et respecter les rythmes locaux."),
            ("Essaouira", "Essaouira est connue pour sa medina classee, son port, ses remparts, le vent, les activites nautiques et une ambiance plus calme que Marrakech. Elle convient aux voyageurs qui veulent combiner culture, mer et detente."),
            ("Saisons", "Le printemps et l'automne sont les periodes les plus confortables pour combiner Marrakech, Atlas et Essaouira. En ete, il faut eviter les longues visites sous le soleil a Marrakech et privilegier la cote ou la montagne."),
        ],
    },
    "guide_fes_rabat_chefchaouen.pdf": {
        "title": "Guide touristique - Fes, Rabat et Chefchaouen",
        "sections": [
            ("Fes", "Fes est une ville ideale pour un voyage culturel. Sa medina, ses medersas, ses tanneries et ses ateliers d'artisanat montrent l'importance historique et spirituelle de la ville. Un guide local peut aider a mieux comprendre les quartiers anciens."),
            ("Rabat", "Rabat combine patrimoine, institutions modernes et bord de mer. La Tour Hassan, le Mausolee Mohammed V, la Kasbah des Oudayas et la medina offrent un programme culturel accessible et moins intense que d'autres grandes villes."),
            ("Chefchaouen", "Chefchaouen attire les voyageurs pour ses ruelles bleues, son rythme calme et sa proximite avec les montagnes du Rif. Il faut respecter les habitants, eviter de bloquer les ruelles pour les photos et prevoir de bonnes chaussures."),
            ("Transport", "Entre les grandes villes marocaines, le train est souvent confortable pour Casablanca, Rabat, Marrakech, Fes et Tanger. Pour Chefchaouen, le bus ou le taxi collectif depuis Tanger, Tetouan ou Fes est plus frequent."),
        ],
    },
    "guide_desert_marocain.pdf": {
        "title": "Guide touristique - Desert marocain",
        "sections": [
            ("Merzouga", "Merzouga est connue pour les dunes de l'Erg Chebbi, les bivouacs, les balades a dos de dromadaire et les levers de soleil. L'experience est spectaculaire mais le trajet depuis Marrakech ou Fes peut etre long."),
            ("Zagora", "Zagora est souvent choisie pour une experience desert plus courte depuis Marrakech. Les dunes sont moins impressionnantes que Merzouga, mais l'itineraire convient mieux aux sejours courts."),
            ("Precautions", "Dans le desert, il faut prevoir de l'eau, une protection solaire, des vetements adaptes, une veste pour la nuit, et verifier les conditions avec l'organisateur. Les temperatures peuvent etre extremes entre le jour et la nuit."),
            ("Saisons", "L'automne, l'hiver et le printemps sont les meilleures saisons pour le desert. En ete, la chaleur peut rendre les activites difficiles, surtout en milieu de journee."),
        ],
    },
    "conseils_pratiques_voyage_maroc.pdf": {
        "title": "Conseils pratiques pour voyager au Maroc",
        "sections": [
            ("Budget", "Le budget depend de la ville, du niveau d'hebergement, des transports et des activites. Pour maitriser les couts, il faut reserver a l'avance, comparer train et bus, manger dans des restaurants locaux et limiter les longs trajets prives."),
            ("Culture", "Le voyageur doit respecter les habitudes locales, demander l'autorisation avant de photographier des personnes, adapter sa tenue dans les lieux religieux ou traditionnels et apprendre quelques mots de base en arabe marocain ou en francais."),
            ("Securite", "Il est conseille de garder ses documents en lieu sur, d'utiliser des moyens de transport officiels, de verifier les prix avant un service et d'eviter les zones isolees la nuit dans une ville inconnue."),
            ("Preparation", "Avant le depart, il faut verifier le passeport, l'assurance voyage, les reservations, la meteo, les horaires de train ou de bus, et garder une copie numerique des documents importants."),
        ],
    },
}


def _create_pdf(path: Path, title: str, sections: list[tuple[str, str]]) -> None:
    from reportlab.lib.pagesizes import A4
    from reportlab.lib.styles import getSampleStyleSheet
    from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer

    styles = getSampleStyleSheet()
    doc = SimpleDocTemplate(str(path), pagesize=A4, title=title)
    story = [Paragraph(title, styles["Title"]), Spacer(1, 12)]
    for heading, text in sections:
        story.append(Paragraph(heading, styles["Heading2"]))
        story.append(Paragraph(text, styles["BodyText"]))
        story.append(Spacer(1, 10))
    doc.build(story)


def download_all() -> None:
    PDF_DIR.mkdir(parents=True, exist_ok=True)
    for filename, payload in DOCUMENTS.items():
        dest = PDF_DIR / filename
        if dest.exists():
            print(f"OK (deja present) : {filename}")
            continue
        _create_pdf(dest, payload["title"], payload["sections"])
        size_kb = dest.stat().st_size / 1024
        print(f"Cree : {filename} ({size_kb:.0f} KB)")


if __name__ == "__main__":
    download_all()
