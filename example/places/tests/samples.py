from places.models import Continent, Country, City


# Some translation spellings are written wrong on purpose to be able to
# test them
CONTINENTS = [
    {
        "code": "EU",
        "name": "Europe",
        "denonym": "European",
        "translations": [
            # de
            {
                "field": "name",
                "language": "de",
                "text": "Europa",
            },
            {
                "field": "denonym",
                "language": "de",
                "text": "Europäisch",
            },
            # tr
            {
                "field": "name",
                "language": "tr",
                "text": "Avrupa",
            },
            {
                "field": "denonym",
                "language": "tr",
                "text": "Avrupalı",
            },
        ],
    },
    {
        "code": "AS",
        "name": "Asia",
        "denonym": "Asian",
        "translations": [
            # de
            {
                "field": "name",
                "language": "de",
                "text": "Asien",
            },
            {
                "field": "denonym",
                "language": "de",
                "text": "Asiatisch",
            },
            # tr
            {
                "field": "name",
                "language": "tr",
                "text": "Asya",
            },
            {
                "field": "denonym",
                "language": "tr",
                "text": "Asyalı",
            },
        ],
    },
    {
        "code": "AF",
        "name": "Africa",
        "denonym": "African",
        "translations": [
            # de
            {
                "field": "name",
                "language": "de",
                "text": "Afrika",
            },
            {
                "field": "denonym",
                "language": "de",
                "text": "Afrikanisch",
            },
            # tr
            {
                "field": "name",
                "language": "tr",
                "text": "Afrika",
            },
            {
                "field": "denonym",
                "language": "tr",
                "text": "Afrikalı",
            },
        ],
    },
    {
        "code": "NA",
        "name": "North America",
        "denonym": "North American",
        "translations": [
            # de
            {
                "field": "name",
                "language": "de",
                "text": "Nordamerika",
            },
            {
                "field": "denonym",
                "language": "de",
                "text": "Nordamerikanisch",
            },
            # tr
            {
                "field": "name",
                "language": "tr",
                "text": "Kuzey Amerika",
            },
            {
                "field": "denonym",
                "language": "tr",
                "text": "Kuzey Amerikalı",
            },
        ],
    },
    {
        "code": "SA",
        "name": "South America",
        "denonym": "South American",
        "translations": [
            # de
            {
                "field": "name",
                "language": "de",
                "text": "Südamerika",
            },
            {
                "field": "denonym",
                "language": "de",
                "text": "Südamerikanisch",
            },
            # tr
            {
                "field": "name",
                "language": "tr",
                "text": "Güney Amerika",
            },
            {
                "field": "denonym",
                "language": "tr",
                "text": "Güney Amerikalı",
            },
        ],
    },
    {
        "code": "AU",
        "name": "Australia",
        "denonym": "Australian",
        "translations": [
            # de
            {
                "field": "name",
                "language": "de",
                "text": "Australien",
            },
            {
                "field": "denonym",
                "language": "de",
                "text": "Australisch",
            },
            # tr
            {
                "field": "name",
                "language": "tr",
                "text": "Avustralya",
            },
            {
                "field": "denonym",
                "language": "tr",
                "text": "Avustralyalı",
            },
        ],
    },
]

