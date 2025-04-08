
# https://www.youtube.com/watch?v=yf2xznF30-s
# styling the printouts

from rich import print
from rich.console import Console



shrek_info = {
    "title": "Shrek",
    "release_year": 2001,
    "genre": ["Animation", "Fantasy", "Comedy"],
    "based_on": "'Shrek!' by William Steig (1990 children's book)",
    "directors": ["Andrew Adamson", "Vicky Jenson"],
    "writers": ["Ted Elliott", "Terry Rossio", "Joe Stillman", "Roger S. H. Schulman"],
    "producers": ["Aron Warner", "John H. Williams", "Jeffrey Katzenberg"],
    "cast": {
        "Shrek": "Mike Myers",
        "Donkey": "Eddie Murphy",
        "Princess Fiona": "Cameron Diaz",
        "Lord Farquaad": "John Lithgow"
    },
    "plot_summary": (
        "Shrek, an anti-social ogre, embarks on a quest to rescue Princess Fiona "
        "from a dragon-guarded tower in exchange for reclaiming his swamp, which "
        "has been overrun by fairytale creatures exiled by Lord Farquaad."
    ),
    "themes": [
        "Self-acceptance",
        "True love",
        "Breaking stereotypes",
        "Friendship"
    ],
    "technical_details": {
        "animation_technology": [
            "PDI proprietary software for skeletal and muscle systems",
            "Maya clothing simulation for realistic fabric movement"
        ],
        "notable_features": [
            "Dynamic fur rendering for Donkey and other elements like grass and moss",
            "Advanced facial and body animations for realism"
        ],
        "sequences_and_shots": {"total_sequences": 31, "total_shots": 1288},
    },
    "box_office": {
        "budget": "$60 million",
        "gross_revenue": "$492.5 million"
    },
    "awards_and_impact": {
        "awards": [
            {
                "name": "Academy Award for Best Animated Feature",
                "year": 2002,
                "note": "*Shrek* was the first film to win this category."
            }
        ],
        "cultural_impact": [
            (
                "*Shrek* revitalized the fairy tale parody genre and became a cultural "
                'phenomenon with its humor, relatable themes, and memorable characters.'
            ),
            (
                'Inspired sequels, spin-offs (e.g., *Puss in Boots*), a Broadway musical, '
                'and video games.'
            ),
            (
                'Became a meme icon with lasting influence on internet culture, including '
                '"Shrek is Love, Shrek is Life" and other ironic gags.'
            )
        ]
    },
    "franchise_details": {
        "sequels_and_spinoffs": [
            "*Shrek 2* (2004)",
            "*Shrek the Third* (2007)",
            "*Shrek Forever After* (2010)",
            "*Puss in Boots* (2011)"
        ],
        "future_projects": {
            "*Shrek 5* release_date": ["December 23, 2026"],
            "*Puss in Boots 2* release_date": ["July 1, 2026"]
        }
    },
    "fun_facts": [
        (
            'The production team visited locations like Hearst Castle and Dordogne, France '
            'to design Duloc and other settings.'
        ),
        (
            'The film’s humor includes adult-oriented jokes that balance its appeal '
            'to both children and adults.'
        ),
        (
            '*Shrek* has been described as a work of art that challenges fantasy tropes '
            'and promotes self-love and acceptance.'
        )
    ]
}



# print(shrek_info)  # the print is much clearer instead of if we didn't install rich


console = Console()

def compare_numbers(a,b):
	if a > b:
		console.print(f"{a} is greater than {b}", style="bold green") # style is optional
		# print(f"{a} is greater than {b}") # without the rich we would see unicolor instead of special color for the numbers
	elif a < b:
		console.print(f"{a} is less than {b}", style="bold red")
		# print(f"{a} is less than {b}")
	else:
		console.print(f"{a} is equal to {b}", style="purple")
		# print(f"{a} is equal to {b}")

compare_numbers(5, 10)
compare_numbers(10, 5)
compare_numbers(5, 5)


from rich.theme import Theme # for theme dictionary

custom_theme = Theme({'error': 'bold red', 'warning': 'yellow', 'info': 'purple'})

console = Console(theme=custom_theme)

print()

def compare_numbers(a,b):
	console.log(log_locals=True) # to view the local values from the params (also TS for when it has started)
	if a > b:
		console.print(f"{a} is greater than {b}", style="error") # style is optional
	elif a < b:
		console.print(f"{a} is less than {b}", style="warning")
	else:
		console.print(f"{a} is equal to {b}", style="info")


compare_numbers(4, 9) # now using theme
compare_numbers(9, 4)
compare_numbers(4, 4)


from rich.traceback import install

install()


compare_numbers(4, "shai")
# the install() help to beautify the traceback error

