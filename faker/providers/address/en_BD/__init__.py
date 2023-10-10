"""
    Contributed by: @aamibhoot 🇧🇩
"""

from .. import Provider as AddressProvider


class Provider(AddressProvider):
    area_names = (
        "Ali",
        "Alam",
        "Abhay",
        "Anwar",
        "Brahmin",
        "Botia",
        "Baghar",
        "Begum",
        "Bijoy",
        "Bandar",
        "Balia",
        "Bajit",
        "Baker",
        "Borhan",
        "Bakhsh",
        "Badr",
        "Biram",
        "Biswnath",
        "Chouddah",
        "Chital",
        "Daud",
        "Daulat",
        "Dev",
        "Devi",
        "Islam",
        "Ful",
        "Fakir",
        "Fatik",
        "Gopal",
        "Gour",
        "Haji",
        "Hariram",
        "Hossain",
        "Hakim",
        "Jibon",
        "Jagannath",
        "Kumar",
        "Kali",
        "Keshav",
        "Qutub",
        "Kabi",
        "Kalia",
        "Karim",
        "Kazi",
        "Kamal",
        "Lal",
        "Murad",
        "Manohar",
        "Mir",
        "Mahes",
        "Moral",
        "Molla",
        "Mohammad",
        "Maniram",
        "Manik",
        "Mirza",
        "Mud",
        "Mohan",
        "Mahadev",
        "Madhab",
        "Nasir",
        "Naria",
        "Nazir",
        "Nalitha",
        "Nandi",
        "Osmani",
        "Pai",
        "Palash",
        "Parvati",
        "Ram",
        "Ray",
        "Rani",
        "Sona",
        "Sharan",
        "Shyam",
        "Subarna",
        "Siraj",
        "Sakhi",
        "Sadar",
        "Sundar",
        "Syed",
        "Shahjahan",
        "Shanti",
        "Shib",
        "Ter",
        "Tara",
        "Uzir",
    )

    building_names = (
        "House No.",
        "Building No.",
        "House No.",
        "Holding No.",
    )

    building_number_formats = ("%", "%#", "%##")

    city_prefixes = ("North", "East", "West", "South", "Middle", "New", "Old")

    city_suffixes = (
        "Bazar",
        "Bari",
        "Char",
        "Diya",
        "Danga",
        "Ganz",
        "Gram",
        "Gan",
        "Gan",
        "Garh",
        "Hat",
        "Har",
        "Khali",
        "Mati",
        "Nagar",
        "Pur",
        "Tala",
    )

    cities = (
        "Barguna",
        "Barisal",
        "Bhola",
        "Bandarban",
        "Brahmanbaria",
        "Bagherhat",
        "Bogura",
        "Chandpur",
        "Chittagong",
        "Cumilla",
        "Cox's Bazar",
        "Chuadanga",
        "Dhaka",
        "Dinajpur",
        "Faripur",
        "Feni",
        "Gazipur",
        "Gopalganj",
        "Gaibandha",
        "Habiganj",
        "Jhalokati",
        "Jessore",
        "Jhenaidah",
        "Jamalpur",
        "Joypurhat",
        "Khagrachhari",
        "Kishoreganj",
        "Khulna",
        "Kushtia",
        "Kurigram",
        "Lakshmipur",
        "Lalmonirhat",
        "Madaripur",
        "Manikganj",
        "Munshiganj",
        "Magura",
        "Meherpur",
        "Mymensingh",
        "Maulvibazar",
        "Noakhali",
        "Narayanganj",
        "Narsingdi",
        "Narail",
        "Netrokona",
        "Naogaon",
        "Naogaon",
        "Chapainawabganj",
        "Nilphamari",
        "Patuakhali",
        "Pirojpur",
        "Pabna",
        "Panchagarh",
        "Rangpur",
        "Shariatpur",
        "Satkhira",
        "Sherpur",
        "Sirajganj",
        "Sunamganj",
        "Sylhet",
        "Tangail",
        "Thakurgaon",
    )

    countries = (
        "Afghanistan",
        "Albania",
        "Algeria",
        "American Samoa",
        "Andorra",
        "Angola",
        "Anguilla",
        "Antarctica (the territory South of 60 deg S)",
        "Antigua and Barbuda",
        "Argentina",
        "Armenia",
        "Aruba",
        "Australia",
        "Austria",
        "Azerbaijan",
        "Bahamas",
        "Bahrain",
        "Bangladesh",
        "Barbados",
        "Belarus",
        "Belgium",
        "Belize",
        "Benin",
        "Bermuda",
        "Bhutan",
        "Bolivia",
        "Bosnia and Herzegovina",
        "Botswana",
        "Bouvet Island (Bouvetoya)",
        "Brazil",
        "British Indian Ocean Territory (Chagos Archipelago)",
        "British Virgin Islands",
        "Brunei Darussalam",
        "Bulgaria",
        "Burkina Faso",
        "Burundi",
        "Cambodia",
        "Cameroon",
        "Canada",
        "Cape Verde",
        "Cayman Islands",
        "Central African Republic",
        "Chad",
        "Chile",
        "China",
        "Christmas Island",
        "Cocos (Keeling) Islands",
        "Colombia",
        "Comoros",
        "Congo",
        "Congo",
        "Cook Islands",
        "Costa Rica",
        "Cote d'Ivoire",
        "Croatia",
        "Cuba",
        "Cyprus",
        "Czech Republic",
        "Denmark",
        "Djibouti",
        "Dominica",
        "Dominican Republic",
        "Ecuador",
        "Egypt",
        "El Salvador",
        "Equatorial Guinea",
        "Eritrea",
        "Estonia",
        "Ethiopia",
        "Faroe Islands",
        "Falkland Islands (Malvinas)",
        "Fiji",
        "Finland",
        "France",
        "French Guiana",
        "French Polynesia",
        "French Southern Territories",
        "Gabon",
        "Gambia",
        "Georgia",
        "Germany",
        "Ghana",
        "Gibraltar",
        "Greece",
        "Greenland",
        "Grenada",
        "Guadeloupe",
        "Guam",
        "Guatemala",
        "Guernsey",
        "Guinea",
        "Guinea-Bissau",
        "Guyana",
        "Haiti",
        "Heard Island and McDonald Islands",
        "Holy See (Vatican City State)",
        "Honduras",
        "Hong Kong",
        "Hungary",
        "Iceland",
        "India",
        "Indonesia",
        "Iran",
        "Iraq",
        "Ireland",
        "Isle of Man",
        "Israel",
        "Italy",
        "Jamaica",
        "Japan",
        "Jersey",
        "Jordan",
        "Kazakhstan",
        "Kenya",
        "Kiribati",
        "Korea",
        "Korea",
        "Kuwait",
        "Kyrgyz Republic",
        "Lao People's Democratic Republic",
        "Latvia",
        "Lebanon",
        "Lesotho",
        "Liberia",
        "Libyan Arab Jamahiriya",
        "Liechtenstein",
        "Lithuania",
        "Luxembourg",
        "Macao",
        "Madagascar",
        "Malawi",
        "Malaysia",
        "Maldives",
        "Mali",
        "Malta",
        "Marshall Islands",
        "Martinique",
        "Mauritania",
        "Mauritius",
        "Mayotte",
        "Mexico",
        "Micronesia",
        "Moldova",
        "Monaco",
        "Mongolia",
        "Montenegro",
        "Montserrat",
        "Morocco",
        "Mozambique",
        "Myanmar",
        "Namibia",
        "Nauru",
        "Nepal",
        "Netherlands Antilles",
        "Netherlands",
        "New Caledonia",
        "New Zealand",
        "Nicaragua",
        "Niger",
        "Nigeria",
        "Niue",
        "Norfolk Island",
        "North Macedonia",
        "Northern Mariana Islands",
        "Norway",
        "Oman",
        "Pakistan",
        "Palau",
        "Palestinian Territory",
        "Panama",
        "Papua New Guinea",
        "Paraguay",
        "Peru",
        "Philippines",
        "Pitcairn Islands",
        "Poland",
        "Portugal",
        "Puerto Rico",
        "Qatar",
        "Reunion",
        "Romania",
        "Russian Federation",
        "Rwanda",
        "Saint Barthelemy",
        "Saint Helena",
        "Saint Kitts and Nevis",
        "Saint Lucia",
        "Saint Martin",
        "Saint Pierre and Miquelon",
        "Saint Vincent and the Grenadines",
        "Samoa",
        "San Marino",
        "Sao Tome and Principe",
        "Saudi Arabia",
        "Senegal",
        "Serbia",
        "Seychelles",
        "Sierra Leone",
        "Singapore",
        "Slovakia (Slovak Republic)",
        "Slovenia",
        "Solomon Islands",
        "Somalia",
        "South Africa",
        "South Georgia and the South Sandwich Islands",
        "Spain",
        "Sri Lanka",
        "Sudan",
        "Suriname",
        "Svalbard & Jan Mayen Islands",
        "Swaziland",
        "Sweden",
        "Switzerland",
        "Syrian Arab Republic",
        "Taiwan",
        "Tajikistan",
        "Tanzania",
        "Thailand",
        "Timor-Leste",
        "Togo",
        "Tokelau",
        "Tonga",
        "Trinidad and Tobago",
        "Tunisia",
        "Turkey",
        "Turkmenistan",
        "Turks and Caicos Islands",
        "Tuvalu",
        "Uganda",
        "Ukraine",
        "United Arab Emirates",
        "United Kingdom",
        "United States of America",
        "United States Minor Outlying Islands",
        "United States Virgin Islands",
        "Uruguay",
        "Uzbekistan",
        "Vanuatu",
        "Venezuela",
        "Vietnam",
        "Wallis and Futuna",
        "Western Sahara",
        "Yemen",
        "Zambia",
        "Zimbabwe",
    )

    secondary_address_formats = (
        "Flat %",
        "Flat %#",
        "Studio %",
        "Studio %#",
        "Apartment %",
        "Apartment %#",
    )

    street_suffixes = (
        "Avenue",
        "Center",
        "Square",
        "Lane",
        "Ghat",
        "Corner",
        "Lane",
        "Highway",
        "Mohalla",
        "Moor",
        "Para",
        "Park",
        "Plaza",
        "Road",
        "Road",
        "Sorok",
        "Station",
        "Stand",
    )

    postcode_formats = ("%###",)
    street_name_formats = (
        "{{area_name}}{{street_suffix}}",
        "{{city_prefix}} {{area_name}}{{street_suffix}}",
        "{{city_prefix}} {{area_name}}{{city_suffix}}",
        "{{area_name}}{{city_suffix}}",
        "{{area_name}}{{city_suffix}} {{street_suffix}}",
        "{{city_prefix}} {{area_name}}{{city_suffix}} {{street_suffix}}",
    )
    street_address_formats = (
        "{{building_name}} {{building_number}}, {{street_name}}",
        "{{secondary_address}}, {{building_name}} {{building_number}}, {{street_name}}",
    )
    town_formats = ("{{area_name}}{{city_suffix}}",)
    address_formats = ("{{street_address}}, {{town}}, {{city}}, {{postcode}}",)

    def administrative_unit(self) -> str:
        """
        :example: 'Dhaka'
        """
        return self.random_element(self.cities)

    def area_name(self) -> str:
        """
        :example: 'Dhanmondi'
        """
        return self.random_element(self.area_names)

    def building_name(self) -> str:
        """
        :example: 'House No.'
        """
        return self.random_element(self.building_names)

    def building_number(self) -> str:
        """
        :example: '791'
        """
        return self.numerify(self.random_element(self.building_number_formats))

    def city_prefix(self) -> str:
        """
        :example: 'North'
        """
        return self.random_element(self.city_prefixes)

    def city(self) -> str:
        """
        :example: 'Dhaka'
        """
        return self.random_element(self.cities)

    def postcode(self) -> str:
        """
        See
        https://bdpost.portal.gov.bd/site/page/6aaeabe4-479b-4e5a-a671-e9e5b994bf9a
        """
        return self.numerify(self.random_element(self.postcode_formats))

    def secondary_address(self) -> str:
        """
        As the generated string format is a Bengali word but English number so splitting the value by space
        and then convert the English number to Bengali number and concat with generated Bengali word
        and return
        : example : 'Apartment 123'
        """
        value = self.bothify(self.random_element(self.secondary_address_formats))
        word_list = value.split(" ")
        return word_list[0] + " " + word_list[1]

    def town(self) -> str:
        """
        :example: 'Dhanmondi'
        """
        pattern: str = self.random_element(self.town_formats)
        return self.generator.parse(pattern)