COUNTRIES = [
    # Europe
    {
        "code": "DE",
        "name": "Germany",
        "denonym": "German",
        "translations": [
            # de
            {
                "field": "name",
                "language": "de",
                "text": "Deutschland",
            },
            {
                "field": "denonym",
                "language": "de",
                "text": "Deutsche",
            },
            # tr
            {
                "field": "name",
                "language": "tr",
                "text": "Almanya",
            },
            {
                "field": "denonym",
                "language": "tr",
                "text": "Almanca",
            },
        ],
    },
    {
        "code": "TR",
        "name": "Turkey",
        "denonym": "Turk",
        "translations": [
            # de
            {
                "field": "name",
                "language": "de",
                "text": "Türkei",
            },
            {
                "field": "denonym",
                "language": "de",
                "text": "Türke",
            },
            # tr
            {
                "field": "name",
                "language": "tr",
                "text": "Türkiye",
            },
            {
                "field": "denonym",
                "language": "tr",
                "text": "Türk",
            },
        ],
    },
    # Asia
    {
        "code": "KR",
        "name": "South Korea",
        "denonym": "South Korean",
        "translations": [
            # de
            {
                "field": "name",
                "language": "de",
                "text": "Südkorea",
            },
            {
                "field": "denonym",
                "language": "de",
                "text": "Südkoreanisch",
            },
            # tr
            {
                "field": "name",
                "language": "tr",
                "text": "Güney Kore",
            },
            {
                "field": "denonym",
                "language": "tr",
                "text": "Güney Korelı",
            },
        ],
    },
    {
        "code": "IN",
        "name": "India",
        "denonym": "Indian",
        "translations": [
            # de
            {
                "field": "name",
                "language": "de",
                "text": "Indien",
            },
            {
                "field": "denonym",
                "language": "de",
                "text": "Indisch",
            },
            # tr
            {
                "field": "name",
                "language": "tr",
                "text": "Hindistan",
            },
            {
                "field": "denonym",
                "language": "tr",
                "text": "Hintlı",
            },
        ],
    },
    # Africa
    {
        "code": "EG",
        "name": "Egypt",
        "denonym": "Egyptian",
        "translations": [
            # de
            {
                "field": "name",
                "language": "de",
                "text": "Ägypten",
            },
            {
                "field": "denonym",
                "language": "de",
                "text": "Ägyptisch",
            },
            # tr
            {
                "field": "name",
                "language": "tr",
                "text": "Mısır",
            },
            {
                "field": "denonym",
                "language": "tr",
                "text": "Mısırlı",
            },
        ],
    },
    {
        "code": "ZA",
        "name": "South Africa",
        "denonym": "South African",
        "translations": [
            # de
            {
                "field": "name",
                "language": "de",
                "text": "Südafrika",
            },
            {
                "field": "denonym",
                "language": "de",
                "text": "Südafrikanisch",
            },
            # tr
            {
                "field": "name",
                "language": "tr",
                "text": "Güney Afrika",
            },
            {
                "field": "denonym",
                "language": "tr",
                "text": "Güney Afrikalı",
            },
        ],
    },
    # North America
    {
        "code": "US",
        "name": "United States of America",
        "denonym": "American",
        "translations": [
            # de
            {
                "field": "name",
                "language": "de",
                "text": "Vereinigte Staaten von Amerika",
            },
            {
                "field": "denonym",
                "language": "de",
                "text": "Amerikanisch",
            },
            # tr
            {
                "field": "name",
                "language": "tr",
                "text": "Amerika Birleşik Devletleri",
            },
            {
                "field": "denonym",
                "language": "tr",
                "text": "Amerikalı",
            },
        ],
    },
    {
        "code": "MX",
        "name": "Mexico",
        "denonym": "Mexican",
        "translations": [
            # de
            {
                "field": "name",
                "language": "de",
                "text": "Mexiko",
            },
            {
                "field": "denonym",
                "language": "de",
                "text": "Mexikaner",
            },
            # tr
            {
                "field": "name",
                "language": "tr",
                "text": "Meksika",
            },
            {
                "field": "denonym",
                "language": "tr",
                "text": "Meksikalı",
            },
        ],
    },
    # South America
    {
        "code": "BR",
        "name": "Brazil",
        "denonym": "Brazilian",
        "translations": [
            # de
            {
                "field": "name",
                "language": "de",
                "text": "Brasilien",
            },
            {
                "field": "denonym",
                "language": "de",
                "text": "Brasilianisch",
            },
            # tr
            {
                "field": "name",
                "language": "tr",
                "text": "Brezilya",
            },
            {
                "field": "denonym",
                "language": "tr",
                "text": "Brezilyalı",
            },
        ],
    },
    {
        "code": "AR",
        "name": "Argentina",
        "denonym": "Argentinian",
        "translations": [
            # de
            {
                "field": "name",
                "language": "de",
                "text": "Argentinien",
            },
            {
                "field": "denonym",
                "language": "de",
                "text": "Argentinisch",
            },
            # tr
            {
                "field": "name",
                "language": "tr",
                "text": "Arjantin",
            },
            {
                "field": "denonym",
                "language": "tr",
                "text": "Arjantinlı",
            },
        ],
    },
    # Australia
    {
        "code": "ID",
        "name": "Indonesia",
        "denonym": "Indonesian",
        "translations": [
            # de
            {
                "field": "name",
                "language": "de",
                "text": "Indonesien",
            },
            {
                "field": "denonym",
                "language": "de",
                "text": "Indonesier",
            },
            # tr
            {
                "field": "name",
                "language": "tr",
                "text": "Endonezya",
            },
            {
                "field": "denonym",
                "language": "tr",
                "text": "Endonezyalı",
            },
        ],
    },
    {
        "code": "NZ",
        "name": "New Zealand",
        "denonym": "New Zealandian",
        "translations": [
            # de
            {
                "field": "name",
                "language": "de",
                "text": "Neuseeland",
            },
            {
                "field": "denonym",
                "language": "de",
                "text": "Neuseeländisch",
            },
            # tr
            {
                "field": "name",
                "language": "tr",
                "text": "Yeni Zelanda",
            },
            {
                "field": "denonym",
                "language": "tr",
                "text": "Yeni Zelandalı",
            },
        ],
    },
]

CITIES = [
    # Germany
    {
        "name": "Cologne",
        "denonym": "Cologner",
        "translations": [
            # de
            {
                "field": "name",
                "language": "de",
                "text": "Köln",
            },
            {
                "field": "denonym",
                "language": "de",
                "text": "Kölner",
            },
            # tr
            {
                "field": "name",
                "language": "tr",
                "text": "Koln",
            },
            {
                "field": "denonym",
                "language": "tr",
                "text": "Kolnlı",
            },
        ],
    },
    {
        "name": "Munich",
        "denonym": "Munichian",
        "translations": [
            # de
            {
                "field": "name",
                "language": "de",
                "text": "München",
            },
            {
                "field": "denonym",
                "language": "de",
                "text": "Münchner",
            },
            # tr
            {
                "field": "name",
                "language": "tr",
                "text": "Münih",
            },
            {
                "field": "denonym",
                "language": "tr",
                "text": "Münihlı",
            },
        ],
    },
    # Turkey
    {
        "name": "Istanbul",
        "denonym": "Istanbulian",
        "translations": [
            # de
            {
                "field": "name",
                "language": "de",
                "text": "Ïstanbul",
            },
            {
                "field": "denonym",
                "language": "de",
                "text": "Ïstanbulisch",
            },
            # tr
            {
                "field": "name",
                "language": "tr",
                "text": "İstanbul",
            },
            {
                "field": "denonym",
                "language": "tr",
                "text": "İstanbullı",
            },
        ],
    },
    {
        "name": "Izmir",
        "denonym": "Izmirian",
        "translations": [
            # de
            {
                "field": "name",
                "language": "de",
                "text": "Ïzmir",
            },
            {
                "field": "denonym",
                "language": "de",
                "text": "Ïzmirisch",
            },
            # tr
            {
                "field": "name",
                "language": "tr",
                "text": "İzmir",
            },
            {
                "field": "denonym",
                "language": "tr",
                "text": "İzmirlı",
            },
        ],
    },
    # South Korea
    {
        "name": "Seoul",
        "denonym": "Seouler",
        "translations": [
            # de
            {
                "field": "name",
                "language": "de",
                "text": "Seül",
            },
            {
                "field": "denonym",
                "language": "de",
                "text": "Seülisch",
            },
            # tr
            {
                "field": "name",
                "language": "tr",
                "text": "Seul",
            },
            {
                "field": "denonym",
                "language": "tr",
                "text": "Seullı",
            },
        ],
    },
    {
        "name": "Ulsan",
        "denonym": "Ulsanian",
        "translations": [
            # de
            {
                "field": "name",
                "language": "de",
                "text": "Ulsän",
            },
            {
                "field": "denonym",
                "language": "de",
                "text": "Ulsänisch",
            },
            # tr
            {
                "field": "name",
                "language": "tr",
                "text": "Ülsan",
            },
            {
                "field": "denonym",
                "language": "tr",
                "text": "Ülsanlı",
            },
        ],
    },
    # India
    {
        "name": "Mumbai",
        "denonym": "Mumbaian",
        "translations": [
            # de
            {
                "field": "name",
                "language": "de",
                "text": "Mumbaï",
            },
            {
                "field": "denonym",
                "language": "de",
                "text": "Mumbäisch",
            },
            # tr
            {
                "field": "name",
                "language": "tr",
                "text": "Bombay",
            },
            {
                "field": "denonym",
                "language": "tr",
                "text": "Bombaylı",
            },
        ],
    },
    {
        "name": "New Delhi",
        "denonym": "New Delhian",
        "translations": [
            # de
            {
                "field": "name",
                "language": "de",
                "text": "Neu-Delhi",
            },
            {
                "field": "denonym",
                "language": "de",
                "text": "Neu-Delhisch",
            },
            # tr
            {
                "field": "name",
                "language": "tr",
                "text": "Yeni Delhi",
            },
            {
                "field": "denonym",
                "language": "tr",
                "text": "Yeni Delhilı",
            },
        ],
    },
    # Egypt
    {
        "name": "Cairo",
        "denonym": "Cairoian",
        "translations": [
            # de
            {
                "field": "name",
                "language": "de",
                "text": "Kairo",
            },
            {
                "field": "denonym",
                "language": "de",
                "text": "Kairoisch",
            },
            # tr
            {
                "field": "name",
                "language": "tr",
                "text": "Kahire",
            },
            {
                "field": "denonym",
                "language": "tr",
                "text": "Kahirelı",
            },
        ],
    },
    {
        "name": "Giza",
        "denonym": "Gizean",
        "translations": [
            # de
            {
                "field": "name",
                "language": "de",
                "text": "Gizeh",
            },
            {
                "field": "denonym",
                "language": "de",
                "text": "Gizisch",
            },
            # tr
            {
                "field": "name",
                "language": "tr",
                "text": "Çizeh",
            },
            {
                "field": "denonym",
                "language": "tr",
                "text": "Çizehlı",
            },
        ],
    },
    # South Africa
    {
        "name": "Cape Town",
        "denonym": "Cape Towner",
        "translations": [
            # de
            {
                "field": "name",
                "language": "de",
                "text": "Kapstadt",
            },
            {
                "field": "denonym",
                "language": "de",
                "text": "Kapstadtisch",
            },
            # tr
            {
                "field": "name",
                "language": "tr",
                "text": "Kap Şehri",
            },
            {
                "field": "denonym",
                "language": "tr",
                "text": "Kap Şehrilı",
            },
        ],
    },
    {
        "name": "Johannesburg",
        "denonym": "Johannesburgian",
        "translations": [
            # de
            {
                "field": "name",
                "language": "de",
                "text": "Johannesbürg",
            },
            {
                "field": "denonym",
                "language": "de",
                "text": "Johannesbürgisch",
            },
            # tr
            {
                "field": "name",
                "language": "tr",
                "text": "Yohannesburg",
            },
            {
                "field": "denonym",
                "language": "tr",
                "text": "Yohannesburglı",
            },
        ],
    },
    # United States of America
    {
        "name": "New York",
        "denonym": "New Yorker",
        "translations": [
            # de
            {
                "field": "name",
                "language": "de",
                "text": "Neu York",
            },
            {
                "field": "denonym",
                "language": "de",
                "text": "Neu Yorkisch",
            },
            # tr
            {
                "field": "name",
                "language": "tr",
                "text": "Yeni York",
            },
            {
                "field": "denonym",
                "language": "tr",
                "text": "Yeni Yorklı",
            },
        ],
    },
    {
        "name": "New Jersey",
        "denonym": "New Jersean",
        "translations": [
            # de
            {
                "field": "name",
                "language": "de",
                "text": "Neu Jersey",
            },
            {
                "field": "denonym",
                "language": "de",
                "text": "Neu Jersisch",
            },
            # tr
            {
                "field": "name",
                "language": "tr",
                "text": "Yeni Jersey",
            },
            {
                "field": "denonym",
                "language": "tr",
                "text": "Yeni Jerseylı",
            },
        ],
    },
    # Mexico
    {
        "name": "Mexico City",
        "denonym": "Mexico Citian",
        "translations": [
            # de
            {
                "field": "name",
                "language": "de",
                "text": "Mexiko Stadt",
            },
            {
                "field": "denonym",
                "language": "de",
                "text": "Mexiko Stadtisch",
            },
            # tr
            {
                "field": "name",
                "language": "tr",
                "text": "Meksika şehri",
            },
            {
                "field": "denonym",
                "language": "tr",
                "text": "Meksika şehrilı",
            },
        ],
    },
    {
        "name": "Cancun",
        "denonym": "Cancunian",
        "translations": [
            # de
            {
                "field": "name",
                "language": "de",
                "text": "Cancún",
            },
            {
                "field": "denonym",
                "language": "de",
                "text": "Cancúnisch",
            },
            # tr
            {
                "field": "name",
                "language": "tr",
                "text": "Cancün",
            },
            {
                "field": "denonym",
                "language": "tr",
                "text": "Cancünlı",
            },
        ],
    },
    # Brazil
    {
        "name": "Sao Paulo",
        "denonym": "Sao Paulean",
        "translations": [
            # de
            {
                "field": "name",
                "language": "de",
                "text": "São Paulo",
            },
            {
                "field": "denonym",
                "language": "de",
                "text": "São Paulisch",
            },
            # tr
            {
                "field": "name",
                "language": "tr",
                "text": "Sao Paülo",
            },
            {
                "field": "denonym",
                "language": "tr",
                "text": "Sao Paülolı",
            },
        ],
    },
    {
        "name": "Rio de Janeiro",
        "denonym": "Rio de Janeirean",
        "translations": [
            # de
            {
                "field": "name",
                "language": "de",
                "text": "Rio von Janeiro",
            },
            {
                "field": "denonym",
                "language": "de",
                "text": "Rio von Janeirisch",
            },
            # tr
            {
                "field": "name",
                "language": "tr",
                "text": "Rio de Janeirü",
            },
            {
                "field": "denonym",
                "language": "tr",
                "text": "Rio de Janeirülı",
            },
        ],
    },
    # Argentina
    {
        "name": "Buenos Aires",
        "denonym": "Buenos Airesean",
        "translations": [
            # de
            {
                "field": "name",
                "language": "de",
                "text": "Büenos Äires",
            },
            {
                "field": "denonym",
                "language": "de",
                "text": "Büenos Äiresisch",
            },
            # tr
            {
                "field": "name",
                "language": "tr",
                "text": "Büenos Aires",
            },
            {
                "field": "denonym",
                "language": "tr",
                "text": "Büenos Aireslı",
            },
        ],
    },
    {
        "name": "Tucuman",
        "denonym": "Tucumanian",
        "translations": [
            # de
            {
                "field": "name",
                "language": "de",
                "text": "Tucumán",
            },
            {
                "field": "denonym",
                "language": "de",
                "text": "Tucumánisch",
            },
            # tr
            {
                "field": "name",
                "language": "tr",
                "text": "Tucüman",
            },
            {
                "field": "denonym",
                "language": "tr",
                "text": "Tucümanlı",
            },
        ],
    },
    # Indonesia
    {
        "name": "Jakarta",
        "denonym": "Jakartean",
        "translations": [
            # de
            {
                "field": "name",
                "language": "de",
                "text": "Jäkarta",
            },
            {
                "field": "denonym",
                "language": "de",
                "text": "Jäkartaisch",
            },
            # tr
            {
                "field": "name",
                "language": "tr",
                "text": "Jákarta",
            },
            {
                "field": "denonym",
                "language": "tr",
                "text": "Jákartalı",
            },
        ],
    },
    {
        "name": "Surabaya",
        "denonym": "Surabayean",
        "translations": [
            # de
            {
                "field": "name",
                "language": "de",
                "text": "Suräbaya",
            },
            {
                "field": "denonym",
                "language": "de",
                "text": "Suräbayisch",
            },
            # tr
            {
                "field": "name",
                "language": "tr",
                "text": "Suràbaya",
            },
            {
                "field": "denonym",
                "language": "tr",
                "text": "Suràbayalı",
            },
        ],
    },
    # New Zealand
    {
        "name": "Auckland",
        "denonym": "Aucklandean",
        "translations": [
            # de
            {
                "field": "name",
                "language": "de",
                "text": "Äuckland",
            },
            {
                "field": "denonym",
                "language": "de",
                "text": "Äucklandisch",
            },
            # tr
            {
                "field": "name",
                "language": "tr",
                "text": "Akland",
            },
            {
                "field": "denonym",
                "language": "tr",
                "text": "Aklandlı",
            },
        ],
    },
    {
        "name": "Wellington",
        "denonym": "Wellingtonian",
        "translations": [
            # de
            {
                "field": "name",
                "language": "de",
                "text": "Wellingtön",
            },
            {
                "field": "denonym",
                "language": "de",
                "text": "Wellingtönisch",
            },
            # tr
            {
                "field": "name",
                "language": "tr",
                "text": "Velington",
            },
            {
                "field": "denonym",
                "language": "tr",
                "text": "Velingtonlı",
            },
        ],
    },
]


def create_continent(name, fields=None, langs=None):
    fields = fields if fields is not None else []
    langs = langs if langs is not None else []
    for continent in CONTINENTS:
        if name.lower() == continent["name"].lower():
            translations = continent["translations"]
            continent = Continent.objects.create(
                code=continent["code"],
                name=continent["name"],
                denonym=continent["denonym"],
            )
            break
    else:
        raise ValueError("No continent named `{}`.".format(name))

    for translation in translations:
        if translation["field"] in fields and translation["language"] in langs:
            continent.translations.create(**translation)

    return continent


def create_country(continent, name, fields=None, langs=None):
    fields = fields if fields is not None else []
    langs = langs if langs is not None else []
    for country in COUNTRIES:
        if name.lower() == country["name"].lower():
            translations = country["translations"]
            country = Country.objects.create(
                continent=continent,
                code=country["code"],
                name=country["name"],
                denonym=country["denonym"],
            )
            break
    else:
        raise ValueError("No country named `{}`.".format(name))

    for translation in translations:
        if translation["field"] in fields and translation["language"] in langs:
            country.translations.create(**translation)

    return country


def create_city(country, name, fields=None, langs=None):
    fields = fields if fields is not None else []
    langs = langs if langs is not None else []
    for city in CITIES:
        if name.lower() == city["name"].lower():
            translations = city["translations"]
            city = City.objects.create(
                country=country,
                name=city["name"],
                denonym=city["denonym"],
            )
            break
    else:
        raise ValueError("No country named `{}`.".format(name))

    for translation in translations:
        if translation["field"] in fields and translation["language"] in langs:
            city.translations.create(**translation)

    return city